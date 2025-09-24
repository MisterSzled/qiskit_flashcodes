// OpenQASM 3 allows classical variables with explicit types
// Must be declared one at a time (no comma-separated)

int[32] a;         // 32-bit signed integer
float[32] b = 5.5; // 32-bit float, initialized
bit[3] c;          // Register of 3 bits
bool flag = true;  // Boolean

// Casting example
a = int[32](b);    // Cast float -> int

// --- Summary ---
// Demonstrates:
// 1. Classical variable declaration rules.
// 2. Initialization on declaration.
// 3. Type casting using typename() syntax.
