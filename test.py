import random
import time
from quicksort import randomized_quicksort, deterministic_quicksort
from hash_table import HashTable


def test_quicksort():
    sizes = [1000, 3000, 5000]

    for size in sizes:
        print(f"\nArray Size: {size}")

        arr = [random.randint(0, 10000) for _ in range(size)]
        sorted_arr = sorted(arr)
        reverse_arr = sorted(arr, reverse=True)
        repeated_arr = [5] * size

        datasets = {
            "Random": arr,
            "Sorted": sorted_arr,
            "Reverse": reverse_arr,
            "Repeated": repeated_arr
        }

        for name, data in datasets.items():
            print(f"\n{name} Data:")

            start = time.time()
            randomized_quicksort(data.copy())
            print("Randomized QS Time:", time.time() - start)

            try:
                start = time.time()
                deterministic_quicksort(data.copy())
                print("Deterministic QS Time:", time.time() - start)
            except RecursionError:
                print("Deterministic QS Time: FAILED (Recursion Error)")


def test_hash_table():
    print("\n--- Hash Table Test ---")

    ht = HashTable(10)

    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)

    print("Search apple:", ht.search("apple"))

    ht.delete("banana")
    print("Search banana:", ht.search("banana"))


if __name__ == "__main__":
    test_quicksort()
    test_hash_table()