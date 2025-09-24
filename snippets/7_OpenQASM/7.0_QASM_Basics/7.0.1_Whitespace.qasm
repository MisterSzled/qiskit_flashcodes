// Whitespace (spaces, tabs, newlines) is ignored in OpenQASM.
// Both compact and spread-out formatting are valid.

OPENQASM 2.0;
include "qelib1.inc";

qreg q[2]; h q[0];       // Compact but valid
qreg p[2];               
      h p[0];            // Spread out, also valid

// --- Summary ---
// Demonstrates:
// 1. OpenQASM ignores whitespace.
// 2. Same operations may be written compact or spaced out.
// 3. Formatting affects readability, not execution.