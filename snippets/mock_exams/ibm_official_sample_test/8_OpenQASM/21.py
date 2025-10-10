# 21. Which method should be used to export a Qiskit circuit named qc to OpenQASM 3
# and store it into a file stream named qasmprogram?
#
# a. qc.to_openqasm3(qasmprogram)
# b. qiskit.qasm3.dump(qc, qasmprogram)
# c. qasmprogram.export_to_qasm3(qc)
# d. qiskit.qasm3.export(qc, qasmprogram)

from qiskit import QuantumCircuit
import qiskit.qasm3

# Create a simple circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Open a file stream and export the circuit to OpenQASM 3
with open("example.qasm", "w") as qasmprogram:
        qiskit.qasm3.dump(qc, qasmprogram)  # <-- fully demonstrates the correct usage

print("Circuit exported to OpenQASM 3 in 'example.qasm'.")

"""
SUMMARY:
        - The Qiskit 2.x correct method to export a QuantumCircuit to OpenQASM 3 is:
                qiskit.qasm3.dump(qc, qasmprogram)
        - This writes the circuit directly into the provided file stream.
        - Other options in the question are invalid in Qiskit 2.x.
"""
