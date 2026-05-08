import time
import random
import math

def generate_random_list_stats(size, lower=0, upper=1000):
    return [random.randint(lower, upper) for _ in range(size)]

def calculate_complex_statistics(data):
    n = len(data)
    if n == 0: return {}

    total_sum = 0
    for x in data:
        total_sum += x
    mean = total_sum / n

    sorted_data = sorted(data)
    mid = n // 2
    median = (sorted_data[mid - 1] + sorted_data[mid]) / 2 if n % 2 == 0 else sorted_data[mid]

    sum_sq_diff = 0
    for x in data:
        sum_sq_diff += (x - mean) ** 2
    variance = sum_sq_diff / n
    std_dev = math.sqrt(variance)

    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    max_count = 0
    mode = None
    for k, v in counts.items():
        if v > max_count:
            max_count = v
            mode = k
        elif v == max_count: 
            if not isinstance(mode, list):
                mode = [mode]
            if k not in mode:
                mode.append(k)

    return {
        "mean": mean,
        "median": median,
        "variance": variance,
        "std_dev": std_dev,
        "mode": mode
    }

def run_statistical_stress_test(size):
    print(f"Running statistical stress test on a list of size {size}...")
    data = generate_random_list_stats(size)
    
    start_time = time.perf_counter()
    stats = calculate_complex_statistics(data)
    end_time = time.perf_counter()
    
    duration = end_time - start_time
    print(f"  Statistical test completed in {duration:.4f} seconds")

if __name__ == '__main__':
    test_size = random.randint(2 * 10**6, 5 * 10**6)
    run_statistical_stress_test(test_size)