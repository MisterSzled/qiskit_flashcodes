"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Random Circuits (qiskit.circuit.random)
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
In qiskit.circuit.random.random_circuit(...), what does the parameter `measure=True`
do to the generated circuit?

a. Inserts measurements at random positions throughout the circuit.  
b. Measures all qubits at the end of the circuit.  
c. Converts the circuit into a sampler backend object.  
d. Ensures the circuit has no measurements (useful for unitary simulation).  

# Minimal runnable example demonstrating the `measure` behavior:
# circ = random_circuit(3, 3, measure=True)
# circ.count_ops() should include 'measure'.
"""
from qiskit.circuit.random import random_circuit

circ = random_circuit(3, 3, measure=True, seed=1)
print("Contains 'measure' in op counts:", "measure" in circ.count_ops())

# ---------------------------------------------------------------
"""

# Question 2
What is the effect of supplying the same integer `seed` to random_circuit(...)?

a. It ensures identical circuits are produced for identical function arguments and seed.  
b. It guarantees circuits with identical depth but different gates.  
c. It randomly chooses a different generator each call (seed ignored).  
d. It only affects classical reset/conditional placement, not gate selection.  

# Minimal runnable example showing determinism with a seed:
# circ1 = random_circuit(4, 4, seed=42)
# circ2 = random_circuit(4, 4, seed=42)
# circ1.qasm() == circ2.qasm() should be True.

"""
from qiskit.circuit.random import random_circuit
from qiskit.qasm3 import dumps

# Generate two circuits with the same seed
c1 = random_circuit(4, 4, seed=42)
c2 = random_circuit(4, 4, seed=42)

# Export to OpenQASM 3 strings for deterministic comparison
qasm_equal = dumps(c1) == dumps(c2)
print("Same seed -> identical QASM:", qasm_equal)

# ---------------------------------------------------------------
"""
# Question 3
What does the `num_operand_distribution` argument to random_circuit(...) specify?

a. A strict, exact count of how many 1Q, 2Q, ... gates will appear.  
b. A preferred ratio of 1Q/2Q/... gates (approximate; deviations depend on circuit size).  
c. A mapping of gate names to their exact probabilities; if invalid, ignored.  
d. The maximum allowed operands per gate (overrides max_operands).  
"""
from qiskit.circuit.random import random_circuit
from collections import Counter

# Must sum to 1.0 (e.g. 50% 1-qubit gates, 50% 2-qubit gates)
circ = random_circuit(
        8,
        6,
        num_operand_distribution={1: 0.5, 2: 0.5},
        seed=7
)

counts = Counter(len(instr.qubits) for instr in circ.data)
print("Observed operand-size counts (len(qubits) -> count):", dict(counts))


# ---------------------------------------------------------------
"""
# Question 4
Which interaction_graph input formats are accepted by random_circuit_from_graph(...),
according to the documentation?

a. Only rustworkx PyGraph / PyDiGraph objects.  
b. Only adjacency matrices (NumPy arrays).  
c. A rustworkx graph OR a Python list of (u, v, weight) tuples describing edges.  
d. Only NetworkX Graph objects.  

# Minimal runnable example using a list-of-tuples interaction graph:
# qc = random_circuit_from_graph([(0,1,0.5),(1,2,0.5)], min_2q_gate_per_edge=1, seed=3)
"""
from qiskit.circuit.random import random_circuit_from_graph

igraph = [(0, 1, 0.5), (1, 2, 0.5)]
qc_from_graph = random_circuit_from_graph(igraph, min_2q_gate_per_edge=1, max_operands=2, seed=3)
print("random_circuit_from_graph produced circuit with qubits:", qc_from_graph.num_qubits)

# ---------------------------------------------------------------
"""
# Question 5
What does random_clifford_circuit(..., gates=...) allow you to specify?

a. A list of Clifford gate names to sample from, or "all" to use the full set.  
b. Only a boolean: True to use Clifford gates, False otherwise.  
c. The exact deterministic sequence of Clifford gates to place.  
d. A PyZX ZX-diagram used to generate the circuit.  

# Minimal runnable example specifying a custom small set of Clifford gate names:
# circ = random_clifford_circuit(num_qubits=2, num_gates=6, gates=['h','cx'], seed=5)
"""
from qiskit.circuit.random import random_clifford_circuit

circ_cliff = random_clifford_circuit(num_qubits=2, num_gates=6, gates=['h', 'cx'], seed=5)
print("Random Clifford circuit depth:", circ_cliff.depth())

# ---------------------------------------------------------------
"""
Answer Key Summary

1. b
2. a
3. b
4. c
5. a
"""
