# 5. Given the code fragment below, which image is the expected output?
# from qiskit.quantum_info import Statevector
# from qiskit.visualization import plot_histogram
# state = Statevector([0.+0.j, 0.+0.j, 0.70710678+0.j, 0.+0.j,
#                      0.+0.j, -0.70710678+0.j, 0.+0.j, 0.+0.j])
# counts = state.sample_counts(shots=1024)
# plot_histogram(counts)
#
# a. A histogram showing counts mostly in |010> and |101>
# b. A histogram showing counts mostly in |011> and |110>
# c. A histogram showing counts mostly in |001> and |100>
# d. A histogram showing counts mostly in |000> and |111>

from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram

# Define the statevector
state = Statevector([
        0.+0.j, 
        0.+0.j, 
        0.70710678+0.j, 
        0.+0.j,
        0.+0.j, 
        -0.70710678+0.j, 
        0.+0.j, 
        0.+0.j
])

# Sample measurement outcomes (simulated counts)
counts = state.sample_counts(shots=1024)

# Plot histogram of measurement results
plot_histogram(counts)
fig = plot_histogram(counts)

# Step 5: Show or save the figure
fig.show()          # Opens interactive window (if supported)
fig.savefig("bell_histogram.png")  # Save instead of showing