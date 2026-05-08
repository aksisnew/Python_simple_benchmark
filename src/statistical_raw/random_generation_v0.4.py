import random
import time

def calculate_mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def calculate_mode(data):
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1

    max_count = 0
    mode = None
    for k, v in counts.items():
        if v > max_count:
            max_count = v
            mode = k
    return mode

# Get user input for benchmarking parameters
num_iterations = int(input("Enter the number of iterations for benchmarking (e.g., 5): "))
data_size = int(input("Enter the size of the data for each iteration (e.g., 1000000): "))
min_value = int(input("Enter the minimum value for random data (e.g., 1): "))
max_value = int(input("Enter the maximum value for random data (e.g., 1000): "))

mean_times = []
mode_times = []

print(f"\nStarting benchmark with {num_iterations} iterations, data size: {data_size}, value range: [{min_value}, {max_value}]")

for i in range(num_iterations):
    print(f"\n--- Iteration {i+1}/{num_iterations} ---")
    data = [random.randint(min_value, max_value) for _ in range(data_size)]

    start_time = time.perf_counter()
    mean_value = calculate_mean(data)
    end_time = time.perf_counter()
    mean_time = end_time - start_time
    mean_times.append(mean_time)

    print(f"Calculated Mean: {mean_value}")
    print(f"Time taken for Mean: {mean_time:.6f} seconds")

    start_time = time.perf_counter()
    mode_value = calculate_mode(data)
    end_time = time.perf_counter()
    mode_time = end_time - start_time
    mode_times.append(mode_time)

    print(f"Calculated Mode: {mode_value}")
    print(f"Time taken for Mode: {mode_time:.6f} seconds")

print("\n--- Benchmark Summary ---")
print(f"Average Time taken for Mean over {num_iterations} iterations: {sum(mean_times)/num_iterations:.6f} seconds")
print(f"Average Time taken for Mode over {num_iterations} iterations: {sum(mode_times)/num_iterations:.6f} seconds")