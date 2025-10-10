# Demonstrate classical expressions (XOR parity) for GHZ-like state
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.classical import expr

num_qubits = 8
if num_qubits % 2 or num_qubits < 4:
        raise ValueError("num_qubits must be even >= 4")

# Measurement targets (every second qubit starting from 2)
meas_qubits = list(range(2, num_qubits, 2))

qr = QuantumRegister(num_qubits, "qr")
mr = ClassicalRegister(len(meas_qubits), "m")
qc = QuantumCircuit(qr, mr)

print("Step 1: Reset all qubits.")
qc.reset(qr)

print("Step 2: Create local Bell pairs.")
qc.h(qr[::2])  # Hadamard on even-indexed qubits
for ctrl in range(0, num_qubits, 2):
        qc.cx(qr[ctrl], qr[ctrl + 1])

print("Step 3: Glue pairs with CNOTs.")
for ctrl in range(1, num_qubits - 1, 2):
        qc.cx(qr[ctrl], qr[ctrl + 1])

print("Step 4: Measure and reset selected qubits.")
for k, q in enumerate(meas_qubits):
        qc.measure(qr[q], mr[k])
        qc.reset(qr[q])

print("Step 5: Apply parity-conditioned X corrections.")
for tgt in range(num_qubits):
        if tgt in meas_qubits:
                continue
        left_bits = [k for k, q in enumerate(meas_qubits) if q < tgt]
        if not left_bits:
                continue
        parity = expr.lift(mr[left_bits[0]])
        for k in left_bits[1:]:
                parity = expr.bit_xor(mr[k], parity)
        with qc.if_test(parity):
                qc.x(qr[tgt])

print("Step 6: Re-entangle measured qubits with CNOTs.")
for ctrl in range(1, num_qubits - 1, 2):
        qc.cx(qr[ctrl], qr[ctrl + 1])

print("\nCircuit created:\n", qc)

"""
SUMMARY:
- Demonstrates using classical expressions (bitwise XOR) in dynamic circuits.
- Steps:
        1. Reset all qubits.
        2. Create Bell pairs on even-odd qubit pairs.
        3. Entangle across pairs with CNOTs.
        4. Measure and reset boundary qubits.
        5. Use XOR parity of prior measurements to conditionally flip qubits.
        6. Re-establish entanglement with CNOTs.
"""
