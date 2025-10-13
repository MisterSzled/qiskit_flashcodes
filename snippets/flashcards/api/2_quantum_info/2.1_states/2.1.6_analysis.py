"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Analysis (qiskit.quantum_info.analysis)
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
What does `hellinger_distance(dist_p, dist_q)` compute between two count distributions?

a. The Euclidean distance between their normalized histograms.  
b. The total variation distance between probabilities.  
c. The Hellinger distance — a measure of dissimilarity between probability distributions.  
d. The trace distance of their corresponding density matrices.

# Minimal runnable example:
# dist_p = {'00': 0.4, '11': 0.6}
# dist_q = {'00': 0.5, '11': 0.5}
# print(hellinger_distance(dist_p, dist_q))
"""
from qiskit.quantum_info import hellinger_distance

dist_p = {"00": 0.4, "11": 0.6}
dist_q = {"00": 0.5, "11": 0.5}
print("Hellinger distance:", hellinger_distance(dist_p, dist_q))

# ---------------------------------------------------------------
"""
# Question 2
What is the range of values that the Hellinger distance can take?

a. [0, ∞)  
b. [−1, 1]  
c. [0, 1]  
d. [0, 2]

# Minimal runnable example:
# hd = hellinger_distance({'0': 1.0}, {'1': 1.0})
# print(hd)
"""
hd = hellinger_distance({"0": 1.0}, {"1": 1.0})
print("Distance upper bound check:", hd <= 1.0)

# ---------------------------------------------------------------
"""
# Question 3
If two distributions are identical, what will `hellinger_distance` return?

a. 1  
b. 0  
c. 0.5  
d. Undefined

# Minimal runnable example:
# hd_same = hellinger_distance({'0': 0.3, '1': 0.7}, {'0': 0.3, '1': 0.7})
# print(hd_same)
"""
hd_same = hellinger_distance({"0": 0.3, "1": 0.7}, {"0": 0.3, "1": 0.7})
print("Distance between identical distributions:", hd_same)

# ---------------------------------------------------------------
"""
# Question 4
What is the mathematical relationship between `hellinger_distance` and `hellinger_fidelity`?

a. Fidelity = 1 − distance  
b. Fidelity = (1 − H²)² where H is the Hellinger distance  
c. Fidelity = 1 / (1 + H²)  
d. They are unrelated measures

# Minimal runnable example:
# from qiskit.quantum_info import hellinger_fidelity
# print(hellinger_fidelity({'0': 1.0}, {'1': 1.0}))
"""
from qiskit.quantum_info import hellinger_fidelity

print("Fidelity for disjoint distributions:", hellinger_fidelity({"0": 1.0}, {"1": 1.0}))

# ---------------------------------------------------------------
"""
# Question 5
What does a Hellinger fidelity value of 1 indicate?

a. The two distributions are maximally different.  
b. The two distributions are identical.  
c. The two distributions are orthogonal.  
d. The fidelity is undefined.

# Minimal runnable example:
# f_same = hellinger_fidelity({'0': 0.2, '1': 0.8}, {'0': 0.2, '1': 0.8})
# print(f_same)
"""
f_same = hellinger_fidelity({"0": 0.2, "1": 0.8}, {"0": 0.2, "1": 0.8})
print("Fidelity between identical distributions:", f_same)

# ---------------------------------------------------------------
"""
# Question 6
How does `hellinger_fidelity` behave compared to the standard classical fidelity F(P,Q) = (∑√pᵢqᵢ)²?

a. It produces the same numerical value for normalized distributions.  
b. It always gives a smaller value.  
c. It is the reciprocal of classical fidelity.  
d. It can exceed 1 for non-normalized inputs.

# Minimal runnable example:
# f = hellinger_fidelity({'00': 0.5, '11': 0.5}, {'00': 0.4, '11': 0.6})
# print(f)
"""
f = hellinger_fidelity({"00": 0.5, "11": 0.5}, {"00": 0.4, "11": 0.6})
print("Fidelity value:", f)

# ---------------------------------------------------------------
"""
# Question 7
In the context of quantum experiments, what are typical inputs to `hellinger_fidelity`?

a. Two Qiskit circuits.  
b. Two dictionaries of measured bitstring counts.  
c. Two Statevector objects.  
d. Two QuantumRegister objects.

# Minimal runnable example:
# counts1 = {'00': 512, '11': 512}
# counts2 = {'00': 500, '11': 524}
# print(hellinger_fidelity(counts1, counts2))
"""
counts1 = {"00": 512, "11": 512}
counts2 = {"00": 500, "11": 524}
print("Fidelity from counts:", hellinger_fidelity(counts1, counts2))

# ---------------------------------------------------------------
"""
# Question 8
Which of the following statements about Hellinger metrics is **true**?

a. The Hellinger distance is a metric; the Hellinger fidelity is not.  
b. Both are metrics on the same space.  
c. Both can exceed 1 for unnormalized distributions.  
d. The fidelity equals the distance for all distributions.

# Minimal runnable example:
# hd = hellinger_distance({'0': 0.4, '1': 0.6}, {'0': 0.5, '1': 0.5})
# hf = hellinger_fidelity({'0': 0.4, '1': 0.6}, {'0': 0.5, '1': 0.5})
# print(hd, hf)
"""
hd = hellinger_distance({"0": 0.4, "1": 0.6}, {"0": 0.5, "1": 0.5})
hf = hellinger_fidelity({"0": 0.4, "1": 0.6}, {"0": 0.5, "1": 0.5})
print("Distance:", hd, "Fidelity:", hf)

# ---------------------------------------------------------------
"""
# Question 9
What does `hellinger_fidelity` return when comparing the results of two identical simulator runs?

a. 0.0  
b. 0.5  
c. 1.0  
d. Depends on the backend seed.

# Minimal runnable example:
# from qiskit import QuantumCircuit
# from qiskit.providers.basic_provider import BasicSimulator
# qc = QuantumCircuit(2, 2)
# qc.h(0)
# qc.cx(0, 1)
# qc.measure_all()
# sim = BasicSimulator()
# res1 = sim.run(qc).result()
# res2 = sim.run(qc).result()
# print(hellinger_fidelity(res1.get_counts(), res2.get_counts()))
"""
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sim = BasicSimulator()
res1 = sim.run(qc).result()
res2 = sim.run(qc).result()
print("Fidelity between identical simulator runs:", hellinger_fidelity(res1.get_counts(), res2.get_counts()))