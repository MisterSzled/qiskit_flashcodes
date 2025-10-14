# ===============================================================
# QISKIT 2.x MOCK EXAM — EXPERIMENT RESULTS
# ===============================================================

# ---------------------------------------------------------------
"""
# Question 1 — Result class purpose
What does the `Result` class in Qiskit represent?

a. The complete data model returned after a backend job finishes.  
b. A simulator configuration for result formatting.  
c. A transpiler pass for classical register merging.  
d. The live execution handle for runtime primitives.  
"""
# minimal runnable demo
from qiskit.result import Result
res = Result(backend_name="test_backend", backend_version="2.0", results=[])
print("Result backend:", res.backend_name)

# ---------------------------------------------------------------
"""
# Question 2 — ResultError
What is the `ResultError` class used for?

a. To represent errors detected in the output of a job result.  
b. To raise syntax errors during circuit transpilation.  
c. To represent backend connection errors.  
d. To handle provider authentication issues.  
"""
# minimal runnable demo
from qiskit.result import ResultError
try:
        raise ResultError({"message": "Example output parsing failure", "status":  403, "code": "BORKED"})
except ResultError as e:
        print("Caught:", e)

# ---------------------------------------------------------------
"""
# Question 3 — Counts class role
Which of the following best describes the `Counts` class?

a. It stores frequency data for bitstring measurement results.  
b. It compiles shots into transpiler statistics.  
c. It maps circuit DAG nodes to measurement memory.  
d. It defines the configuration of the backend.  
"""
# minimal runnable demo
from qiskit.result import Counts
counts = Counts({"00": 400, "11": 600})
print("Total shots:", sum(counts.values()))

# ---------------------------------------------------------------
"""
# Question 4 — Accessing counts metadata
What optional information can the `Counts` object store besides counts data?

a. Measurement time and classical register sizes.  
b. Provider authentication keys.  
c. Job IDs and transpiler passes.  
d. Backend firmware versions.  
"""
# minimal runnable demo
counts = Counts({"0": 300, "1": 700}, time_taken=0.23, creg_sizes=[("c", 1)])
print("Metadata:", counts.time_taken, counts.creg_sizes)

# ---------------------------------------------------------------
"""
# Question 5 — Marginalization basics
What does the function `marginal_counts()` perform?

a. Reduces count data to selected bit indices of interest.  
b. Normalizes counts by total shots.  
c. Converts counts into statevectors.  
d. Merges multiple job results into one.  
"""
# minimal runnable demo
from qiskit.result import marginal_counts
sample_counts = {"00": 200, "01": 300, "10": 500}
marg = marginal_counts(sample_counts, indices=[1])
print("Marginalized counts:", marg)

# ---------------------------------------------------------------
"""
# Question 6 — Marginalization inplace behavior
What happens when `inplace=True` is set in `marginal_counts()`?

a. The input `Result` object is modified directly.  
b. A deep copy of the Result is returned.  
c. Marginalization is skipped.  
d. Only the memory field is removed.  
"""
# minimal runnable demo
marg_inplace = marginal_counts(sample_counts, indices=[0], inplace=False)
print("Inplace=False result:", marg_inplace)

# ---------------------------------------------------------------
"""
# Question 7 — Marginalization memory handling
What is the role of the `marginalize_memory` parameter in `marginal_counts()`?

a. It determines whether the memory field of the result is also reduced.  
b. It enables parallel memory allocation during sampling.  
c. It merges memory strings into a single histogram.  
d. It applies bitstring compression for memory data.  
"""
# minimal runnable demo
print("Marginalize memory default:", marginal_counts(sample_counts, [0]))

# ---------------------------------------------------------------
"""
# Question 8 — marginal_distribution() difference
How does `marginal_distribution()` differ from `marginal_counts()`?

a. It preserves the ordering of the specified bit indices.  
b. It converts counts to probabilities automatically.  
c. It modifies the Result object in-place by default.  
d. It supports only hexadecimal formatted keys.  
"""
# minimal runnable demo
from qiskit.result import marginal_distribution
dist = marginal_distribution(sample_counts, indices=[1, 0])
print("Marginal distribution keys:", list(dist.keys()))

# ---------------------------------------------------------------
"""
# Question 9 — marginal_distribution() format_marginal
What does `format_marginal=True` do in `marginal_distribution()`?

a. Inserts placeholders for bits not included in the marginal.  
b. Automatically normalizes counts.  
c. Renames classical registers.  
d. Applies log-scaling to frequencies.  
"""
# minimal runnable demo
dist_fmt = marginal_distribution(sample_counts, indices=[0], format_marginal=True)
print("Formatted marginal:", dist_fmt)

# ---------------------------------------------------------------
"""
# Question 10 — marginal_memory() purpose
What is the goal of the function `marginal_memory()`?

a. To reduce lists of shot memory bitstrings to selected bit positions.  
b. To compute fidelity estimates from shot memory.  
c. To convert memory arrays into counts objects.  
d. To randomize sampling order in the memory buffer.  
"""
# minimal runnable demo
from qiskit.result import marginal_memory
memory = ["00", "01", "10", "11"]
mem_out = marginal_memory(memory, indices=[1])
print("Marginalized memory:", mem_out)

# ---------------------------------------------------------------
"""
# Question 11 — marginal_memory() return options
What happens when `int_return=True` or `hex_return=True` is passed to `marginal_memory()`?

a. The output format of each memory entry changes to integers or hex strings.  
b. The number of shots doubles.  
c. Memory indices are randomized.  
d. The function becomes single-threaded.  
"""
# minimal runnable demo
mem_int = marginal_memory(["00", "01", "11"], indices=[1], int_return=True)
print("Integer output:", mem_int)

# ---------------------------------------------------------------
"""
# Question 12 — marginal_memory() threading behavior
When does `marginal_memory()` use multiple CPU threads?

a. When the number of memory entries exceeds `parallel_threshold`.  
b. When int_return is True.  
c. Only when avg_data is True.  
d. Only when run from a Provider context.  
"""
# minimal runnable demo
mem_threads = marginal_memory(["00", "01"], indices=[0], parallel_threshold=1)
print("Parallel marginal run:", mem_threads)
