import os
import time
import tracemalloc
import matplotlib.pyplot as plt
from sat_solver import solve_sat, solve_3sat
from reduction import sat_to_3sat
from utils import generate_random_formula

CHARTS_DIR = "charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

# Measure time and memory using tracemalloc with multiple iterations
def measure_time_and_memory(func, iterations, *args):
    total_time = 0
    total_memory = 0

    for _ in range(iterations):
        tracemalloc.start()
        start_time = time.time()

        # Call solver function
        func(*args)

        end_time = time.time()
        current, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        total_time += end_time - start_time
        total_memory += peak_memory

    avg_time = total_time / iterations
    avg_memory = (total_memory / iterations) / (1024 ** 2)  # Convert memory to MB
    return avg_time, avg_memory

# Performance analysis
def analyze_performance():
    num_vars = 5  # Fixed number of variables
    clause_range = range(1, 16, 1)  # Gradually increase the number of clauses
    iterations = 1  # Number of repetitions for averaging
    results = {
        "num_clauses": [],
        "sat_time": [],
        "sat_memory": [],
        "three_sat_time": [],
        "three_sat_memory": [],
    }

    for nbr_clauses in clause_range:
        print(f"Testing with {nbr_clauses} clauses...")

        # Generate random SAT formula
        sat_formula = generate_random_formula(num_vars, nbr_clauses)
        print(f"Generated SAT Formula ({nbr_clauses} clauses): {sat_formula}")

        # Measure SAT performance
        sat_time, sat_memory = measure_time_and_memory(solve_sat, iterations, sat_formula, num_vars)
        sat_result = solve_sat(sat_formula, num_vars)  # Solve SAT to get the solution
        print(f"SAT Solution: {sat_result}")

        results["num_clauses"].append(nbr_clauses)
        results["sat_time"].append(sat_time)
        results["sat_memory"].append(sat_memory)

        # Convert SAT to 3-SAT
        three_sat_formula, updated_vars = sat_to_3sat(sat_formula)
        print(f"Converted 3-SAT Formula ({nbr_clauses} clauses): {three_sat_formula}")

        # Measure 3-SAT performance
        three_sat_time, three_sat_memory = measure_time_and_memory(solve_3sat, iterations, three_sat_formula, updated_vars)
        three_sat_result = solve_3sat(three_sat_formula, updated_vars)  # Solve 3-SAT to get the solution
        print(f"3-SAT Solution: {three_sat_result}")

        results["three_sat_time"].append(three_sat_time)
        results["three_sat_memory"].append(three_sat_memory)

        print(f"SAT - Time: {sat_time:.6f}s, Memory: {sat_memory:.6f} MB")
        print(f"3-SAT - Time: {three_sat_time:.6f}s, Memory: {three_sat_memory:.6f} MB\n")

    # Plot and save the results
    save_results_charts(results)

# Save the results as charts
def save_results_charts(results):
    # Execution time plot
    plt.figure(figsize=(12, 6))
    plt.plot(results["num_clauses"], results["sat_time"], label="SAT Time")
    plt.plot(results["num_clauses"], results["three_sat_time"], label="3-SAT Time")
    plt.xlabel("Number of Clauses")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time vs Number of Clauses")
    plt.legend()
    plt.grid()
    plt.savefig(os.path.join(CHARTS_DIR, "execution_time_vs_clauses.png"))
    plt.close()

    # Memory usage plot
    plt.figure(figsize=(12, 6))
    plt.plot(results["num_clauses"], results["sat_memory"], label="SAT Memory")
    plt.plot(results["num_clauses"], results["three_sat_memory"], label="3-SAT Memory")
    plt.xlabel("Number of Clauses")
    plt.ylabel("Memory Usage (MB)")
    plt.title("Memory Usage vs Number of Clauses")
    plt.legend()
    plt.grid()
    plt.savefig(os.path.join(CHARTS_DIR, "memory_usage_vs_clauses.png"))
    plt.close()

    print(f"Charts saved in the '{CHARTS_DIR}' directory.")

if __name__ == "__main__":
    analyze_performance()
