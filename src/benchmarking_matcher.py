import matplotlib.pyplot as plt
import time
from io_utils import read_preferences
from matcher import gale_shapley
from verifier import check_validity, check_stability

def time_matcher(n_values):
    count = len(n_values)
    times_matcher = [None] * count
    times_with_verifier = [None] * count

    for i, n in enumerate(n_values):
        input_file = f"data/taskC/n{n}.in"

        # Time matcher only (read + match)
        start = time.perf_counter()
        n_read, hospital_prefs, student_prefs = read_preferences(input_file)
        h_match = gale_shapley(n_read, hospital_prefs, student_prefs)
        end = time.perf_counter()
        times_matcher[i] = end - start

        # Time matcher + verifier (read + match + checks)
        start = time.perf_counter()
        n_read, hospital_prefs, student_prefs = read_preferences(input_file)
        h_match = gale_shapley(n_read, hospital_prefs, student_prefs)
        is_valid = check_validity(matching=h_match, n=n_read)
        is_stable = check_stability(h_match, hospital_prefs, student_prefs)
        end = time.perf_counter()
        times_with_verifier[i] = end - start

    return times_matcher, times_with_verifier

def plot_matcher_benchmark_results(n_values, times_matcher, times_with_verifier):
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times_matcher, marker='o', linewidth=2, markersize=8, label='matcher only')
    plt.plot(n_values, times_with_verifier, marker='s', linewidth=2, markersize=8, label='matcher + verifier')
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Benchmark Results: matcher vs matcher+verifier")
    plt.grid(True)
    plt.legend()
    plt.savefig("docs/matcher_times.png")
    plt.close()

n_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
times_matcher, times_with_verifier = time_matcher(n_values)
plot_matcher_benchmark_results(n_values, times_matcher, times_with_verifier)