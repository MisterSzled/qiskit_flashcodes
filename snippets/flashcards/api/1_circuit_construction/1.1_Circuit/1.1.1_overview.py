"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Quantum Circuit Model (qiskit.circuit)
"""

# ---------------------------------------------------------------
"""
# Question 1
Which statement best describes the difference between an abstract circuit and a physical circuit in Qiskit 2.x?

a. An abstract circuit can only contain measurement and reset operations.  
b. A physical circuit is defined purely in terms of virtual qubits.  
c. A physical circuit is defined in terms of hardware qubits and native operations supported by a specific backend.  
d. An abstract circuit must be compiled with transpile() before any simulation.  
"""

from qiskit import QuantumCircuit, transpile

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# Convert from abstract to physical circuit for a mock backend
physical_qc = transpile(qc, optimization_level=1)
print(physical_qc)

# ---------------------------------------------------------------
"""
# Question 2
What does the QuantumCircuit.ensure_physical() method do in Qiskit 2.x?

a. It forces a circuit to only use basis gates supported by a target backend.  
b. It validates that a circuit is logically correct for abstract simulation.  
c. It rewrites circuit metadata so qubit indices are recognized as physical qubits.  
d. It replaces all virtual qubits with ancilla qubits.  
"""

from qiskit import QuantumCircuit
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc = transpile(qc, backend=FakeManilaV2())
print("Circuit transpiled to physical qubits and native gates for FakeManila.")


# ---------------------------------------------------------------
"""
# Question 3
In Qiskit terminology, which of the following correctly defines a hardware qubit?

a. A mathematical placeholder representing any quantum state.  
b. A virtual qubit used for simulation only.  
c. A single physical or logical qubit exposed by the QPU for real operations.  
d. A temporary ancilla qubit automatically deleted after measurement.  
"""

from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)  # Acts on a hardware qubit when executed on a QPU
qc.measure_all()
print(qc)

# ---------------------------------------------------------------
"""
# Question 4
Which Qiskit object represents a single computational routine executed one shot at a time on a QPU?

a. QuantumRegister  
b. QuantumCircuit  
c. InstructionSet  
d. ClassicalRegister  
"""

from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.measure_all()
print("QuantumCircuit defines the full computational routine per shot.")

# ---------------------------------------------------------------
"""
# Question 5
In the context of the quantum circuit model, which statement about measurement is correct?

a. Measurement preserves entanglement between qubits.  
b. Measurement is a reversible unitary operation.  
c. Measurement extracts one classical bit and destroys phase coherence.  
d. Measurement converts physical qubits to virtual qubits.  
"""

from qiskit import QuantumCircuit

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
print("Measurement added; circuit now outputs a classical bit.")

# ---------------------------------------------------------------
"""
Answer Key Summary
------------------
1. c  
2. c  
3. c  
4. b  
5. c  
"""
