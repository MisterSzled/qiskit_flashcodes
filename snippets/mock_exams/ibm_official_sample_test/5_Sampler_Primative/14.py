# 14. Given the code snippet, which one of the following is a valid way to invoke the
# run method on an instance of SamplerV2?
#
# from qiskit_ibm_runtime import SamplerV2
# ...
# sampler = SamplerV2(...)
#
# a. sampler.run([isa_circuit])
# b. sampler.run(distribution, isa_circuit)
# c. sampler.run(isa_circuit, distribution='gauss')
# d. sampler.run([isa_circuit1, isa_circuit2], runs=1024)

from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2

# --- Setup ---
# Define simple test circuits
isa_circuit = QuantumCircuit(1)
isa_circuit.h(0)
isa_circuit.measure_all()

isa_circuit1 = QuantumCircuit(1)
isa_circuit1.x(0)
isa_circuit1.measure_all()

isa_circuit2 = QuantumCircuit(1)
isa_circuit2.h(0)
isa_circuit2.measure_all()

# Create Aer-based sampler
sampler = SamplerV2()
sampler.options.default_shots = 100

# --- Test each option safely ---
print("Testing possible invocations:\n")

options = {
        "a": lambda: sampler.run([isa_circuit]),
        "b": lambda: sampler.run("distribution", isa_circuit),
        "c": lambda: sampler.run(isa_circuit, distribution="gauss"),
        "d": lambda: sampler.run([isa_circuit1, isa_circuit2], runs=1024),
}

for label, func in options.items():
        print(f"Option {label}:")
        try:
                result = func().result()
                print(f"  ✅ Executed successfully — result type: {type(result)}")
        except Exception as e:
                print(f"  ❌ Failed with error: {e.__class__.__name__}: {e}")
        print()

"""
SUMMARY:
- Only one option corresponds to the correct and valid SamplerV2 API usage.
- The valid call format is to pass a *list of circuits* to `sampler.run()`.
- Other forms (extra args like 'distribution' or 'runs') cause errors.
- Correct answer: (a)
"""
