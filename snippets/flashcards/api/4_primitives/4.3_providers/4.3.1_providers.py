# ---------------------------------------------------------------
"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Providers Interface — qiskit.providers
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1 — Provider Role
In Qiskit, what is a *Provider*?

a. A module for visualizing results.  
b. A factory class that supplies external quantum services like backends.  
c. A class used to define hardware calibration data.  
d. A low-level transpiler optimization component.
"""

from qiskit_ibm_runtime.fake_provider import FakeManilaV2

provider = FakeManilaV2()
print("Provider name:", type(provider).__name__)

# ---------------------------------------------------------------
"""
# Question 2 — Backend Relationship
What is the relationship between a Provider and a Backend?

a. A Provider contains multiple Backend objects that execute QuantumCircuits.  
b. A Backend provides Providers to manage multiple quantum circuits.  
c. Both are unrelated abstractions in Qiskit.  
d. A Backend defines the interface for classical simulation only.
"""
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

provider = FakeManilaV2()
backend_name = provider.backend_name
print("Q2 demo backend name:", backend_name)

# ---------------------------------------------------------------
"""
# Question 3 — Interface Versioning
Why are provider interfaces in Qiskit individually versioned?

a. To allow independent evolution of different interface types without global version bumps.  
b. To match hardware firmware versions.  
c. To ensure every provider uses the same interface version at all times.  
d. To control the random number generator seed.
"""

# Each abstract class (BackendV2, JobV1, etc.) has its own versioned interface.

# ---------------------------------------------------------------
"""
# Question 4 — Version Support Policy
According to Qiskit's support policy, how long is a provider interface version (e.g. BackendV2)
supported before potential deprecation?

a. At least 3 minor releases or 6 months, whichever is longer.  
b. Exactly 2 releases after introduction.  
c. Only until the next major release.  
d. Indefinitely, until manually deprecated by the provider.
"""

# The policy ensures providers have ample time to adapt before a breaking interface is removed.

# ---------------------------------------------------------------
"""
# Question 5 — Backend Abstract Classes
Which abstract class defines the base type for all backend implementations?

a. BackendV2  
b. BackendBase  
c. Backend  
d. QuantumBackend
"""

from qiskit.providers import Backend
print(isinstance(Backend, type))

# ---------------------------------------------------------------
"""
# Question 6 — Job Handling
Which of the following correctly describes `JobV1`?

a. A concrete class used to execute Python threads.  
b. A versioned abstract interface defining job handling between Qiskit and providers.  
c. A deprecated API used only in AerSimulator.  
d. A visualization helper for displaying job status.
"""

from qiskit.providers import JobV1
print(isinstance(JobV1, type))

# ---------------------------------------------------------------
"""
# Question 7 — Job Errors
Which exception is raised when a job fails due to a timeout?

a. QiskitBackendNotFoundError  
b. JobError  
c. JobTimeoutError  
d. TimeoutWarning
"""

from qiskit.providers import JobTimeoutError

try:
        raise JobTimeoutError("Job exceeded timeout limit.")
except JobTimeoutError as e:
        print("Caught:", e)

# ---------------------------------------------------------------
"""
# Question 8 — Backend Not Found
What does `QiskitBackendNotFoundError` indicate?

a. A backend cannot be located or retrieved by name.  
b. The backend failed during runtime execution.  
c. A provider returned an invalid backend configuration.  
d. A job was cancelled before completion.
"""

from qiskit.providers import QiskitBackendNotFoundError

try:
        raise QiskitBackendNotFoundError("No backend found with that name.")
except QiskitBackendNotFoundError as e:
        print("Error:", e)

# ---------------------------------------------------------------
"""
# Question 9 — Options Object
What is the purpose of the `Options` class in the provider interface?

a. To define configurable parameters for backends or jobs.  
b. To store measurement results from circuits.  
c. To handle serialization of quantum states.  
d. To register Qiskit extensions dynamically.
"""

from qiskit.providers import Options
opts = Options(shots=1024, optimization_level=2)
print("Options:", opts.__dict__)

# ---------------------------------------------------------------
"""
# Question 10 — Versioning Example
Suppose `BackendV2` was introduced in Qiskit 0.19.0, and versions 0.20.0, 0.21.0, and 0.22.0
were released in the next 3 months. When could Qiskit first deprecate `BackendV2`?

a. In version 0.20.0, immediately.  
b. In version 0.23.0, after at least 3 minor releases and 6 months.  
c. In version 0.21.0, once Aer updates.  
d. Never — backend interfaces are permanent.
"""

# As per Qiskit's deprecation schedule, deprecation can begin in 0.23.0 in this example.
