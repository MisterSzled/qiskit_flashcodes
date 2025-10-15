# ===============================================================
# QISKIT 2.x MOCK EXAM — DISTRIBUTIONS
# ===============================================================

# ---------------------------------------------------------------
"""
# Question 1 — ProbDistribution purpose
What is the purpose of the `ProbDistribution` class in Qiskit?

a. It represents normalized classical probability data as a dict-like object.  
b. It stores raw shot counts for backend execution.  
c. It generates random distributions for simulators.  
d. It defines a backend calibration mapping.  
"""
# minimal runnable demo
from qiskit.result import ProbDistribution
dist = ProbDistribution({'00': 0.5, '11': 0.5})
print("ProbDistribution:", dist)

# ---------------------------------------------------------------
"""
# Question 2 — QuasiDistribution meaning
What does the `QuasiDistribution` class represent?

a. A dict-like object that can contain negative probabilities.  
b. A noise-free perfect probability map.  
c. A histogram normalized to 1 always.  
d. A backend-specific measurement layout.  
"""
# minimal runnable demo
from qiskit.result import QuasiDistribution
qd = QuasiDistribution({'00': 0.6, '11': 0.4})
print("QuasiDistribution sum:", sum(qd.values()))

# ---------------------------------------------------------------
"""
# Question 3 — shots parameter
What does the optional `shots` parameter represent in ProbDistribution and QuasiDistribution?

a. The total number of measurement samples used to generate the distribution.  
b. The number of threads in the marginalization routine.  
c. The maximum number of Pauli observables supported.  
d. The quantum depth of the evaluated circuit.  
"""
# minimal runnable demo
pd = ProbDistribution({'0': 0.3, '1': 0.7}, shots=1000)
print("Shots recorded:", pd.shots)

# ---------------------------------------------------------------
"""
# Question 4 — sampled_expectation_value() usage
What does the `sampled_expectation_value()` function compute?

a. The expectation value of an observable from a sampled distribution.  
b. The marginal probability of selected indices.  
c. The variance of measurement counts.  
d. The fidelity between two distributions.  
"""
# minimal runnable demo
from qiskit.result import sampled_expectation_value
value = sampled_expectation_value({'0': 0.2, '1': 0.8}, oper='Z')
print("Expectation value:", value)

# ---------------------------------------------------------------
"""
# Question 5 — sampled_expectation_value() input types
Which of the following inputs are valid for the `dist` argument of `sampled_expectation_value()`?

a. Counts, QuasiDistribution, ProbDistribution, or a raw dict.  
b. Only backend job result objects.  
c. Only numpy arrays of floats.  
d. Only QASM circuit files.  
"""
# minimal runnable demo
val2 = sampled_expectation_value(ProbDistribution({'0': 1.0}), oper='I')
print("Expectation value (identity):", val2)
