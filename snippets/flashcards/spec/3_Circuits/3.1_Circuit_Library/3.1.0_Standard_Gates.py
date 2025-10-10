from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate, MCXGate

# Create gates from the circuit library
mcx_gate = MCXGate(3)     # Multi-controlled X gate with 3 controls
hadamard_gate = HGate()   # Single-qubit Hadamard gate

# Build a 4-qubit circuit
qc = QuantumCircuit(4)
qc.append(hadamard_gate, [0])            # Apply H to qubit 0
qc.append(mcx_gate, [0, 1, 2, 3])        # Apply MCX across qubits 0–3

print("Circuit with Hadamard and Multi-controlled X gate:")
print(qc)

"""
Summary:
- Demonstrates importing and using standard gates from the circuit library.
- Steps:
        1. Import HGate and MCXGate.
        2. Create a 4-qubit circuit.
        3. Append H on qubit 0.
        4. Append MCX on qubits [0,1,2,3].
"""
