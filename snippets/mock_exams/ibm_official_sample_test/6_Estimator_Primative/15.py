"""
Question 15 (compact demo)

Which one of the following describes the expected behavior of the number of
shots if the value for the parameter precision were changed from 0.015625 to 0.03125?

a. It increases the number of shots quadratically
b. It increases the number of shots exponentially
c. It has no effect on the number of shots
d. It decreases the number of shots
"""

# given precisions
p1 = 0.015625
p2 = 0.03125

# shots scale approximately as 1/precision^2
ratio = (p1 / p2) ** 2  # this equals shots2 / shots1

print(f"Precision1 = {p1}")
print(f"Precision2 = {p2}")
print()
print("Scaling rule: shots ∝ 1 / precision^2")
print(f"Therefore shots2 / shots1 = (p1 / p2)^2 = {ratio:.6f}")

# example: if we used 10,000 shots originally, how many shots now?
shots1 = 10_000
shots2 = int(round(shots1 * ratio))
print(f"\nExample: if shots1 = {shots1}, then shots2 ≈ {shots2}")

# interpret the numeric result
percent = ratio * 100.0
if ratio < 1.0:
        print(f"\nInterpretation: the number of shots DECREASES to {percent:.1f}% of the original (a reduction by factor {1/ratio:.1f}).")
elif ratio > 1.0:
        print(f"\nInterpretation: the number of shots INCREASES by factor {ratio:.2f}.")
else:
        print("\nInterpretation: the number of shots is unchanged.")
