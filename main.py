import os
import time
import tracemalloc
import matplotlib.pyplot as plt
from sat_solver import solve_sat, solve_3sat
from reduction import sat_to_3sat
from utils import generate_random_formula

CHARTS_DIR = "charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

# measure time and memory using tracemalloc
def measure_time_and_memory(func, *args):
    tracemalloc.start()
    start_time = time.time()

    # call solver function
    func(*args)

    end_time = time.time()
    current, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time_taken = end_time - start_time
    memory_used = peak_memory / (1024 ** 2)  # to MB
    return time_taken, memory_used

# performance analysis
def analyze_performance():
    num_vars = 5  #number of variables
    clause_range = range(1, 16, 1)  #increase number of clauses gradually
    results = {
        "num_clauses": [],
        "sat_time": [],
        "sat_memory": [],
        "three_sat_time": [],
        "three_sat_memory": [],
    }

    for nbr_clauses in clause_range:
        print(f"Testing with {nbr_clauses} clauses...")

        #random sat formula
        sat_formula = generate_random_formula(num_vars, nbr_clauses)
        print(f"Generated SAT Formula ({nbr_clauses} clauses): {sat_formula}")

        # sat performance
        sat_time, sat_memory = measure_time_and_memory(solve_sat, sat_formula, num_vars)
        sat_result = solve_sat(sat_formula, num_vars)  
        print(f"SAT Solution: {sat_result}")

        results["num_clauses"].append(nbr_clauses)
        results["sat_time"].append(sat_time)
        results["sat_memory"].append(sat_memory)

        # convert SAT to 3-Sat
        three_sat_formula, updated_vars = sat_to_3sat(sat_formula)
        print(f"Converted 3-SAT Formula ({nbr_clauses} clauses): {three_sat_formula}")

        # 3-sat performance
        three_sat_time, three_sat_memory = measure_time_and_memory(solve_3sat, three_sat_formula, updated_vars)
        three_sat_result = solve_3sat(three_sat_formula, updated_vars)  # Solve 3-SAT to get the solution
        print(f"3-SAT Solution: {three_sat_result}")

        results["three_sat_time"].append(three_sat_time)
        results["three_sat_memory"].append(three_sat_memory)

        print(f"SAT - Time: {sat_time:.6f}s, Memory: {sat_memory:.6f} MB")
        print(f"3-SAT - Time: {three_sat_time:.6f}s, Memory: {three_sat_memory:.6f} MB\n")

    # plot results
    save_results_charts(results)

# save the results as charts
def save_results_charts(results):
    # EXecution time 
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

    # Memory usage 
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
