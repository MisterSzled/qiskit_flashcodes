# ---------------------------------------------------------------
"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Primitives — SamplerV2 Overview
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1 — Purpose of SamplerV2
What is the main role of a `BaseSamplerV2` primitive in Qiskit 2.x?

a. To compile quantum circuits into backend-specific instructions.  
b. To sample measurement outcomes (bitstrings) from quantum circuits.  
c. To estimate expectation values of observables.  
d. To optimize the topology mapping of quantum gates.
"""

from qiskit.primitives import StatevectorSampler as Sampler
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

sampler = Sampler()
result = sampler.run([qc]).result()
print("Sampled distribution:", result)

# ---------------------------------------------------------------
"""
# Question 2 — Core Input Unit
What is a *Primitive Unified Bloc* (PUB) when used with `SamplerV2`?

a. A JSON serialization format for measurement results.  
b. A self-contained data unit describing one computational task (circuit + parameters + shots).  
c. A classical optimization layer for parameter tuning.  
d. A backend configuration schema.
"""

# PUBs define the "unit of work" for primitives, containing circuit, parameter sets, and shots.

# ---------------------------------------------------------------
"""
# Question 3 — Parameterized Circuit Usage
In the following code, what does `[(pqc, theta1), (pqc2, theta2)]` represent in the `run()` call?

from qiskit.primitives import StatevectorSampler as Sampler
from qiskit.circuit.library import RealAmplitudes
from qiskit import QuantumCircuit

pqc = RealAmplitudes(num_qubits=2, reps=2)
pqc.measure_all()
pqc2 = RealAmplitudes(num_qubits=2, reps=3)
pqc2.measure_all()

theta1 = [0, 1, 1, 2, 3, 5]
theta2 = [0, 1, 2, 3, 4, 5, 6, 7]

sampler = Sampler()
job = sampler.run([(pqc, theta1), (pqc2, theta2)])
res = job.result()
print("Results length:", len(res.quasi_dists))

a. A list of (circuit, parameter_values) tuples defining multiple PUBs.  
b. A mapping from circuits to their observable operators.  
c. A list of backend configuration options.  
d. A queue of asynchronous simulator threads.
"""

# Each tuple corresponds to a separate sampling job with different parameter bindings.

# ---------------------------------------------------------------
"""
# Question 4 — Shots Parameter
In SamplerV2, what happens if the number of `shots` is not explicitly provided when calling `run()`?

a. The sampler automatically infers it from the backend noise model.  
b. The sampler uses a default number of shots specified during initialization.  
c. The sampler fails with a missing argument error.  
d. The sampler always performs analytical (infinite-shot) sampling.
"""

# By default, StatevectorSampler performs analytical sampling, but shots can be specified if desired.

sampler = Sampler(default_shots=128)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
result = sampler.run([qc]).result()
print("Number of sampled distributions:", len(result))

# ---------------------------------------------------------------
"""
# Question 5 — Return Type
When you execute `sampler.run([...])`, what type of object is returned before calling `.result()`?

a. BasePrimitiveJob  
b. SamplerResult  
c. BackendJob  
d. QuantumJobV2
"""

from qiskit.primitives import BaseSamplerV2
print(isinstance(sampler, BaseSamplerV2))
job = sampler.run([qc])
print("Type of returned object:", type(job).__name__)

# ---------------------------------------------------------------
"""
# Question 6 — Output Structure
What does calling `.result()` on a `BasePrimitiveJob` from a sampler return?

a. A tuple of raw bitstrings and metadata.  
b. A result object containing quasi-probability distributions and metadata for each PUB.  
c. Only a histogram of classical register values.  
d. A JSON string encoding the backend configuration.
"""

# Example run producing quasi distributions (normalized probabilities)
print(job.result())

# ---------------------------------------------------------------
"""
# Question 7 — Reference Implementations
Which two SamplerV2 implementations are included in Qiskit 2.x?

a. NoiseAdaptiveSampler and RealisticSampler  
b. StatevectorSampler and BackendSamplerV2  
c. ClassicalSampler and MatrixSampler  
d. IdealSampler and ExperimentalSampler
"""

from qiskit.primitives import BackendSamplerV2
print(isinstance(BackendSamplerV2, type))

# ---------------------------------------------------------------
"""
# Question 8 — BackendSamplerV2
What does the `BackendSamplerV2` class do?

a. It simulates ideal results using a full statevector backend.  
b. It evaluates bitstrings for circuits executed on a real or simulated backend.  
c. It estimates expectation values of observables.  
d. It generates randomized benchmarking sequences.
"""

from qiskit.providers.fake_provider import GenericBackendV2
backend = GenericBackendV2(num_qubits=2)
backend_sampler = BackendSamplerV2(backend=backend)
print(isinstance(backend_sampler, BackendSamplerV2))

# ---------------------------------------------------------------
"""
# Question 9 — Multi-PUB Jobs
What happens when multiple PUBs are submitted to a single `SamplerV2.run()` call?

a. Each PUB is executed sequentially with a separate job ID.  
b. The sampler executes all PUBs as a batch, returning one result with multiple distributions.  
c. Only the first PUB executes successfully.  
d. The sampler raises a ValueError for multiple circuits.
"""

# SamplerV2 supports batching of multiple PUBs within a single call.
job2 = sampler.run([qc, qc])
print("Number of quasi distributions returned:", len(job2.result()))

# ---------------------------------------------------------------
"""
# Question 10 — Conceptual Summary
Which statement best summarizes the design philosophy of SamplerV2?

a. It replaces all backend APIs with lightweight samplers for probabilistic simulation.  
b. It provides a unified, extensible interface for sampling from circuits using either simulated or hardware backends.  
c. It only supports classical sampling through approximate simulation.  
d. It is a visualization utility for measurement outcomes.
"""

# SamplerV2 provides a uniform interface across simulators and hardware, via unified PUB definitions.
