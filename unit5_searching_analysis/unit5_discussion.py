"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time
import random

def linear_search(lst, target):
    """
    Time complexity: O(n)
    - In the worst case (target is the last element, or not in
      the list at all), we must check every single element.
    - There's no way to skip ahead, because we don't know the
      list is sorted (or even if it is, linear search ignores
      that fact) — so work grows in direct proportion (1:1)
      to the size of the list, n.
    """
    for i in range (len(lst)):  # walks every index pos, 0 to n-1
        if lst[i] == target:    # found, then stop and return index
            return i
    return -1   # ran off the end without a match


def binary_search(lst, target):
    """
    Binary search: assumes the list is already SORTED, and
    repeatedly cuts the remaining search space in half by
    comparing the target to the middle element.

    Time complexity: O(log n)
    - Each comparison eliminates HALF of the remaining elements,
      not just one. So instead of n steps, we need roughly
      log2(n) steps.
    """
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target: return mid   # middle is target
        elif lst[mid] < target: low = mid + 1   # target must be to right: discard left half
        else: high = mid - 1    # target must be to the left: discard right half

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    small_data = list(range(1, 21)) # sorted list from 1-20

    print("\n=== SMALL DATASET TEST ===")
    print(f"Dataset: {small_data}")

    target = 14
    # Both correctly find 14 at index 13. On a list this small, the diff in speed
    # between the 2 algorithms is not noticeable, both run in a fraction of a millisec
    print(f"linear_search: {target}) -> index {linear_search(small_data, target)}")
    print(f"binary_search: {target}) -> index {binary_search(small_data, target)}")

    target = 69
    # both return -1. Linear search had to check all 20 elements before giving up
    # binary search only needed a handful of comparisons because it kept cutting the
    # remaining range in half
    print(f"linear_search: {target}) -> index {linear_search(small_data, target)}")
    print(f"binary_search: {target}) -> index {binary_search(small_data, target)}")


    # ===============================
    # LARGE DATASET
    # ===============================
    large_data = list(range(0, 2_000_000, 2)) # 1000k sorted even #s

    print("\n=== LARGE DATASET TEST ===")
    print(f"Dataset: {len(large_data)} elements")

    target = 1_999_998  # near the end of the list (worst case for linear search)
    start = time.perf_counter()
    result_linear = linear_search(large_data, target)
    time_linear = time.perf_counter() - start

    start = time.perf_counter()
    result_binary = binary_search(large_data, target)
    time_binary = time.perf_counter() - start

    print(f"linear_search found index {result_linear} in {time_linear:.6f} seconds")
    print(f"binary_search found index {result_binary} in {time_binary:.6f} seconds")
    # As the dataset grows from 20-1000k elements, linear searches runtime grows right
    # along with (0(n)), here it has to scan nearly the whole list because the target is
    # near the end.
    # ==============================================
    # Binary search's run barely changes at all (0(log n)) because doubling n only costs
    # it one extra comparison. This gap is why binary search is much more efficient on large
    # sorted data

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # Edge case #1: Empty list
    # Both immediately return -1. Linear search's loop never executes (range(0) is empty).
    # Binary search starts with low=0, high=1, so low <= high is False right away and the
    # loop never runs either
    empty_list = []
    print(f"Empty list -> linear: {linear_search(empty_list, 5)}, "
          f"binary: {binary_search(empty_list, 5)}")

    # Edge case #2: singe-element list, value present
    # Both return 0. This is the smallest case where a math is possible
    one_item = [7]
    print(f"Single-element list (present) -> linear: {linear_search(one_item, 7)}, "
          f"binary: {binary_search(one_item, 7)}")

    # Edge case #3: value at the very first position
    # Linear search finds it instantly (best case, 0(1) in practice)
    # Binary search takes a few extra steps to narrow down to index 0, since it always
    # starts by checking the middle, not the front
    print(f"Value at first position -> linear: {linear_search(small_data, 1)}, "
          f"binary: {binary_search(small_data, 1)}")

    # Edge case #4: value at the very last position
    # Linear search's worst case. It must check every element before reaching the last one
    # Binary is unaffected by position; it only cares about value relative to the midpoint,
    # so it still finishes in ~log2(n) steps
    print(f"Value at last position -> linear: {linear_search(small_data, 20)}, "
          f"binary: {binary_search(small_data, 20)}")

    # ===============================
    # REAL-WORLD SEARCH SCENARIO
    # ===============================
    print("\n=== REAL-WORLD SCENARIO ===")
    # A sorted phone directory: rep looks up one account number.
    phone_directory = sorted(random.sample(range(10_000_000, 99_999_999), 100_000))
    lookup_number = phone_directory[-1]   # worst case: last entry

    t_linear = -time.perf_counter(); linear_search(phone_directory, lookup_number); t_linear += time.perf_counter()
    t_binary = -time.perf_counter(); binary_search(phone_directory, lookup_number); t_binary += time.perf_counter()

    print(f"{len(phone_directory)} records -> linear: {t_linear:.6f}s, binary: {t_binary:.6f}s")
    # Sorted data + binary search = near-instant lookups at any scale.

if __name__ == "__main__":
    main()