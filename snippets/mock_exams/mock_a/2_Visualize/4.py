"""

4. Which one of the following statements is used to create a conditional (if) block in a Qiskit circuit?

a. qc.for_loop((c0,1))
b. qc.if_test((c0,1))
c. qc.while_loop((c0,1))
d. qc.switch((c0,1))

"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

qubits = QuantumRegister(2)
clbits = ClassicalRegister(2)
circuit = QuantumCircuit(qubits, clbits)

(q0, q1) = qubits
(c0, c1) = clbits

circuit.h(q0)
circuit.measure(q0, c0)

# Conditional blocks (if/else based on c0)
with circuit.if_test((c0, 1)) as else_:
        circuit.h(q1)
with else_:
        circuit.x(q1)

circuit.measure(q1, c1)

# --- Draw circuit (mpl output) ---
print(circuit)
circuit.draw(output="mpl", filename="circuit.png")