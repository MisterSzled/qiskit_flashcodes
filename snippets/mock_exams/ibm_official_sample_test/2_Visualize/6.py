# 6. Which one of the following code fragments will generate
# the given qsphere representation visualization?
# Note: the circles on the qsphere are the same color.
#
# a.
# qc = QuantumCircuit(2)
# qc.h(0)
# qc.z(0)
# qc.cx(0, 1)
# state = Statevector(qc)
# plot_state_qsphere(state)
#
# b.
# qc = QuantumCircuit(2)
# qc.h(0)
# qc.z(0)
# qc.x(1)
# qc.cx(0, 1)
# state = Statevector(qc)
# plot_state_qsphere(state)
#
# c.
# qc = QuantumCircuit(2)
# qc.x(1)
# qc.h(0)
# qc.cx(0, 1)
# state = Statevector(qc)
# plot_state_qsphere(state)
#
# d.
# qc = QuantumCircuit(2)
# qc.h(0)
# qc.cx(0, 1)
# state = Statevector(qc)
# plot_state_qsphere(state)

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

# --- Define all four candidate circuits ---
def option_a():
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.z(0)
        qc.cx(0, 1)
        return qc

def option_b():
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.z(0)
        qc.x(1)
        qc.cx(0, 1)
        return qc

def option_c():
        qc = QuantumCircuit(2)
        qc.x(1)
        qc.h(0)
        qc.cx(0, 1)
        return qc

def option_d():
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        return qc

# --- Collect all options ---
options = {
        "a": option_a(),
        "b": option_b(),
        "c": option_c(),
        "d": option_d(),
}

# --- Generate and save qsphere plots ---
for label, qc in options.items():
        state = Statevector.from_instruction(qc)
        fig = plot_state_qsphere(state)
        filename = f"qsphere_option_{label}.png"
        fig.savefig(filename)
