import time
import random
import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        self.size += 1

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key) is not None

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

def get_deep_sizeof(obj):
    sum_size = sys.getsizeof(obj)
    if isinstance(obj, (list, tuple, set, frozenset)):
        sum_size += sum(get_deep_sizeof(i) for i in obj)
    elif isinstance(obj, dict):
        sum_size += sum(get_deep_sizeof(k) + get_deep_sizeof(v) for k, v in obj.items())
    elif hasattr(obj, '__dict__'):
        sum_size += get_deep_sizeof(obj.__dict__)
    return sum_size

def run_benchmark():
    TEST_SIZE = 50000
    SEARCH_COUNT = 10000

    print("Starting Pydroid Benchmarking Test")
    print(f"Test size for data generation and BST insertion: {TEST_SIZE} elements")
    print(f"Number of search operations: {SEARCH_COUNT}")
    print("-" * 50)

    start_time = time.time()
    random_integers = [random.randint(0, 1000000) for _ in range(TEST_SIZE)]
    end_time = time.time()
    generation_time = end_time - start_time
    integer_memory = get_deep_sizeof(random_integers)
    print(f"Generated {TEST_SIZE} random integers.")
    print(f"Time taken for integer generation: {generation_time:.4f} seconds")
    print(f"Approximate memory for integers list: {integer_memory / (1024 * 1024):.2f} MB")
    print("-" * 50)

    bst = BinarySearchTree()
    start_time = time.time()
    for num in random_integers:
        bst.insert(num)
    end_time = time.time()
    bst_build_time = end_time - start_time
    print(f"Built Binary Search Tree with {TEST_SIZE} elements.")
    print(f"Time taken for BST construction: {bst_build_time:.4f} seconds")
    node_memory_estimate = bst.size * (sys.getsizeof(Node(0)) + sys.getsizeof(0))
    print(f"Approximate memory for BST nodes (rough estimate): {node_memory_estimate / (1024 * 1024):.2f} MB")
    print("-" * 50)

    search_keys = [random.randint(0, 1000000) for _ in range(SEARCH_COUNT // 2)]
    search_keys.extend([random_integers[random.randint(0, TEST_SIZE - 1)] for _ in range(SEARCH_COUNT // 2)])
    random.shuffle(search_keys)

    start_time = time.time()
    found_count = 0
    for key in search_keys:
        if bst.search(key):
            found_count += 1
    end_time = time.time()
    search_time = end_time - start_time
    print(f"Performed {SEARCH_COUNT} search operations in BST.")
    print(f"Found {found_count} out of {SEARCH_COUNT} keys.")
    print(f"Time taken for BST search operations: {search_time:.4f} seconds")
    print("-" * 50)

    start_time = time.time()
    random_floats = [random.uniform(0.0, 1000000.0) for _ in range(TEST_SIZE)]
    end_time = time.time()
    float_generation_time = end_time - start_time
    float_memory = get_deep_sizeof(random_floats)
    print(f"Generated {TEST_SIZE} random decimals.")
    print(f"Time taken for decimal generation: {float_generation_time:.4f} seconds")
    print(f"Approximate memory for decimals list: {float_memory / (1024 * 1024):.2f} MB")
    print("-" * 50)

    bst_floats = BinarySearchTree()
    start_time = time.time()
    for num in random_floats:
        bst_floats.insert(num)
    end_time = time.time()
    bst_floats_build_time = end_time - start_time
    print(f"Built Binary Search Tree with {TEST_SIZE} decimal elements.")
    print(f"Time taken for decimal BST construction: {bst_floats_build_time:.4f} seconds")
    node_float_memory_estimate = bst_floats.size * (sys.getsizeof(Node(0.0)) + sys.getsizeof(0.0))
    print(f"Approximate memory for decimal BST nodes (rough estimate): {node_float_memory_estimate / (1024 * 1024):.2f} MB")
    print("-" * 50)

    search_float_keys = [random.uniform(0.0, 1000000.0) for _ in range(SEARCH_COUNT // 2)]
    search_float_keys.extend([random_floats[random.randint(0, TEST_SIZE - 1)] for _ in range(SEARCH_COUNT // 2)])
    random.shuffle(search_float_keys)

    start_time = time.time()
    found_float_count = 0
    for key in search_float_keys:
        if bst_floats.search(key):
            found_float_count += 1
    end_time = time.time()
    float_search_time = end_time - start_time
    print(f"Performed {SEARCH_COUNT} search operations in decimal BST.")
    print(f"Found {found_float_count} out of {SEARCH_COUNT} keys.")
    print(f"Time taken for decimal BST search operations: {float_search_time:.4f} seconds")
    print("-" * 50)

    print("Benchmarking Complete.")
    print("\nSummary Score:")
    print(f"Integer Generation Time: {generation_time:.4f} s")
    print(f"Integer List Memory (approx): {integer_memory / (1024 * 1024):.2f} MB")
    print(f"Integer BST Build Time: {bst_build_time:.4f} s")
    print(f"Integer BST Node Memory (rough estimate): {node_memory_estimate / (1024 * 1024):.2f} MB")
    print(f"Integer BST Search Time ({SEARCH_COUNT} operations): {search_time:.4f} s")
    print(f"Decimal Generation Time: {float_generation_time:.4f} s")
    print(f"Decimal List Memory (approx): {float_memory / (1024 * 1024):.2f} MB")
    print(f"Decimal BST Build Time: {bst_floats_build_time:.4f} s")
    print(f"Decimal BST Node Memory (rough estimate): {node_float_memory_estimate / (1024 * 1024):.2f} MB")
    print(f"Decimal BST Search Time ({SEARCH_COUNT} operations): {float_search_time:.4f} s")

run_benchmark()