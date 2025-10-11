"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Singleton instructions (qiskit.circuit.singleton)
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
When a subclass of `SingletonGate` or `SingletonInstruction` is constructed with its
default arguments, what is the expected behavior?

a. It creates a new, mutable instance each time.  
b. It returns a shared, immutable singleton instance.  
c. It constructs a proxy object that lazily initializes the gate.  
d. It raises a TypeError because defaults are not allowed.  

# Minimal runnable example demonstrating default-argument singleton reuse:
"""
from qiskit.circuit.singleton import SingletonInstruction

class MyInstruction(SingletonInstruction):
        def __init__(self, label=None):
                super().__init__("my_instruction", 1, 0, params=[], label=label)

print("Q1 demo:", MyInstruction() is MyInstruction())
print("Q1 demo:", MyInstruction() is MyInstruction())

# ---------------------------------------------------------------
"""
# Question 2
If a singleton-based instruction includes a `label` argument and an instance is created
with a **non-default label**, what happens?

a. The singleton is reused, and its label is changed.  
b. A new, mutable instance is created.  
c. The constructor ignores the label and returns the default singleton.  
d. A ValueError is raised because singleton labels must be None.  

# Minimal runnable example showing label-based mutability:
"""
from qiskit.circuit.singleton import SingletonInstruction

class LabeledInstruction(SingletonInstruction):
        def __init__(self, label=None):
                super().__init__("labeled_instruction", 1, 0, params=[], label=label)

print("Q2 default same object:", LabeledInstruction() is LabeledInstruction())
print("Q2 labeled creates new instance:", LabeledInstruction(label='A') is LabeledInstruction())
print("Q2 labeled instance mutable:", LabeledInstruction(label='A').mutable)

# ---------------------------------------------------------------
"""
# Question 3
Which statement is correct about checking types of singleton gate instances?

a. Use `type(obj) == MyInstruction` because singleton subclasses share exact type.  
b. Use `isinstance(obj, MyInstruction)` since singleton types are synthetic subclasses.  
c. Compare `obj.name` to the class name string for reliability.  
d. Singleton instances always have `type(obj) is MyInstruction`.  

# Minimal runnable example demonstrating type vs isinstance:
"""
from qiskit.circuit.singleton import SingletonInstruction

class ExampleInst(SingletonInstruction):
        def __init__(self, label=None):
                super().__init__("example", 1, 0, params=[], label=label)

obj = ExampleInst()
print("Q3 type equality:", type(obj) == ExampleInst)
print("Q3 isinstance:", isinstance(obj, ExampleInst))

# ---------------------------------------------------------------
"""
# Question 4
When defining a subclass of `SingletonInstruction` that lacks default constructor arguments,
how can you ensure that no default singleton is automatically created?

a. Set `create_default_singleton=False` in the class definition.  
b. Define a `_disable_singleton()` method in the class.  
c. Use `super().__init__(None)` to suppress singleton creation.  
d. Use `@abstractmethod` on the `__init__` method.  

# Minimal runnable example disabling automatic singleton creation:
"""
from qiskit.circuit.singleton import SingletonInstruction

class NotASingleton(SingletonInstruction):
        _singleton_create_default = False

        def __init__(self):
                super().__init__("mutable_instruction", 1, 0, params=[], label=None)

# Demonstration
a = NotASingleton()
b = NotASingleton()
print("Q4 no default singleton:", a is b)

# ---------------------------------------------------------------
"""
# Question 5
What is the role of `_singleton_lookup_key()` and `additional_singletons` when defining
a singleton-based gate class?

a. They are deprecated and unused in Qiskit 2.x.  
b. They define constructor argument combinations that should return shared singleton instances.  
c. They ensure only one mutable instance exists at runtime.  
d. They specify equality and hashing for `Instruction` comparison.  

# Minimal runnable example demonstrating additional_singletons behavior:
"""
from qiskit.circuit.singleton import SingletonGate

class MySingleton(SingletonGate, additional_singletons=[((2,), {"label": "two"})]):
        def __init__(self, n=1, label=None):
                super().__init__("my_gate", n, [], label=label)

        @staticmethod
        def _singleton_lookup_key(n=1, params=[], label=None):
                return (n, label)

# Test default singleton
print("Q5 default same singleton:", MySingleton() is MySingleton(1, label=None))
# Test custom additional singleton
print("Q5 custom additional singleton:", MySingleton(2, "two") is MySingleton(n=2, label="two"))


# ---------------------------------------------------------------
"""
Answer Key Summary
Q1: b  
Q2: b  
Q3: b  
Q4: a  
Q5: b  
"""
