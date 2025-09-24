// Identifiers are names for registers and variables.
// Rules:
// - Start with lowercase letter
// - Can include alphanumeric + underscores
// - Cannot use reserved keywords
// - Case-sensitive (q_a != q_A)

OPENQASM 2.0;
include "qelib1.inc";

qreg q0[2];
qreg q_a[2];
qreg q_A[2];   // Different from q_a

// Invalid (would cause compiler error): Q0, _q, 0_q

// --- Summary ---
// Demonstrates:
// 1. Identifier naming rules in OpenQASM.
// 2. Case sensitivity of identifiers.
// 3. Examples of valid and invalid identifiers.
