"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Classical Expressions (qiskit.circuit.classical.expr)
"""

# ---------------------------------------------------------------
"""
# Question 1
Which statement about the Expr base class in Qiskit 2.x is TRUE?

a. Expr can be directly instantiated for user-defined nodes.  
b. Expr represents the abstract base class of all classical expression nodes and cannot be instantiated.  
c. Expr automatically converts Python integers into Value nodes.  
d. Expr subclasses must all define a 'name' attribute.  
"""

from qiskit.circuit.classical.expr import Expr, Value

try:
        _ = Expr()
except TypeError as e:
        print("Cannot instantiate Expr:", type(e))

# ---------------------------------------------------------------
"""
# Question 2
Which statement about Var nodes in Qiskit 2.x is correct?

a. Var.new() creates a variable bound to a name and a type.  
b. Var objects always reference qubits, not classical data.  
c. Var instances are immutable and cannot store type information.  
d. Var must be created using Value() instead of Var().  
"""

from qiskit.circuit.classical.expr import Var
from qiskit.circuit.classical.types import Bool

v = Var.new("flag", Bool())
print("Variable name:", v.name)
print("Variable type:", v.type)

# ---------------------------------------------------------------
"""
# Question 3
Which description best fits the Value class in Qiskit 2.x?

a. Value nodes represent mutable references to registers.  
b. Value wraps constant literals or evaluated expressions.  
c. Value cannot represent integers or booleans.  
d. Value nodes are used only for measurement outcomes.  
"""

from qiskit.circuit.classical.expr import Value
from qiskit.circuit.classical.types import Uint

v = Value(7, Uint(7))
print("Value node constant:", v.const, "Value type:", v.type)

# ---------------------------------------------------------------
"""
# Question 4
Which statement about Unary and Binary operator nodes is TRUE?

a. Unary nodes have no operand.  
b. Binary nodes always represent arithmetic operations only.  
c. Binary logical operators (e.g. LOGIC_AND) coerce operands to Boolean and return Boolean.  
d. Unary operators always return integers regardless of input.  
"""

from qiskit.circuit.classical import expr

logic_expr = expr.logic_and(1, 0)
print("Expression type:", logic_expr.type)

# ---------------------------------------------------------------
"""
# Question 5
What is the purpose of helper functions like expr.lift() and expr.cast()?

a. lift() wraps Python scalars or classical data into expression nodes, and cast() changes node type when necessary.  
b. lift() converts all expressions to integers, and cast() deletes invalid nodes.  
c. lift() replaces Expr with Var, while cast() merges two Expr trees.  
d. lift() and cast() are deprecated in Qiskit 2.x.  
"""

from qiskit.circuit.classical import expr, types

lifted = expr.lift(5)
casted = expr.cast(lifted, types.Uint(8))
print("Lifted type:", lifted.type, "Casted type:", casted.type)

# ---------------------------------------------------------------
"""
# Question 6
Which statement about visitors and iteration utilities in Qiskit 2.x is correct?

a. iter_vars() yields all Var and Stretch nodes found in an expression tree.  
b. iter_identifiers() returns only Value nodes.  
c. Visitors cannot traverse Index nodes.  
d. iter_vars() only yields top-level nodes.  
"""

from qiskit.circuit import ClassicalRegister
from qiskit.circuit.classical import expr

cr = ClassicalRegister(2, "c")
e = expr.bit_and(cr[0], cr[1])
print("Vars found:", [v.name for v in expr.iter_vars(e)])

# ---------------------------------------------------------------
"""
# Question 7
Which statement about expression equality in Qiskit 2.x is TRUE?

a. Expressions can only be compared by Python object identity.  
b. structurally_equivalent() compares expressions ignoring differences in bound variables if given key functions.  
c. is_lvalue() always returns True for Value nodes.  
d. Two identical Expr trees are never equal.  
"""

from qiskit.circuit.classical import expr
from qiskit.circuit import ClassicalRegister

cr1 = ClassicalRegister(2, "a")
cr2 = ClassicalRegister(2, "b")

e1 = expr.logic_and(expr.logic_not(cr1[0]), cr1[1])
e2 = expr.logic_and(expr.logic_not(cr2[0]), cr2[1])

print("Python == :", e1 == e2)
print("Structural equivalence:", expr.structurally_equivalent(e1, e2))

# ---------------------------------------------------------------
"""
Answer Key Summary
------------------
1. b  
2. a  
3. b  
4. c  
5. a  
6. a  
7. b  
"""