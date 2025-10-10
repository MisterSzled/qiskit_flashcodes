"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Circuit annotations (qiskit.circuit.annotation)
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
What is the correct behavior of `iter_namespaces("hello.world")` when resolving
annotation handlers in priority order?

a. ["hello.world", "hello", ""]  
b. ["", "hello", "hello.world"]  
c. ["hello", "hello.world"]  
d. ["hello.world", "hello.world.parent", ""]
"""

from qiskit.circuit.annotation import iter_namespaces

print(list(iter_namespaces("hello.world")))

# ---------------------------------------------------------------
"""
# Question 2
When defining a custom annotation subclass of `qiskit.circuit.annotation.Annotation`,
what is the required field to enable correct dispatch behavior?

a. `handler_name` must be defined at class scope.  
b. `namespace` must be defined (either per-instance or per-class).  
c. `prefix` must be dynamically set during circuit construction.  
d. No field is required; dispatch is automatic.  
"""

from qiskit.circuit.annotation import Annotation

class MyAnnotation(Annotation):
        namespace = "my_namespace"

a = MyAnnotation()
print(a.namespace)

# ---------------------------------------------------------------
"""
# Question 3
According to the QPY serialization process, which order of method calls occurs
for a single circuits annotations?

a. Many `dump_annotation()` calls (sharing a namespace prefix), then one `dump_state()` call.  
b. A single `dump_state()` call followed by multiple `load_annotation()` calls.  
c. Many `load_annotation()` calls followed by a single `dump_state()` call.  
d. One `dump_annotation()` call per entire circuit, then many `dump_state()` calls.  
"""

from qiskit.circuit.annotation import QPYSerializer

print("Serializer interface loaded:", QPYSerializer.__name__)

# ---------------------------------------------------------------
"""
# Question 4
Which of the following correctly describes an `OpenQASM3Serializer` subclass?

a. It may track mutable internal state across calls to `dump()` and `load()`.  
b. It must be stateless and return UTF-8-encoded single-line text.  
c. It must serialize annotations as binary data structures.  
d. It automatically deserializes annotations during transpilation.  
"""

import numpy as np
from qiskit.circuit.annotation import OpenQASM3Serializer, Annotation

class PerformsUnitary(Annotation):
        namespace = "unitary"
        def __init__(self, matrix):
                self.matrix = matrix

class Serializer(OpenQASM3Serializer):
        def dump(self, annotation):
                if annotation.namespace != "unitary":
                        return NotImplemented
                return "[]"
        def load(self, namespace, payload):
                if namespace != "unitary":
                        return NotImplemented
                return PerformsUnitary(np.array([]))

print("Dumped representation:", Serializer().dump(PerformsUnitary(np.eye(2))))

# ---------------------------------------------------------------
"""
# Question 5
When exporting a circuit with custom annotations to OpenQASM 3 using
`qiskit.qasm3.dumps`, and providing a handler for the `"unitary"` namespace,
what effect does this have?

a. The OpenQASM 3 output will contain `@unitary[...]` annotations above box blocks.  
b. The annotations are silently ignored unless serialized to QPY first.  
c. The handler must return binary pickles to be recognized.  
d. OpenQASM 3 does not support any custom annotations.  
"""

from qiskit import QuantumCircuit, qasm3

class UAnn(Annotation):
        namespace = "unitary"

class S(OpenQASM3Serializer):
        def dump(self, a):
                return "[]" if getattr(a, "namespace", "") == "unitary" else NotImplemented
        def load(self, ns, payload):
                return UAnn()

qc = QuantumCircuit(1)
with qc.box(annotations=[UAnn()]):
        qc.h(0)

dumped = qasm3.dumps(qc, annotation_handlers={"unitary": S()})
print(dumped)

# ---------------------------------------------------------------
"""
Answer Key Summary
Q1: a
Q2: b
Q3: a
Q4: b
Q5: a
"""
