# 8. Which one of the following types of register stores the result of a measured circuit?
#
# a. Ancillary register
# b. Quantum register
# c. Classical register
# d. Circuit register

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# --- Option A: Ancillary register (used for temporary qubits, not measurement storage) ---
anc = QuantumRegister(1, "ancilla")
qc_a = QuantumCircuit(anc)
qc_a.h(0)
print("\nOption A circuit (ancillary qubit):")
print(qc_a.draw())

# --- Option B: Quantum register (holds qubit states) ---
qreg = QuantumRegister(1, "q")
qc_b = QuantumCircuit(qreg)
qc_b.x(0)
print("\nOption B circuit (quantum register):")
print(qc_b.draw())

# --- Option C: Classical register (stores measurement results) ---
q = QuantumRegister(1, "q")
c = ClassicalRegister(1, "c")
qc_c = QuantumCircuit(q, c)
qc_c.h(0)
qc_c.measure(0, 0)
print("\nOption C circuit (quantum + classical registers):")
print(qc_c.draw())

# --- Option D: Circuit register (not a valid Qiskit register type) ---
try:
        # This will fail because 'CircuitRegister' doesn't exist
        from qiskit.circuit import CircuitRegister
        qc_d = QuantumCircuit(CircuitRegister(1, "circ"))
except Exception as e:
        print("\nOption D error:", e)

"""
SUMMARY:
- Demonstrates different register types in Qiskit.
- Quantum registers hold qubits; classical registers hold measurement outcomes.
- Ancillary registers are special-purpose qubits, not for storing measurement results.
- CircuitRegister is not a valid register type in Qiskit 2.x.
"""
