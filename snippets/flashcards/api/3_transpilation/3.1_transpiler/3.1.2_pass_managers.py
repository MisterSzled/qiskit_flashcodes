# ---------------------------------------------------------------
"""
# Qiskit 2.x Mock Exam — Preset Pass Managers
# One question per subsection, formatted for runnable code demos.
"""

# ---------------------------------------------------------------
"""
# Question 1 — Preset Pass Managers Overview
What is the primary purpose of the function `generate_preset_pass_manager()` in Qiskit?

a. It generates random circuit optimizations at runtime.  
b. It constructs predefined (preset) transpilation pipelines as instances of `StagedPassManager`.  
c. It executes the transpilation process automatically without user configuration.  
d. It provides stochastic gates for circuit execution.
"""

from qiskit.transpiler import generate_preset_pass_manager
from qiskit.providers.fake_provider import GenericBackendV2

backend = GenericBackendV2(num_qubits=3)
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
print(type(pm).__name__)  # Should print: StagedPassManager

# ---------------------------------------------------------------
"""
# Question 2 — Transpiler Stages
Which of the following correctly lists the *execution order* of the six possible stages in a preset pass manager?

a. layout → init → optimization → routing → translation → scheduling  
b. init → layout → routing → translation → optimization → scheduling  
c. translation → optimization → init → layout → routing → scheduling  
d. init → routing → layout → translation → optimization → scheduling
"""

stages = ["init", "layout", "routing", "translation", "optimization", "scheduling"]
print(stages)

# ---------------------------------------------------------------
"""
# Question 3 — Optimization Levels
In the preset transpiler, what is the default optimization level and what does it represent?

a. 0 — No optimization; only minimal routing  
b. 2 — Balanced trade-off between optimization time and performance  
c. 1 — Fastest optimization for trivial layouts  
d. 3 — Full exhaustive optimization with guaranteed best results
"""

from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

backend = FakeManilaV2()
pm_default = generate_preset_pass_manager(optimization_level=2, backend=backend)
print("Q3 demo optimization level:", pm_default)

# ---------------------------------------------------------------
"""
# Question 4 — Reproducibility and Seeds
Why would you use the `seed_transpiler` argument when generating a preset pass manager?

a. To enable stochastic routing passes to run in parallel.  
b. To ensure reproducibility in stochastic and heuristic-based passes.  
c. To improve optimization speed by caching random seeds.  
d. To disable deterministic analysis of the DAGCircuit.
"""

pm_seeded = generate_preset_pass_manager(backend=backend, optimization_level=1, seed_transpiler=123)
print(pm_seeded)

# ---------------------------------------------------------------
"""
# Question 5 — Choosing Stage Implementations
Given the following code, which routing and layout methods are explicitly chosen?

from qiskit.transpiler import generate_preset_pass_manager
from qiskit.providers.fake_provider import GenericBackendV2

backend = GenericBackendV2(num_qubits=5)
pm = generate_preset_pass_manager(
        optimization_level=1,
        backend=backend,
        layout_method="trivial",
        routing_method="sabre",
)

a. Layout: default, Routing: lookahead  
b. Layout: sabre, Routing: basic  
c. Layout: trivial, Routing: sabre  
d. Layout: dense, Routing: none
"""

print(pm)

# ---------------------------------------------------------------
"""
# Question 6 — Initialization Stage
At optimization level 2, which of the following transformations is *not* performed by the init stage?

a. Virtual permutation elision  
b. Removal of imperceivable tiny-angle rotations  
c. Translation of gates into the target ISA  
d. Cancellation of adjacent inverse gates
"""

# Init stage runs before translation, so translation into ISA (c) is not included.

# ---------------------------------------------------------------
"""
# Question 7 — Layout Stage
Which built-in layout method attempts to find a “perfect” mapping between virtual and physical qubits using subgraph isomorphism?

a. DenseLayout  
b. VF2Layout (used by default plugin)  
c. TrivialLayout  
d. SabreLayout
"""

# No code needed; theoretical question.

# ---------------------------------------------------------------
"""
# Question 8 — Routing Stage
Which routing plugin uses a greedy swap-insertion approach that may yield poor-quality output circuits?

a. lookahead  
b. basic  
c. sabre  
d. default
"""

# Conceptual; BasisSwap (basic) is greedy.

# ---------------------------------------------------------------
"""
# Question 9 — Translation Stage
Which translation plugin uses symbolic equivalences from the `EquivalenceLibrary` to express gates in the target basis?

a. synthesis  
b. default  
c. translator  
d. decomposition
"""

# Default uses BasisTranslator with symbolic rules.

# ---------------------------------------------------------------
"""
# Question 10 — Custom Stage Example
In the following example, what is achieved by setting `pass_manager.scheduling = scheduling_pm`?

from qiskit.transpiler import PassManager, generate_preset_pass_manager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, PadDynamicalDecoupling
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.circuit import library as lib

backend = GenericBackendV2(num_qubits=5)
dd_sequence = [lib.XGate(), lib.XGate()]
scheduling_pm = PassManager(
        [
                ALAPScheduleAnalysis(target=backend.target),
                PadDynamicalDecoupling(target=backend.target, dd_sequence=dd_sequence),
        ]
)
pm = generate_preset_pass_manager(optimization_level=0)
pm.scheduling = scheduling_pm

a. It disables scheduling for all subsequent runs.  
b. It replaces the default scheduling stage with a custom pass manager.  
c. It appends scheduling before routing.  
d. It randomizes delay insertion using a seed.
"""
from qiskit.transpiler import PassManager, generate_preset_pass_manager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, PadDynamicalDecoupling
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.circuit import library as lib

dd_sequence = [lib.XGate(), lib.XGate()]
scheduling_pm = PassManager([
        ALAPScheduleAnalysis(target=backend.target),
        PadDynamicalDecoupling(target=backend.target, dd_sequence=dd_sequence),
])

pm = generate_preset_pass_manager(optimization_level=0)
pm.scheduling = scheduling_pm

print("Q10 demo custom scheduling is PassManager:", isinstance(pm.scheduling, PassManager))

