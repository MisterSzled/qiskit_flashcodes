// Declaring qubits in OpenQASM 3
// `qubit` type is used (qreg is legacy)

qubit q0;             // Single qubit
qubit[3] qreg1;       // Register of 3 qubits

// Unicode names are valid
qubit γ;

// Indexing with constant
x qreg1[0];     // Apply X to first qubit
z qreg1[2];     // Apply Z to last qubit

// --- Summary ---
// Demonstrates:
// 1. Declaring qubits (single + register).
// 2. Unicode identifiers.
// 3. Applying gates to indexed qubits.
