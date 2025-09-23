# Demonstrate Qiskit Runtime limitations in classical feedforward
from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister

# --- Setup ---
qr = QuantumRegister(2, "q")
cr = ClassicalRegister(65, "c")  # allocate 65 bits to test broadcast limit
qc = QuantumCircuit(qr, cr)

(q0, q1) = qr

print("Step 1: Apply Hadamard to q0 and measure into c[0].")
qc.h(q0)
qc.measure(q0, cr[0])

# --- Limitation 1: Classical register size (<= 32 bits per operand) ---
print("\n[Limitation 1] Register operand size must be ≤ 32 bits.")
try:
        # This is invalid: using full 65-bit register as condition
        with qc.if_test((cr, 0b1)):
                qc.x(q1)
        print("❌ Unexpected: Accepted >32-bit register!")
except Exception as e:
        print("✅ Expected error:", e)

# --- Valid case (≤ 32-bit slice) ---
print("\n[Valid] Using 32-bit slice of classical register as condition.")
slice32 = cr[:32]
with qc.if_test((slice32, 0b1)):
        qc.x(q1)

# --- Limitation 2: Broadcast bit count (≤ 60) ---
print("\n[Limitation 2] Broadcasts limited to ≤ 60 classical bits.")
try:
        qc.measure(qr, cr[:65])  # attempt 65-bit broadcast
        print("❌ Unexpected: Accepted >60-bit broadcast!")
except Exception as e:
        print("✅ Expected error:", e)

# --- Valid broadcast ---
print("\n[Valid] Broadcasting into 2 classical bits only.")
qc.measure(qr, cr[:2])

# --- Limitation 3: No nesting of if-tests ---
print("\n[Limitation 3] Nested if-statements are not supported.")
try:
        with qc.if_test((cr[0], 1)):
                with qc.if_test((cr[1], 1)):
                        qc.x(q1)
        print("❌ Unexpected: Accepted nested if-tests!")
except Exception as e:
        print("✅ Expected error:", e)

print("\nFinal circuit (valid parts only):\n", qc)

"""
SUMMARY:
- Shows Qiskit Runtime dynamic circuit restrictions:
        1. Classical register operands limited to 32 bits (invalid: >32).
        2. Broadcasts limited to ≤ 60 classical bits (invalid: >60).
        3. Nested if-statements not supported.
- Provided valid vs invalid cases with error logging.
"""
