# Flashcard: Execution mode recommendations
# Demonstrates best practices for choosing batch, session, or job execution modes
# Includes logging examples to show reasoning

# --- Step 1: Define workload characteristics ---
workload_size = 5          # number of jobs/circuits
inputs_ready = True        # True if all inputs available upfront
iterative_workload = False # True if workload requires iterative feedback
qpu_time_per_job = 0.5     # QPU time in minutes per job

# --- Step 2: Determine recommended execution mode ---
if iterative_workload:
        recommended_mode = "Session"
elif workload_size > 1 and inputs_ready:
        recommended_mode = "Batch"
else:
        recommended_mode = "Job"

# --- Step 3: Log rationale ---
print("Execution Mode Recommendation:")
print(f"Workload size: {workload_size}")
print(f"All inputs ready? {inputs_ready}")
print(f"Iterative workload? {iterative_workload}")
print(f"Average QPU time per job: {qpu_time_per_job} min")
print(f"Recommended execution mode: {recommended_mode}")

# --- Step 4: Additional recommendations ---
if qpu_time_per_job < 1 and recommended_mode != "Job":
        print("Note: Combine multiple short QPU-time jobs into one batch to reduce overhead.")

"""
SUMMARY:
- Demonstrates recommended execution mode selection based on workload characteristics.
- Steps executed:
        1. Define workload size, readiness of inputs, whether iterative, and QPU time per job.
        2. Determine mode:
                * Session: iterative workloads needing dedicated access.
                * Batch: multiple jobs with all inputs ready.
                * Job: single or small test jobs.
        3. Print rationale with logging statements for clarity.
        4. Provide additional tip for combining short jobs to minimize overhead.
- Key points:
  * Use batch mode for multiple independent jobs to reduce wall-clock time.
  * Use session mode for iterative workloads requiring feedback and dedicated QPU.
  * Use job mode for single or small experiments.
  * Always consider QPU time per job to optimize throughput and cost.
"""
