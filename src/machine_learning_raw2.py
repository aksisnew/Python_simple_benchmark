
if __name__ == '__main__':
    print("\n--- Starting CPU Stress Tests ---\n")

    # Number of CPU cores available for multiprocessing (or a fixed number for testing)
    num_cores = multiprocessing.cpu_count()
    print(f"Detected {num_cores} CPU cores for multi-core tests.\n")

    # --- Single-core CPU-bound tests ---

    # Test 1: Large Matrix Multiplication
    matrix_dim = random.randint(100, 200)
    run_single_core_test(f"Matrix Multiplication ({matrix_dim}x{matrix_dim})", test_matrix_multiplication, matrix_dim)

    # Test 2: Summing a very large list
    list_size_sum = random.randint(5 * 10**6, 10**7)
    run_single_core_test(f"Large List Sum (size {list_size_sum})", test_large_list_sum, list_size_sum)

    # Test 3: Sieve of Eratosthenes for prime numbers
    sieve_limit = random.randint(5 * 10**5, 10**6)
    run_single_core_test(f"Sieve of Eratosthenes (limit {sieve_limit})", test_sieve_of_eratosthenes, sieve_limit)

    # Test 4: Recursive Fibonacci (computationally expensive)
    fib_n = random.randint(28, 35) # Keep N relatively small to avoid extremely long runtimes
    run_single_core_test(f"Recursive Fibonacci (n={fib_n})", test_recursive_fibonacci, fib_n)

    # Test 5: Statistical calculations on a large list
    stats_list_size = random.randint(2 * 10**6, 5 * 10**6)
    run_single_core_test(f"List Statistics (mean, std dev) (size {stats_list_size})", test_statistics_calculation, stats_list_size)

    # Test 6: Polynomial Evaluation
    poly_points = random.randint(5 * 10**5, 10**6)
    poly_degree = random.randint(10, 20)
    run_single_core_test(f"Polynomial Evaluation ({poly_points} points, degree {poly_degree})", test_polynomial_evaluation, poly_points, poly_degree)

    # Test 7: Vector Dot Product
    vector_size = random.randint(5 * 10**6, 10**7)
    run_single_core_test(f"Vector Dot Product (size {vector_size})", test_vector_dot_product, vector_size)

    # Test 8: Quick Sort a large list
    sort_list_size = random.randint(10**5, 2 * 10**5)
    run_single_core_test(f"Quick Sort (size {sort_list_size})", test_quick_sort, generate_random_list(sort_list_size))

    # Test 9: String Hashing
    num_hashes = random.randint(5 * 10**5, 10**6)
    hash_len = random.randint(10, 50)
    run_single_core_test(f"String Hashing ({num_hashes} strings, length {hash_len})", test_string_hashing, num_hashes, hash_len)

    # Test 10: Simple Neural Network Forward Pass
    nn_input = random.randint(50, 100)
    nn_hidden = random.randint(100, 200)
    nn_output = random.randint(10, 20)
    nn_samples = random.randint(5000, 10000)
    run_single_core_test(f"Simple NN Forward Pass (samples {nn_samples})", test_simple_nn_forward_pass, nn_input, nn_hidden, nn_output, nn_samples)

    # Test 11: K-Means Single Iteration
    kmeans_points = random.randint(10**5, 2 * 10**5)
    kmeans_clusters = random.randint(50, 100)
    kmeans_dims = random.randint(10, 20)
    run_single_core_test(f"K-Means Single Iteration (points {kmeans_points}, clusters {kmeans_clusters}, dims {kmeans_dims})", test_k_means_single_iteration, kmeans_points, kmeans_clusters, kmeans_dims)

    # Test 12: Mandelbrot Set Generation
    mandel_width = random.randint(500, 800)
    mandel_height = random.randint(400, 600)
    mandel_iter = random.randint(50, 100)
    run_single_core_test(f"Mandelbrot Set ({mandel_width}x{mandel_height}, {mandel_iter} iter)", test_mandelbrot_set, mandel_width, mandel_height, mandel_iter)

    # Test 13: Iterative Factorial of a large number
    fact_n = random.randint(50000, 100000)
    run_single_core_test(f"Iterative Factorial (n={fact_n})", test_factorial_iterative, fact_n)

    # Test 14: Complex Math Operations
    math_ops_count = random.randint(5 * 10**6, 10**7)
    run_single_core_test(f"Complex Math Operations ({math_ops_count} ops)", test_complex_math_operations, math_ops_count)

    # Test 15: Chained List Comprehensions
    lc_size = random.randint(10**6, 2 * 10**6)
    run_single_core_test(f"Chained List Comprehensions (size {lc_size})", test_list_comprehension_chain, lc_size)

    # Test 16: Dictionary Operations
    dict_entries = random.randint(5 * 10**5, 10**6)
    dict_accesses = random.randint(10**6, 2 * 10**6)
    run_single_core_test(f"Dictionary Operations ({dict_entries} entries, {dict_accesses} accesses)", test_dictionary_operations, dict_entries, dict_accesses)


    print("\n--- Starting Multi-core CPU-bound tests ---\n")

    # Test 17: Parallel Prime Checking
    pp_limit = random.randint(2 * 10**6, 4 * 10**6)
    run_multi_core_test(f"Parallel Prime Checking (limit {pp_limit}, {num_cores} processes)", test_parallel_prime_checking, pp_limit, num_cores)

    # Test 18: Parallel Matrix Row Sum
    pm_dim = random.randint(5000, 8000)
    run_multi_core_test(f"Parallel Matrix Row Sum ({pm_dim}x{pm_dim}, {num_cores} processes)", test_parallel_matrix_row_sum, pm_dim, num_cores)

    # Test 19: Parallel Data Processing (sqrt and log)
    pdp_size = random.randint(10**7, 2 * 10**7)
    run_multi_core_test(f"Parallel Data Processing (size {pdp_size}, {num_cores} processes)", test_parallel_data_processing, pdp_size, num_cores)

    # Test 20: Parallel Monte Carlo Pi Estimation
    pi_sims = random.randint(5 * 10**7, 10**8)
    run_multi_core_test(f"Parallel Monte Carlo Pi Estimation (sims {pi_sims}, {num_cores} processes)", test_parallel_monte_carlo_pi, pi_sims, num_cores)

    # Test 21: Parallel NN Inference
    pnn_input = random.randint(30, 60)
    pnn_hidden = random.randint(60, 120)
    pnn_output = random.randint(5, 15)
    pnn_samples = random.randint(50000, 100000)
    run_multi_core_test(f"Parallel NN Inference (samples {pnn_samples}, {num_cores} processes)", test_parallel_nn_inference, pnn_input, pnn_hidden, pnn_output, pnn_samples, num_cores)

    # Test 22: Parallel K-Means Assignment Step
    pk_points = random.randint(5 * 10**5, 10**6)
    pk_clusters = random.randint(100, 200)
    pk_dims = random.randint(15, 30)
    run_multi_core_test(f"Parallel K-Means Assignment (points {pk_points}, {num_cores} processes)", test_parallel_k_means_assignment, pk_points, pk_clusters, pk_dims, num_cores)

    print("\n--- All CPU Stress Tests Completed ---\n")
