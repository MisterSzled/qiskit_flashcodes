# Qiskit v2.X Certification Study Flashcodes

This repository is a collection of **Qiskit code-snippet flashcards** designed to study for the **IBM Quantum Qiskit v2.X Certification Exam**.  
Each folder explores one topic from the official exam guide in a **minimal, runnable example**.

---

### ✨ Why this repo?

I created this project because I wanted a **complete set of learning material grounded in actual, concrete code examples** — not just documentation.  

Key goals:  
- Provide **self-contained snippets** that can run independently of the actual IBM Quantum hardware, making them really easy to revisit repeatedly.  
- Ensure that for every exam topic, there is a **direct, runnable example** that demonstrates the concept in practice.  
- Build a **comprehensive study resource** so that i know: "if I can read, understand, and run all of these flashcards, I can be confident I have the knowledge required to pass the certification."  

---

## 📚 Structure

- All snippets are organized under the **`snippets/`** directory.  
- The folder hierarchy mirrors the **exam guide topics**:
  - Each file is named as:  
    ```
    <section>.<subsection>.<example>_<Feature>.py
    ```
  - Example:  
    ```
    snippets/2_Visualization/2.2_States/2.2.4_Plot_State_City_and_PauliVec.py
    ```

---

## 🧩 Exam Guide Coverage

The flashcards are organized according to the exam guide:

- **Perform quantum operations**
  - Define Pauli operators
  - Apply quantum operations  
- **Visualize circuits, measurements, and states**
  - Circuits, measurements, quantum states  
- **Create quantum circuits**
  - Basic, dynamic, parameterized circuits  
  - Transpilation & optimization  
- **Run quantum circuits**
  - Execution modes, runtime, hardware execution  
- **Use primitives**
  - Sampler primitive  
  - Estimator primitive  
- **Retrieve & analyze results**
  - Save, retrieve, and monitor jobs  
- **Operate with OpenQASM**
  - QASM 2 & 3 syntax, semantics, interoperability  

---

## 🚀 Usage

You can use this repository in two ways:

1. **Browse Online**  
   - Review each flashcard directly in the GitHub repo.

2. **Run Locally**  
   - Clone the repository and set up the environment with [uv](https://docs.astral.sh/uv/):
     ```bash
     git clone https://github.com/<your-username>/<repo-name>.git
     cd <repo-name>
     uv sync
     ```
   - Run any snippet inside the project environment:
     ```bash
     uv run snippets/2_Visualization/2.2_States/2.2.4_Plot_State_City_and_PauliVec.py
     ```

   > `uv sync` installs all dependencies from `pyproject.toml` into a local `.venv`,  
   > and `uv run` ensures the snippet runs in that environment without manual activation.


---

### 🧑‍🎓 Suggested Study Method

My personal workflow when using these flashcards was:

1. **Read the code carefully**  
   - Try to understand each line, argument, and command.  

2. **Summarize the purpose**  
   - Form a mental summary of what the entire snippet is demonstrating.  

3. **Check against the summary block**  
   - Compare your own understanding with the provided explanation at the bottom of the file.  

4. **Run the code**  
   - Observe the print logging to confirm your reasoning matches the actual behavior.  

This approach reinforces both **conceptual understanding** and **practical execution**.  
