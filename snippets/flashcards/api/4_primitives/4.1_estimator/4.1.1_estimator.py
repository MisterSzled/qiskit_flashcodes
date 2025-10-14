# ---------------------------------------------------------------
"""
# Qiskit 2.x Mock Exam — Primitives
# Covers: Sampler, Estimator, and their V1/V2 abstractions.
# Includes runnable code examples and conceptual multiple-choice questions.
"""

# ---------------------------------------------------------------
"""
# Question 1 — Primitive Definition
In Qiskit 2.x, what is the purpose of a *primitive*?

a. It defines the syntax rules for OpenQASM circuits.  
b. It acts as a fundamental computational building block for quantum tasks.  
c. It compiles classical functions into quantum instructions.  
d. It defines hardware-specific noise models.
"""

from qiskit.primitives import StatevectorSampler
print(isinstance(StatevectorSampler(), StatevectorSampler))

# ---------------------------------------------------------------
"""
# Question 2 — Primitive Categories
Which of the following correctly lists the two major primitive types introduced in Qiskit 2.x?

a. Estimators and Builders  
b. Executors and Samplers  
c. Samplers and Estimators  
d. Backends and Executors
"""

# Samplers → sample classical outputs
# Estimators → compute observable expectation values

# ---------------------------------------------------------------
"""
# Question 3 — Sampler Functionality
What is the role of a `Sampler` primitive?

a. It computes the expectation value of an observable.  
b. It samples measurement outcomes from quantum circuits.  
c. It synthesizes circuits into the target basis.  
d. It performs symbolic differentiation on circuit parameters.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1)
qc.h(0)
sampler = StatevectorSampler()
result = sampler.run([qc]).result()
print(result)

# ---------------------------------------------------------------
"""
# Question 4 — Estimator Functionality
What is the role of an `Estimator` primitive?

a. It measures the fidelity between two quantum states.  
b. It estimates expectation values of observables given circuits.  
c. It compiles quantum circuits into backend-specific instructions.  
d. It generates randomized benchmarking circuits.
"""

from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator

qc = QuantumCircuit(1)
qc.h(0)
obs = SparsePauliOp("Z")

estimator = StatevectorEstimator()
res = estimator.run([(qc, obs)]).result()
print(res)  # Expected ≈ 0.0

# ---------------------------------------------------------------
"""
# Question 5 — Base Class Hierarchy
Which base classes define the latest primitive abstractions in Qiskit 2.x?

a. BaseSamplerV1 and BaseEstimatorV1  
b. BaseSamplerV2 and BaseEstimatorV2  
c. BaseSampler and BaseEstimator (no version suffix)  
d. SamplerBase and EstimatorBase
"""

from qiskit.primitives import BaseSamplerV2, BaseEstimatorV2
print(issubclass(StatevectorEstimator, BaseEstimatorV2))

# ---------------------------------------------------------------
"""
# Question 6 — Migration from V1 to V2
What is the key improvement of V2 primitives over V1?

a. V2 introduces a unified input/output model (PUBs) supporting parameter sweeps.  
b. V2 uses asynchronous GPU-based execution only.  
c. V2 removes all abstract base class dependencies.  
d. V2 eliminates all use of backends.
"""

# V2 primitives generalize the interface via primitive unified blocks (PUBs).

# ---------------------------------------------------------------
"""
# Question 7 — Reference Implementations
Which of the following provides a *reference* (i.e., simulator-based) implementation of the new primitives?

a. BackendEstimatorV2 and BackendSamplerV2  
b. StatevectorEstimator and StatevectorSampler  
c. EstimatorCore and SamplerCore  
d. LocalEstimatorV2 and LocalSamplerV2
"""

# Both StatevectorEstimator and StatevectorSampler simulate ideal noiseless outcomes.

# ---------------------------------------------------------------
"""
# Question 8 — Backend-Connected Estimator
What is true about `BackendEstimatorV2`?

a. It only supports classical backends.  
b. It estimates observables using circuits executed on a given backend.  
c. It is limited to a single qubit.  
d. It cannot accept observables as input.
"""

from qiskit_ibm_runtime.fake_provider import FakeManilaV2
from qiskit.primitives import BackendEstimatorV2

backend = FakeManilaV2()

backend_estimator = BackendEstimatorV2(backend=backend)
print("Q8 demo backend_estimator is instance:", isinstance(backend_estimator, BackendEstimatorV2))


# ---------------------------------------------------------------
"""
# Question 9 — PUB Concept
In the Qiskit Primitives API, what are *Primitive Unified Blocks* (PUBs)?

a. Lightweight quantum gates for performance optimization.  
b. Input/output data units encapsulating all arguments for a single primitive execution.  
c. Classical caching layers used by transpiler passes.  
d. Dynamically loaded C++ acceleration kernels.
"""

# PUBs are the core input units for Estimators and Samplers in V2.

# ---------------------------------------------------------------
"""
# Question 10 — Example Comparison
What does the following code demonstrate?

from qiskit.primitives import StatevectorSampler, StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)
obs = SparsePauliOp("Z")

sampler = StatevectorSampler()
estimator = StatevectorEstimator()

sampled = sampler.run([qc]).result().quasi_dists[0]
estimated = estimator.run([(qc, obs)]).result().values[0]

print(sampled, estimated)

a. Sampler gives bitstring probabilities; Estimator gives expectation values.  
b. Both return expectation values.  
c. Both return probability distributions.  
d. Estimator performs sampling before computing expectations.
"""

# Demonstrates: Sampler → distribution; Estimator → expectation value.