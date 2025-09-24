// Physical qubits use `$N` syntax
// They directly reference hardware qubits

CX $0, $1;          // Apply CNOT between hardware qubits 0 and 1

// Custom calibration (defcal) must use physical qubits
defcal h $0 { ... } // Define hardware-level instruction for H

// --- Summary ---
// Demonstrates:
// 1. Physical qubit syntax `$N`.
// 2. Difference between logical (virtual) and physical qubits.
// 3. That defcal applies only to physical qubits.
