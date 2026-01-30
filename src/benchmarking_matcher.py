import matplotlib.pyplot as plt
import time
from io_utils import read_preferences
from matcher import gale_shapley

def time_matcher(n_values):
    times = [None]*10
    for n,i in zip(n_values, range(10)):
        input_file = f"data/taskC/n{n}.in"
        
        start = time.perf_counter()
        n_read, hospital_prefs, student_prefs = read_preferences(input_file)
        h_match = gale_shapley(n_read, hospital_prefs, student_prefs)
        end = time.perf_counter()
        
        elapsed = end - start
        times[i] = elapsed 
    return times

def plot_matcher_benchmark_results(n_values, times):
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linewidth=2, markersize=8)
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Benchmark Results")
    plt.grid(True)
    plt.savefig("docs/matcher_times.png")
    plt.close()

n_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
times = time_matcher(n_values)
plot_matcher_benchmark_results(n_values, times)