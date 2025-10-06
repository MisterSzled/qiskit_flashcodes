# 13. Given the following code fragment, which one of the following describes the
# SamplerOptions parameter options.default_shots?
#
# from qiskit_ibm_runtime import Sampler
# sampler = Sampler(mode=backend)
# sampler.options.default_shots = ...
#
# a. The sum of the number of measurements in each qubit
# b. The number of randomizations we apply to the circuit
# c. The number of times that we run the circuit
# d. The number of sequences in dynamical decoupling

from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2

# Simple single-qubit circuit
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

# Create a local sampler (Aer-based)
sampler = SamplerV2()

# Try different default_shots settings
for shots in [10, 100, 1000]:
        sampler.options.default_shots = shots
        result = sampler.run([qc]).result()  # circuits must be passed in a list
        meas = result[0].data.meas.get_counts()  # access sampled counts
        print(f"\nDefault shots = {shots}")
        print(f"Measured counts: {meas}")

"""
SUMMARY:
- 'options.default_shots' controls how many times the circuit is executed (sampled).
- More shots → probabilities converge to ideal theoretical values.
- Correct answer: (c) The number of times that we run the circuit.
"""
