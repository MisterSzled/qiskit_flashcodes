from qiskit.circuit.library import ZZFeatureMap

# Example feature vector
features = [0.2, 0.4, 0.8]

# Create ZZFeatureMap for angle encoding
feature_map = ZZFeatureMap(feature_dimension=len(features))

# Assign data features to circuit parameters
encoded = feature_map.assign_parameters(features)

print("Feature-encoded circuit with ZZFeatureMap:")
print(encoded)

"""
Summary:
- Demonstrates angle encoding using ZZFeatureMap.
- Steps:
        1. Import ZZFeatureMap.
        2. Define a 3-feature vector.
        3. Create feature map with dimension=3.
        4. Assign feature values to parameters.
        5. Print the encoded circuit.
"""
