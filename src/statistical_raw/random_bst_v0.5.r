# Node constructor function. Returns an environment to simulate an object with mutable fields.
Node <- function(key) {
  node_env <- new.env()
  node_env$key <- key
  node_env$left <- NULL
  node_env$right <- NULL
  return(node_env)
}

# BinarySearchTree constructor function. Returns an environment that contains the BST state and methods.
BinarySearchTree <- function() {
  bst_env <- new.env()
  bst_env$root <- NULL
  bst_env$size <- 0

  # Internal recursive insertion helper. Modifies nodes in place (due to environment semantics).
  bst_env$insert_recursive_internal <- function(current_node, key) {
    if (is.null(current_node)) {
      return(Node(key))
    }
    if (key < current_node$key) {
      # This needs to assign to the 'left' slot of the current_node environment
      current_node$left <- bst_env$insert_recursive_internal(current_node$left, key)
    } else if (key > current_node$key) {
      # This needs to assign to the 'right' slot of the current_node environment
      current_node$right <- bst_env$insert_recursive_internal(current_node$right, key)
    }
    return(current_node) # Return the (potentially modified) current_node
  }

  # Public insert method
  bst_env$insert <- function(key) {
    bst_env$root <- bst_env$insert_recursive_internal(bst_env$root, key)
    bst_env$size <- bst_env$size + 1
  }

  # Internal recursive search helper
  bst_env$search_recursive_internal <- function(current_node, key) {
    if (is.null(current_node) || current_node$key == key) {
      return(current_node)
    }
    if (key < current_node$key) {
      return(bst_env$search_recursive_internal(current_node$left, key))
    }
    return(bst_env$search_recursive_internal(current_node$right, key))
  }

  # Public search method
  bst_env$search <- function(key) {
    !is.null(bst_env$search_recursive_internal(bst_env$root, key))
  }

  return(bst_env)
}

run_benchmark_r <- function() {
  TEST_SIZE <- 50000
  SEARCH_COUNT <- 10000

  cat("Starting Pydroid Benchmarking Test (R Version)\n")
  cat(paste0("Test size for data generation and BST insertion: ", TEST_SIZE, " elements\n"))
  cat(paste0("Number of search operations: ", SEARCH_COUNT, "\n"))
  cat(paste0(paste(rep("-", 50), collapse = ""), "\n"))

  # Integer Generation
  start_time <- Sys.time()
  random_integers <- sample.int(1000000, TEST_SIZE, replace = TRUE)
  end_time <- Sys.time()
  generation_time <- as.numeric(end_time - start_time, units = "secs")
  integer_memory <- object.size(random_integers)
  cat(paste0("Generated ", TEST_SIZE, " random integers.\n"))
  cat(paste0("Time taken for integer generation: ", format(round(generation_time, 4), nsmall = 4), " seconds\n"))
  cat(paste0("Approximate memory for integers vector: ", format(round(integer_memory / (1024 * 1024), 2), nsmall = 2), " MB\n"))
  cat(paste0(paste(rep("-", 50), collapse = ""), "\n"))

  # Integer BST Construction
  bst_integers <- BinarySearchTree()
  start_time <- Sys.time()
  for (num in random_integers) {
    bst_integers$insert(num)
  }
  end_time <- Sys.time()
  bst_build_time <- as.numeric(end_time - start_time, units = "secs")
  cat(paste0("Built Binary Search Tree with ", TEST_SIZE, " elements.\n"))
  cat(paste0("Time taken for BST construction: ", format(round(bst_build_time, 4), nsmall = 4), " seconds\n"))
  # Memory for BST (rough estimate using object.size on the BST environment)
  bst_node_memory_estimate <- object.size(bst_integers)
  cat(paste0("Approximate memory for Integer BST (rough estimate): ", format(round(bst_node_memory_estimate / (1024 * 1024), 2), nsmall = 2), " MB\n"))
  cat(paste0(paste(rep("-", 50), collapse = ""), "\n"))

  # Integer BST Search
  search_keys_int <- c(sample.int(1000000, SEARCH_COUNT %/% 2, replace = TRUE),
                       random_integers[sample.int(TEST_SIZE, SEARCH_COUNT %/% 2, replace = TRUE)])
  search_keys_int <- sample(search_keys_int) # Shuffle

  start_time <- Sys.time()
  found_count_int <- 0
  for (key in search_keys_int) {
    if (bst_integers$search(key)) {
      found_count_int <- found_count_int + 1
    }
  }
  end_time <- Sys.time()
  search_time_int <- as.numeric(end_time - start_time, units = "secs")
  cat(paste0("Performed ", SEARCH_COUNT, " search operations in BST.\n"))
  cat(paste0("Found ", found_count_int, " out of ", SEARCH_COUNT, " keys.\n"))
  cat(paste0("Time taken for BST search operations: ", format(round(search_time_int, 4), nsmall = 4), " seconds\n"))
  cat(paste0(paste(rep("-", 50), collapse = ""), "\n"))

  # Decimal Generation
  start_time <- Sys.time()
  random_floats <- runif(TEST_SIZE, min = 0.0, max = 1000000.0)
  end_time <- Sys.time()
  float_generation_time <- as.numeric(end_time - start_time, units = "secs")
  float_memory <- object.size(random_floats)
  cat(paste0("Generated ", TEST_SIZE, " random decimals.\n"))
  cat(paste0("Time taken for decimal generation: ", format(round(float_generation_time, 4), nsmall = 4), " seconds\n"))
  cat(paste0("Approximate memory for decimals vector: ", format(round(float_memory / (1024 * 1024), 2), nsmall = 2), " MB\n"))
  cat(paste0(paste(rep("-", 50), collapse = ""), "\n"))

  # Decimal BST Construction
  bst_floats <- BinarySearchTree()
  start_time <- Sys.time()
  for (num in random_floats) {
    bst_floats$insert(num)
  }
  end_time <- Sys.time()
  bst_floats_build_time <- as.numeric(end_time - start_time, units = "secs")
  cat(paste0("Built Binary Search Tree with ", TEST_SIZE, " decimal elements.\n"))
  cat(paste0("Time taken for decimal BST construction: ", format(round(bst_floats_build_time, 4), nsmall = 4), " seconds\n"))
  bst_floats_node_memory_estimate <- object.size(bst_floats)
  cat(paste0("Approximate memory for Decimal BST (rough estimate): ", format(round(bst_floats_node_memory_estimate / (1024 * 1024), 2), nsmall = 2), " MB\n"))
  cat(paste0(paste(rep("-", 50), collapse = ""), "\n"))

  # Decimal BST Search
  search_keys_float <- c(runif(SEARCH_COUNT %/% 2, min = 0.0, max = 1000000.0),
                         random_floats[sample.int(TEST_SIZE, SEARCH_COUNT %/% 2, replace = TRUE)])
  search_keys_float <- sample(search_keys_float) # Shuffle

  start_time <- Sys.time()
  found_count_float <- 0
  for (key in search_keys_float) {
    if (bst_floats$search(key)) {
      found_count_float <- found_count_float + 1
    }
  }
  end_time <- Sys.time()
  float_search_time <- as.numeric(end_time - start_time, units = "secs")
  cat(paste0("Performed ", SEARCH_COUNT, " search operations in decimal BST.\n"))
  cat(paste0("Found ", found_count_float, " out of ", SEARCH_COUNT, " keys.\n"))
  cat(paste0("Time taken for decimal BST search operations: ", format(round(float_search_time, 4), nsmall = 4), " seconds\n"))
  cat(paste0(paste(rep("-", 50), collapse = ""), "\n"))

  cat("Benchmarking Complete.\n")
  cat("\nSummary Score:\n")
  cat(paste0("Integer Generation Time: ", format(round(generation_time, 4), nsmall = 4), " s\n"))
  cat(paste0("Integer Vector Memory (approx): ", format(round(integer_memory / (1024 * 1024), 2), nsmall = 2), " MB\n"))
  cat(paste0("Integer BST Build Time: ", format(round(bst_build_time, 4), nsmall = 4), " s\n"))
  cat(paste0("Integer BST Memory (rough estimate): ", format(round(bst_node_memory_estimate / (1024 * 1024), 2), nsmall = 2), " MB\n"))
  cat(paste0("Integer BST Search Time (", SEARCH_COUNT, " operations): ", format(round(search_time_int, 4), nsmall = 4), " s\n"))
  cat(paste0("Decimal Generation Time: ", format(round(float_generation_time, 4), nsmall = 4), " s\n"))
  cat(paste0("Decimal Vector Memory (approx): ", format(round(float_memory / (1024 * 1024), 2), nsmall = 2), " MB\n"))
  cat(paste0("Decimal BST Build Time: ", format(round(bst_floats_build_time, 4), nsmall = 4), " s\n"))
  cat(paste0("Decimal BST Memory (rough estimate): ", format(round(bst_floats_node_memory_estimate / (1024 * 1024), 2), nsmall = 2), " MB\n"))
  cat(paste0("Decimal BST Search Time (", SEARCH_COUNT, " operations): ", format(round(float_search_time, 4), nsmall = 4), " s\n"))
}

# Execute the benchmark
run_benchmark_r()