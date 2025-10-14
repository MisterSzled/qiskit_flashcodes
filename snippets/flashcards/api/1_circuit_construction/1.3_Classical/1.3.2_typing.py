"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Typing (qiskit.circuit.classical.types)
"""

# ---------------------------------------------------------------
"""
# Question 1
Which statement best describes the `Type` base class in Qiskit 2.x?

a. Type can be subclassed by users to define custom classical types.  
b. Type is the abstract root of the classical type hierarchy and cannot be instantiated directly.  
c. Type instances are mutable objects that should always be copied.  
d. Type automatically casts between Float and Uint types.  
"""

from qiskit.circuit.classical import types

try:
    _ = types.Type()  # should not be directly instantiated
except TypeError as e:
    print("Cannot instantiate Type directly:", type(e))

bool_t = types.Bool()
print("Created Bool type:", bool_t)

# ---------------------------------------------------------------
"""
# Question 2
Which of the following correctly matches Qiskit's built-in classical types to their use?

a. Bool → classical bit values; Uint → unsigned integers; Float → real numbers; Duration → time intervals.  
b. Bool → qubit states; Uint → floating point numbers; Float → register lengths; Duration → logical operations.  
c. Bool → quantum boolean gates; Uint → ancilla qubits; Float → rotation gates; Duration → resets.  
d. Bool → floating point type; Uint → integer literals; Float → qubit counts; Duration → booleans.  
"""

from qiskit.circuit.classical import types

print("Bool:", types.Bool())
print("Uint(8):", types.Uint(8))
print("Float:", types.Float())
print("Duration:", types.Duration())

# ---------------------------------------------------------------
"""
# Question 3
What does the `order()` function in `qiskit.circuit.classical.types` return?

a. A boolean indicating if two types are equal.  
b. An Ordering enumeration describing their subtyping relationship.  
c. The larger of the two types directly.  
d. The numeric bit width difference between the two types.  
"""

from qiskit.circuit.classical import types

result = types.order(types.Uint(8), types.Uint(16))
print("Ordering result between Uint(8) and Uint(16):", result)

# ---------------------------------------------------------------
"""
# Question 4
Which of the following statements about the `Ordering` enumeration is correct?

a. It only defines LESS and GREATER relationships.  
b. It represents partial order relations, including cases with no relation (Ordering.NONE).  
c. It performs automatic type coercion during comparison.  
d. It represents total order among all types.  
"""

from qiskit.circuit.classical.types import Ordering

print("Possible order values:", list(Ordering))
print("NONE represents unrelated types:", Ordering.NONE)

# ---------------------------------------------------------------
"""
# Question 5
What does `is_subtype(left, right, strict=False)` return?

a. True if left ≤ right according to the partial type ordering.  
b. True if left ≥ right according to the partial ordering.  
c. True only if the two types are identical.  
d. True if left and right share the same bit width.  
"""

from qiskit.circuit.classical import types

print("Is Uint(8) a subtype of Uint(16)?", types.is_subtype(types.Uint(8), types.Uint(16)))
print("Is Bool a strict subtype of Bool?", types.is_subtype(types.Bool(), types.Bool(), strict=True))

# ---------------------------------------------------------------
"""
# Question 6
Which function checks if a type is a supertype of another according to the Qiskit type ordering?

a. is_subtype()  
b. is_supertype()  
c. greater()  
d. cast_kind()  
"""

from qiskit.circuit.classical import types

print("Is Uint(16) a supertype of Uint(8)?", types.is_supertype(types.Uint(16), types.Uint(8)))

# ---------------------------------------------------------------
"""
# Question 7
What is the behavior of `greater(left, right)` in Qiskit 2.x?

a. Returns whichever type has the lower bit width.  
b. Returns the greater of two ordered types, or raises TypeError if unrelated.  
c. Returns a merged type representing both inputs.  
d. Always returns a Uint regardless of input.  
"""

from qiskit.circuit.classical import types

print("Greater of Uint(8) and Uint(16):", types.greater(types.Uint(8), types.Uint(16)))

# ---------------------------------------------------------------
"""
# Question 8
What does the `cast_kind(from_, to_)` function determine?

a. The type name of a variable before and after casting.  
b. The type of cast required between two classical types.  
c. Whether casting will raise a runtime exception.  
d. The numeric result of the cast operation.  
"""

from qiskit.circuit.classical import types

print("Bool → Bool:", types.cast_kind(types.Bool(), types.Bool()))
print("Uint(8) → Bool:", types.cast_kind(types.Uint(8), types.Bool()))
print("Bool → Uint(8):", types.cast_kind(types.Bool(), types.Uint(8)))
print("Uint(16) → Uint(8):", types.cast_kind(types.Uint(16), types.Uint(8)))

# ---------------------------------------------------------------
"""
# Question 9
Which statement about the CastKind enumeration is TRUE?

a. CastKind enumerates possible casting kinds such as EQUAL, IMPLICIT, LOSSLESS, and DANGEROUS.  
b. CastKind values are numeric codes returned by is_subtype().  
c. CastKind is deprecated in Qiskit 2.x.  
d. CastKind only supports type equality comparison.  
"""

from qiskit.circuit.classical.types import CastKind

print("Available cast kinds:", list(CastKind))

# ---------------------------------------------------------------
"""
Answer Key Summary
------------------
1. b  
2. a  
3. b  
4. b  
5. a  
6. b  
7. b  
8. b  
9. a  
"""
