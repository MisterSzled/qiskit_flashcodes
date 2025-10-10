"""

Given the code fragment below, which image is the expected output?

from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram

state = Statevector([0.70710678+0.j, 0.+0.j, 0.70710678+0.j, 0.+0.j])
counts = state.sample_counts(shots=1024)

plot_histogram(counts)

a. Bars at outcomes 00 and 01 only
b. Bars at outcomes 01 and 11 only
c. Bars at outcomes 00 and 10 only
d. Bars at outcomes 10 and 11 only

"""

