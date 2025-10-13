"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Transpiler (qiskit.transpiler)
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
What is the main purpose of the Qiskit transpiler?

a. To visualize circuits in different backends.  
b. To rewrite and optimize a quantum circuit to match a specific hardware topology.  
c. To convert circuits into OpenQASM format.  
d. To measure all qubits in a circuit.

# Minimal runnable example:
# from qiskit import QuantumCircuit, transpile
# qc = QuantumCircuit(2)
# qc.h(0); qc.cx(0, 1)
# tqc = transpile(qc, optimization_level=2)
# tqc.draw('text')
"""
from qiskit import QuantumCircuit, transpile

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
tqc = transpile(qc, optimization_level=2)
print(tqc)

# ---------------------------------------------------------------
"""
# Question 2
In the transpilation process, what intermediate representation (IR) does Qiskit use internally?

a. QuantumCircuitTree  
b. DAGCircuit  
c. TensorNetwork  
d. QASM3Graph

# Minimal runnable example:
# from qiskit.converters import circuit_to_dag
# dag = circuit_to_dag(qc)
# print(type(dag))
"""
from qiskit.converters import circuit_to_dag

dag = circuit_to_dag(qc)
print("Intermediate representation type:", type(dag))

# ---------------------------------------------------------------
"""
# Question 3
What is the role of a `PassManager` in the Qiskit transpiler stack?

a. It stores the compiled binaries for the circuit.  
b. It schedules jobs on IBM Quantum backends.  
c. It defines and executes a sequence of analysis and transformation passes on a circuit.  
d. It handles device calibration data.

# Minimal runnable example:
# from qiskit.transpiler import PassManager
# from qiskit.transpiler.passes import Optimize1qGates
# pm = PassManager([Optimize1qGates()])
# out = pm.run(qc)
# out.draw('text')
"""
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Optimize1qGates

pm = PassManager([Optimize1qGates()])
out = pm.run(qc)
print(out)

# ---------------------------------------------------------------
"""
# Question 4
What is the recommended entry point for generating a fully configured transpilation pipeline for a backend?

a. qiskit.transpiler.TranspileManager()  
b. qiskit.transpiler.generate_preset_pass_manager()  
c. qiskit.transpiler.compile_pipeline()  
d. qiskit.transpiler.generate_default_pass_set()

# Minimal runnable example:
# from qiskit.transpiler import generate_preset_pass_manager
# from qiskit_ibm_runtime import QiskitRuntimeService
# backend = QiskitRuntimeService().backend("ibm_sherbrooke")
# pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
# physical = pm.run(qc)
# print(physical)
"""
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService

# (This example will only run with a valid IBM Quantum account)
# backend = QiskitRuntimeService().backend("ibm_sherbrooke")
# pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
# physical = pm.run(qc)
# print(physical)
