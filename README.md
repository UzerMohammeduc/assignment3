
# Hash Table and Quicksort Algorithms Comparison

## Introduction:
This Python code provides two main functionalities:
1. A **Hash Table** implementation that stores key-value pairs and handles collisions using **chaining**.
2. A comparison between **Randomized Quicksort** and **Iterative Deterministic Quicksort** algorithms to assess their performance on different types of arrays and sizes.

The hash table offers fast insertion, search, and deletion of key-value pairs, while the sorting algorithms allow you to observe how different quicksort strategies perform under various conditions.

## Part 1: Hash Table Implementation

This part of the code implements a hash table where data is stored in key-value pairs. The hash table uses lists (or "buckets") to handle multiple entries that may map to the same index (collisions). It also automatically resizes when necessary to keep performance efficient.

### Features:
- **Insert:** Adds a new key-value pair or updates the value for an existing key.
- **Search:** Retrieves the value associated with a given key.
- **Delete:** Removes a key-value pair from the table.
- **Resize:** Automatically doubles the size of the table when it becomes too full.
- **Load Factor:** Measures how full the hash table is.
- **Display:** Prints the current state of the hash table.

### Example Usage:
```python
hash_table = HashTable()
hash_table.insert('apple', 50)
hash_table.insert('banana', 30)
hash_table.insert('grape', 40)
hash_table.display()

print("Search 'apple':", hash_table.search('apple'))
hash_table.delete('banana')
hash_table.display()
```

### Output:
```
Bucket 0: []
Bucket 1: []
Bucket 2: [('banana', 30)]
Bucket 6: [('apple', 50)]
Bucket 9: [('grape', 40)]
Search 'apple': 50
Bucket 0: []
Bucket 1: []
Bucket 2: []
Bucket 6: [('apple', 50)]
Bucket 9: [('grape', 40)]
```

## Part 2: Quicksort Algorithms Comparison

This part compares two sorting algorithms—**Randomized Quicksort** and **Iterative Deterministic Quicksort**. The performance is measured based on different input types, including random arrays, sorted arrays, reverse-sorted arrays, and arrays with repeated elements.

### Key Algorithms:
1. **Randomized Quicksort**: The pivot element is chosen randomly to avoid worst-case scenarios like already sorted arrays.
2. **Iterative Deterministic Quicksort**: Uses the first element as the pivot but is iterative to prevent deep recursion issues.

### Features:
- **Sorting Arrays:** Compares the speed of both algorithms on arrays of size 100, 500, and 1000 with different data distributions.
- **Display Timing:** Shows the time taken by each algorithm for each array size and type.

### Example Usage:
```python
compare_algorithms()
```

### Sample Output:
```
Array size: 100
Randomized Quicksort:
Time taken: 0.000958 seconds
...
Iterative Deterministic Quicksort (First Element as Pivot):
Time taken: 0.000644 seconds
...
```

## Dependencies:
- **Python 3.x**: This code is written for Python 3.x and does not require any external libraries.
