"""

Part 1  Randomized Quicksort Analysis
"""

import numpy as np
import time

# Randomized Quicksort function
def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# Function to choose a random pivot and partition the array
def randomized_partition(arr, low, high):
    pivot_index = np.random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return partition(arr, low, high)

# Partition function for quicksort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Iterative Quicksort using first element as pivot
def deterministic_quicksort_iterative(arr, low, high):
    # Create an explicit stack
    stack = [(low, high)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = deterministic_partition(arr, low, high)

            # Push subarrays on the stack for further processing
            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

# Partition function using first element as pivot
def deterministic_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Function to test and compare both algorithms
def compare_algorithms():
    sizes = [100, 500, 1000]  # Array sizes for testing
    for size in sizes:
        print(f"Array size: {size}")

        # Generate test arrays
        arr_random = np.random.randint(0, 10000, size)
        arr_sorted = np.sort(arr_random)
        arr_reverse = arr_sorted[::-1]
        arr_repeated = np.random.choice([1, 2, 3], size=size)

        # Randomized Quicksort Timing
        print("Randomized Quicksort:")
        for arr in [arr_random, arr_sorted, arr_reverse, arr_repeated]:
            arr_copy = arr.copy()
            start = time.time()
            randomized_quicksort(arr_copy, 0, len(arr_copy) - 1)
            print(f"Time taken: {time.time() - start:.6f} seconds")

        # Iterative Deterministic Quicksort Timing (First Element as Pivot)
        print("Iterative Deterministic Quicksort (First Element as Pivot):")
        for arr in [arr_random, arr_sorted, arr_reverse, arr_repeated]:
            arr_copy = arr.copy()
            start = time.time()
            deterministic_quicksort_iterative(arr_copy, 0, len(arr_copy) - 1)
            print(f"Time taken: {time.time() - start:.6f} seconds")

# Run the comparison
compare_algorithms()

"""Part 2: Hashing with Chaining"""

class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with the specified size."""
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_elements = 0

    def hash_function(self, key):
        """Hash function: uses simple modulo operation to compute hash."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        # Check if the key already exists, update the value if it does
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Otherwise, insert the new key-value pair
        self.table[index].append((key, value))
        self.num_elements += 1
        # Resize if load factor exceeds threshold
        if self.load_factor() > 0.75:
            self.resize()

    def search(self, key):
        """Search for a value associated with the key in the hash table."""
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.num_elements -= 1
                return True
        return False  # Key not found

    def load_factor(self):
        """Calculate the load factor of the hash table."""
        return self.num_elements / self.size

    def resize(self):
        """Resize the hash table to double its current size."""
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]
        # Rehash all key-value pairs into the new table
        for bucket in self.table:
            for key, value in bucket:
                new_index = hash(key) % new_size
                new_table[new_index].append((key, value))
        self.size = new_size
        self.table = new_table

    def display(self):
        """Display the current state of the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Example usage:
hash_table = HashTable()

# Insert key-value pairs
hash_table.insert('apple', 50)
hash_table.insert('banana', 30)
hash_table.insert('grape', 40)

# Display the hash table
hash_table.display()

# Search for keys
print("Search 'apple':", hash_table.search('apple'))  # Output: 50
print("Search 'banana':", hash_table.search('banana'))  # Output: 30

# Delete a key
hash_table.delete('banana')
hash_table.display()