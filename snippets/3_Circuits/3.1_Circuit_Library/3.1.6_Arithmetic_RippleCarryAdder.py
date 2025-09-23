from qiskit.circuit.library import FullAdderGate
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.primitives import StatevectorSampler

# Create a ripple-carry adder for 3-bit numbers
adder = FullAdderGate(3)

# Quantum registers for inputs
reg_a = QuantumRegister(3, "a")
number_a = QuantumCircuit(reg_a)
number_a.initialize(2)  # Encode A=2 (|010>)

reg_b = QuantumRegister(3, "b")
number_b = QuantumCircuit(reg_b)
number_b.initialize(3)  # Encode B=3 (|011>)

# Full circuit: cin, a, b, cout + classical register
qregs = [
        QuantumRegister(1, "cin"),
        QuantumRegister(3, "a"),
        QuantumRegister(3, "b"),
        QuantumRegister(1, "cout"),
]
reg_result = ClassicalRegister(3)
circuit = QuantumCircuit(*qregs, reg_result)

# Compose numbers and adder into main circuit
circuit = (
        circuit.compose(number_a, qubits=reg_a)
        .compose(number_b, qubits=reg_b)
        .compose(adder)
)
circuit.measure(reg_b, reg_result)

print("Ripple-carry adder circuit for A=2, B=3:")
print(circuit)

# Simulate using StatevectorSampler
result = StatevectorSampler().run([circuit]).result()
print("Measurement results:", result[0].data.c0.get_int_counts())

"""
Summary:
- Demonstrates arithmetic circuits with FullAdderGate.
- Steps:
        1. Build registers for two 3-bit numbers (A=2, B=3).
        2. Create ripple-carry adder.
        3. Compose numbers + adder into one circuit.
        4. Measure result in B's register.
        5. Simulate with StatevectorSampler to confirm result=5.
"""
