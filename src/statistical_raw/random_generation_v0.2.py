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

data_size = 1000000
data = [random.randint(1, 1000) for _ in range(data_size)]

print(f"Benchmarking with data size: {data_size}")

start_time = time.perf_counter()
mean_value = calculate_mean(data)
end_time = time.perf_counter()
mean_time = end_time - start_time

print(f"Calculated Mean: {mean_value}")
print(f"Time taken for Mean: {mean_time:.6f} seconds")

start_time = time.perf_counter()
mode_value = calculate_mode(data)
end_time = time.perf_counter()
mode_time = end_time - start_time

print(f"Calculated Mode: {mode_value}")
print(f"Time taken for Mode: {mode_time:.6f} seconds")