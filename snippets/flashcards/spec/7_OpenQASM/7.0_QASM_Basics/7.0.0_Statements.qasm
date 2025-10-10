// OpenQASM statements always end with a semicolon
// They can be placed on separate lines (recommended) or on one line

OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];    // quantum register with 2 qubits
creg c[2];    // classical register with 2 bits

h q[0];       // Apply Hadamard
x q[1];       // Apply Pauli-X
measure q[0] -> c[0];  // Store measurement in c[0]
measure q[1] -> c[1];  // Store measurement in c[1]

// --- Summary ---
// Demonstrates:
// 1. That every OpenQASM statement ends with `;`.
// 2. Statements can be stacked inline or written one per line.
// 3. Includes declaration, gate operations, and measurement.
