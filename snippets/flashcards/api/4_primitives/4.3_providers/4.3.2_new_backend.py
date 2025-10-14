# ===============================================================
# QISKIT 2.x MOCK EXAM — WRITING A NEW BACKEND
# ===============================================================

# ---------------------------------------------------------------
"""
# Question 1 — Purpose of a Custom Backend
What is the main reason for writing a new Backend in Qiskit?

a. To define a custom quantum job execution interface for a specific device or simulator.
b. To replace the Provider system with custom transpiler passes.
c. To visualize circuits differently from Matplotlib.
d. To directly compile OpenQASM programs without a provider.

"""
# minimal runnable demo
from qiskit_ibm_runtime.fake_provider import FakeManilaV2
backend = FakeManilaV2()
backend_name = backend.backend_name
print("Backend name:", backend_name)

# ---------------------------------------------------------------
"""
# Question 2 — Provider Class Fundamentals
Which statement correctly describes a Qiskit Provider?

a. A Provider is a factory that manages and returns Backend instances.
b. A Provider directly executes quantum circuits on hardware.
c. A Provider stores circuit results and visualization data.
d. A Provider replaces the transpiler and scheduler subsystems.

"""

# ---------------------------------------------------------------
"""
# Question 3 — BackendV2 Core Requirements
When implementing a custom BackendV2, which attribute must always be defined?

a. `backend_name`
b. `target`
c. `job_limit`
d. `service_url`

"""
# minimal runnable demo
from qiskit_ibm_runtime.fake_provider import FakeManilaV2
target = FakeManilaV2().target
print("Target qubits:", target.items)

# ---------------------------------------------------------------
"""
# Question 4 — Target and Transpiler Interface
What does the `Target` object represent in a BackendV2 implementation?

a. A mapping of supported instructions, qubits, and their properties.
b. A configuration file describing backend memory usage.
c. A cache of all jobs previously executed.
d. A parameter vector used during optimization.

"""
# minimal runnable demo
print("Has HGate:", "h" in target)

# ---------------------------------------------------------------
"""
# Question 5 — Adding Custom Basis Gates
How can you extend a backend's supported operations?

a. By adding Gate objects to the backend's Target.
b. By redefining the transpiler PassManager.
c. By subclassing QuantumCircuit.
d. By creating a new Provider subclass.

"""
# minimal runnable demo
from qiskit.transpiler import Target
from qiskit.circuit.library import XGate

# Create a clean Target with no predefined instructions
target = Target(num_qubits=1)

# Add a custom instruction (here, XGate)
target.add_instruction(XGate())

print("Added XGate:", "x" in target)

# ---------------------------------------------------------------
"""
# Question 6 — Registering Equivalence Rules
How can you register new equivalence transformations for a backend?

a. Using an `EquivalenceLibrary` and calling `add_equivalence()`.
b. By editing the backend's run() method directly.
c. By redefining the TranspileConfig.
d. By modifying the backend.job() factory.

"""
# minimal runnable demo
from qiskit.circuit.equivalence import EquivalenceLibrary
from qiskit.circuit import QuantumCircuit
elib = EquivalenceLibrary()
qc = QuantumCircuit(1)
qc.x(0)
elib.add_equivalence(XGate(), qc)
print("Equivalence rules:", len(elib.get_entry(XGate())))

# ---------------------------------------------------------------
"""
# Question 7 — Backend Options and Validators
How are custom backend runtime parameters defined and checked?

a. By adding entries to the `backend.options` object with validation.
b. By subclassing the transpiler passes.
c. By updating the backend configuration file directly.
d. By overriding the Provider's __init__.

"""
# minimal runnable demo
backend.options.set_validator("shots", int)
backend.options.shots = 512
print("Backend shots:", backend.options.shots)

# ---------------------------------------------------------------
"""
# Question 8 — Implementing run()
Which is the minimal required argument of the backend `run()` method?

a. circuits
b. transpiler_passes
c. run_config
d. provider

"""
# minimal runnable demo
from qiskit import QuantumCircuit
qc = QuantumCircuit(1)
qc.h(0)
job = backend.run(qc, shots=8)
print("Job ID:", job.job_id())

# ---------------------------------------------------------------
"""
# Question 9 — JobV1 Subclass
Why would you subclass JobV1 when defining a new backend?

a. To implement asynchronous job submission and custom result handling.
b. To define a new transpilation strategy.
c. To optimize pulse scheduling.
d. To replace the Options object.

"""
# minimal runnable demo
from qiskit.providers.job import JobV1
print("JobV1 is subclassable:", issubclass(type(job), JobV1))

# ---------------------------------------------------------------
"""
# Question 10 — Transpiler Stage Plugins
How can a custom backend influence transpilation for its circuits?

a. By exposing a `Target` object with operation definitions.
b. By redefining the qiskit.transpiler module.
c. By injecting custom register bindings.
d. By bypassing the transpiler completely.

"""
# minimal runnable demo
from qiskit.transpiler import CouplingMap
cm = backend.coupling_map
print("Coupling edges:", len(cm.get_edges()))

# ---------------------------------------------------------------
"""
# Question 11 — Real-Time Variables and Bounds
Which attribute defines allowable numeric ranges for real-valued gate parameters?

a. `ParameterBounds` inside the backend's Target instruction properties.
b. `Options` validators for the backend.
c. `Provider` connection settings.
d. `QuantumCircuit` metadata.

"""
# minimal runnable demo
from qiskit.transpiler import Target
from qiskit.circuit.library import RXGate

target = Target(num_qubits=1)

# Add RXGate and define its parameter bounds directly in the Target metadata
target.add_instruction(RXGate(3.14159))

# Define numeric range for the RXGate’s θ parameter

# Retrieve and print
print("RX angle bounds:", target)

# ---------------------------------------------------------------
"""
# Question 12 — Provider-Level Integration
What enables multiple backends to be grouped and accessed consistently?

a. Their common Provider instance.
b. A shared transpiler pass manager.
c. Identical run() method signatures.
d. A single job submission queue.

"""
# minimal runnable demo
print("Provider name:", backend.backend_name)
