import time
import random
import math
import multiprocessing

def generate_random_matrix(rows, cols, lower=0, upper=100):
    return [[random.uniform(lower, upper) for _ in range(cols)] for _ in range(rows)]

def generate_random_vector(size, lower=0, upper=100):
    return [random.uniform(lower, upper) for _ in range(size)]

def generate_random_list(size, lower=0, upper=100):
    return [random.randint(lower, upper) for _ in range(size)]

def time_test(func, *args, **kwargs):
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time

def run_single_core_test(name, func, *args, **kwargs):
    print(f"Running single-core test: {name}...")
    duration = time_test(func, *args, **kwargs)
    print(f"  {name} completed in {duration:.4f} seconds")

def run_multi_core_test(name, func, *args, **kwargs):
    print(f"Running multi-core test: {name}...")
    duration = time_test(func, *args, **kwargs)
    print(f"  {name} completed in {duration:.4f} seconds")




def test_matrix_multiplication(dim):
    matrix_a = generate_random_matrix(dim, dim)
    matrix_b = generate_random_matrix(dim, dim)
    result_matrix = [[0 for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix

def test_large_list_sum(size):
    data = generate_random_list(size)
    total_sum = 0
    for x in data:
        total_sum += x
    return total_sum

def test_sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for multiple in range(i * i, limit + 1, i):
                primes[multiple] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

def test_recursive_fibonacci(n):
    if n <= 1:
        return n
    return test_recursive_fibonacci(n - 1) + test_recursive_fibonacci(n - 2)

def test_statistics_calculation(size):
    data = generate_random_list(size, 0, 1000)
    n = len(data)
    if n == 0: return (0, 0)
    mean = sum(data) / n
    variance = sum([(x - mean) ** 2 for x in data]) / n
    std_dev = math.sqrt(variance)
    return mean, std_dev

def test_polynomial_evaluation(num_points, degree):
    coefficients = generate_random_vector(degree + 1, -10, 10)
    points = generate_random_vector(num_points, -5, 5)
    results = []
    for x in points:
        y = 0
        for i, coef in enumerate(coefficients):
            y += coef * (x ** i)
        results.append(y)
    return results

def test_vector_dot_product(size):
    vec1 = generate_random_vector(size)
    vec2 = generate_random_vector(size)
    dot_product = 0
    for i in range(size):
        dot_product += vec1[i] * vec2[i]
    return dot_product

def test_quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return test_quick_sort(left) + middle + test_quick_sort(right)

def test_string_hashing(num_strings, length):
    results = []
    for _ in range(num_strings):
        s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))
        results.append(hash(s))
    return results

def test_simple_nn_forward_pass(input_size, hidden_size, output_size, num_samples):
    weights1 = generate_random_matrix(input_size, hidden_size, -1, 1)
    bias1 = generate_random_vector(hidden_size, -1, 1)
    weights2 = generate_random_matrix(hidden_size, output_size, -1, 1)
    bias2 = generate_random_vector(output_size, -1, 1)
    inputs = generate_random_matrix(num_samples, input_size, 0, 1)

    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    outputs = []
    for sample in inputs:
        hidden_layer_input = [0] * hidden_size
        for h in range(hidden_size):
            for i in range(input_size):
                hidden_layer_input[h] += sample[i] * weights1[i][h]
            hidden_layer_input[h] += bias1[h]

        hidden_layer_output = [sigmoid(x) for x in hidden_layer_input]

        output_layer_input = [0] * output_size
        for o in range(output_size):
            for h in range(hidden_size):
                output_layer_input[o] += hidden_layer_output[h] * weights2[h][o]
            output_layer_input[o] += bias2[o]

        final_output = [sigmoid(x) for x in output_layer_input]
        outputs.append(final_output)
    return outputs

def test_k_means_single_iteration(num_points, num_clusters, dimensions):
    points = generate_random_matrix(num_points, dimensions, 0, 100)
    centroids = generate_random_matrix(num_clusters, dimensions, 0, 100)
    
    new_centroids_sum = [[0.0] * dimensions for _ in range(num_clusters)]
    new_centroids_count = [0] * num_clusters

    for point_idx in range(num_points):
        point = points[point_idx]
        min_dist = float('inf')
        closest_cluster = -1
        
        for cluster_idx in range(num_clusters):
            centroid = centroids[cluster_idx]
            dist = 0
            for d in range(dimensions):
                dist += (point[d] - centroid[d]) ** 2
            
            if dist < min_dist:
                min_dist = dist
                closest_cluster = cluster_idx
        
        if closest_cluster != -1:
            new_centroids_count[closest_cluster] += 1
            for d in range(dimensions):
                new_centroids_sum[closest_cluster][d] += point[d]
    
    # Calculate new centroids (simplified, just sum and count for one iteration)
    final_centroids = []
    for cluster_idx in range(num_clusters):
        if new_centroids_count[cluster_idx] > 0:
            final_centroids.append([new_centroids_sum[cluster_idx][d] / new_centroids_count[cluster_idx] for d in range(dimensions)])
        else:
            final_centroids.append(centroids[cluster_idx]) # Centroid remains same if no points assigned
    return final_centroids

def test_mandelbrot_set(width, height, max_iter):
    results = []
    for row in range(height):
        for col in range(width):
            c_real = -2.0 + col * (3.0 / width)
            c_imag = -1.5 + row * (3.0 / height)
            z_real = 0.0
            z_imag = 0.0
            iteration = 0
            while (z_real * z_real + z_imag * z_imag < 4) and (iteration < max_iter):
                z_real_new = z_real * z_real - z_imag * z_imag + c_real
                z_imag_new = 2 * z_real * z_imag + c_imag
                z_real = z_real_new
                z_imag = z_imag_new
                iteration += 1
            results.append(iteration)
    return results

def test_factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_complex_math_operations(num_ops):
    results = []
    for _ in range(num_ops):
        a = random.uniform(0.1, 100)
        b = random.uniform(0.1, 100)
        op_type = random.randint(0, 4)
        if op_type == 0: results.append(math.sin(a) * math.cos(b))
        elif op_type == 1: results.append(math.log(a) / math.exp(b))
        elif op_type == 2: results.append(math.sqrt(a**2 + b**2))
        elif op_type == 3: results.append(math.tan(a) + math.atan(b))
        else: results.append(math.hypot(a, b))
    return results

def test_list_comprehension_chain(size):
    data = generate_random_list(size, 0, 100)
    result = [x * 2 for x in [y + 1 for y in [z**2 for z in data if z % 2 == 0] if y < 5000] if x > 100]
    return result

def test_dictionary_operations(num_entries, num_accesses):
    data = {str(i): random.randint(0, 1000) for i in range(num_entries)}
    total_value = 0
    for _ in range(num_accesses):
        key = str(random.randint(0, num_entries - 1))
        if key in data: total_value += data[key]
    return total_value





def _parallel_prime_check_worker(start, end):
    primes = []
    for n in range(start, end + 1):
        if n < 2: continue
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime: primes.append(n)
    return primes

def test_parallel_prime_checking(limit, num_processes):
    chunk_size = limit // num_processes
    ranges = [(i * chunk_size, (i + 1) * chunk_size - 1) for i in range(num_processes - 1)]
    ranges.append(((num_processes - 1) * chunk_size, limit))
    
    all_primes = []
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.starmap(_parallel_prime_check_worker, ranges)
        for r in results: all_primes.extend(r)
    return sorted(all_primes)

def _parallel_matrix_row_sum_worker(row):
    return sum(row)

def test_parallel_matrix_row_sum(dim, num_processes):
    matrix = generate_random_matrix(dim, dim)
    with multiprocessing.Pool(num_processes) as pool:
        row_sums = pool.map(_parallel_matrix_row_sum_worker, matrix)
    return row_sums

def _parallel_data_processing_worker(data_chunk):
    return [math.sqrt(x) + math.log(x + 1) for x in data_chunk if x > 0]

def test_parallel_data_processing(size, num_processes):
    data = generate_random_list(size, 1, 1000)
    chunk_size = size // num_processes
    chunks = [data[i:i + chunk_size] for i in range(0, size, chunk_size)]
    
    processed_data = []
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(_parallel_data_processing_worker, chunks)
        for r in results: processed_data.extend(r)
    return processed_data

def _parallel_monte_carlo_pi_worker(num_simulations_per_process):
    in_circle_count = 0
    for _ in range(num_simulations_per_process):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1: in_circle_count += 1
    return in_circle_count

def test_parallel_monte_carlo_pi(total_simulations, num_processes):
    sims_per_process = total_simulations // num_processes
    
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(_parallel_monte_carlo_pi_worker, [sims_per_process] * num_processes)
    
    total_in_circle = sum(results)
    pi_estimate = 4 * total_in_circle / total_simulations
    return pi_estimate

def _parallel_nn_inference_worker(samples_chunk, weights1, bias1, weights2, bias2, input_size, hidden_size, output_size):
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    outputs = []
    for sample in samples_chunk:
        hidden_layer_input = [0] * hidden_size
        for h in range(hidden_size):
            for i in range(input_size):
                hidden_layer_input[h] += sample[i] * weights1[i][h]
            hidden_layer_input[h] += bias1[h]

        hidden_layer_output = [sigmoid(x) for x in hidden_layer_input]

        output_layer_input = [0] * output_size
        for o in range(output_size):
            for h in range(hidden_size):
                output_layer_input[o] += hidden_layer_output[h] * weights2[h][o]
            output_layer_input[o] += bias2[o]

        final_output = [sigmoid(x) for x in output_layer_input]
        outputs.append(final_output)
    return outputs

def test_parallel_nn_inference(input_size, hidden_size, output_size, num_samples, num_processes):
    weights1 = generate_random_matrix(input_size, hidden_size, -1, 1)
    bias1 = generate_random_vector(hidden_size, -1, 1)
    weights2 = generate_random_matrix(hidden_size, output_size, -1, 1)
    bias2 = generate_random_vector(output_size, -1, 1)
    all_inputs = generate_random_matrix(num_samples, input_size, 0, 1)

    chunk_size = num_samples // num_processes
    input_chunks = [all_inputs[i:i + chunk_size] for i in range(0, num_samples, chunk_size)]

    all_outputs = []
    with multiprocessing.Pool(num_processes) as pool:
        args = [(chunk, weights1, bias1, weights2, bias2, input_size, hidden_size, output_size) for chunk in input_chunks]
        results = pool.starmap(_parallel_nn_inference_worker, args)
        for r in results: all_outputs.extend(r)
    return all_outputs

def _parallel_k_means_assignment_worker(points_chunk, centroids, dimensions):
    assignments = []
    for point in points_chunk:
        min_dist = float('inf')
        closest_cluster = -1
        for cluster_idx in range(len(centroids)):
            centroid = centroids[cluster_idx]
            dist = 0
            for d in range(dimensions):
                dist += (point[d] - centroid[d]) ** 2
            if dist < min_dist:
                min_dist = dist
                closest_cluster = cluster_idx
        assignments.append(closest_cluster)
    return assignments

def test_parallel_k_means_assignment(num_points, num_clusters, dimensions, num_processes):
    points = generate_random_matrix(num_points, dimensions, 0, 100)
    centroids = generate_random_matrix(num_clusters, dimensions, 0, 100)

    chunk_size = num_points // num_processes
    point_chunks = [points[i:i + chunk_size] for i in range(0, num_points, chunk_size)]

    all_assignments = []
    with multiprocessing.Pool(num_processes) as pool:
        args = [(chunk, centroids, dimensions) for chunk in point_chunks]
        results = pool.starmap(_parallel_k_means_assignment_worker, args)
        for r in results: all_assignments.extend(r)
    return all_assignments
