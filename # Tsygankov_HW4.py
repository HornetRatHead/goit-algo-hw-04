# Tsygankov_HW4

import timeit
import random

def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def timsort(arr):
    arr.sort()
    return arr

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_sorting_time(sorting_function, data):
    setup_code = f"from __main__ import {sorting_function}"
    stmt = f"{sorting_function}({data})"
    time_taken = timeit.timeit(stmt, setup=setup_code, number=1)
    return time_taken

def compare_algorithms():
    array_sizes = {
        "20-50": random.sample(range(1, 999), random.randint(20, 50)),
        "51-200": random.sample(range(1, 999), random.randint(51, 200)),
        "201-500": random.sample(range(1, 999), random.randint(201, 500)),
        "501-999": random.sample(range(1, 999), random.randint(501, 999)),
    }

    for size_range, array in array_sizes.items():
        print(f"\nArray Size Range: {size_range}")
        print(f"Number of Values in Array: {len(array)}")

        insertion_sort_time = measure_sorting_time("insertion_sort", array.copy())
        print(f"Insertion Sort time: {insertion_sort_time:.6f} seconds")

        merge_sort_time = measure_sorting_time("merge_sort", array.copy())
        print(f"Merge Sort time: {merge_sort_time:.6f} seconds")

        timsort_time = measure_sorting_time("timsort", array.copy())
        print(f"Timsort time: {timsort_time:.6f} seconds")

if __name__ == "__main__":
    compare_algorithms()