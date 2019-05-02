"""
Useful for searching information in SORTED arrays / lists.
The idea of the binary search is to use the information that the data is sorted and reduce the time complexity
from O(n) in case of linear search to O(log(n)) in case of binary search.
"""

def binary_search_recursive(arr, val):
    # If the input array is empty or contains only one element which
    # is not equal to the searched value
    # return False
    if len(arr) == 0 or (len(arr) == 1 and arr[0] != val):
        return False

    # value at the middle of the array
    mid = arr[len(arr) // 2]
    if mid == val: return True
    if val < mid: return binary_search_recursive(arr[:len(arr) // 2], val)
    if val > mid: return binary_search_recursive(arr[len(arr) // 2 + 1:], val)



def binary_search_iterative(arr, val):
    # If the input array is empty or contains only one element which
    # is not equal to the searched value
    # return False

    half = arr
    found = False
    while not found:

        if len(arr) == 0 or len(half) == 0 or (len(arr) == 1 and arr[0] != val):
            return False

        mid = half[len(half) // 2]

        if val == mid:
            found = True
        elif val < mid:
            half = half[:len(half) // 2]
        elif val > mid:
            half = half[len(half) // 2 + 1:]

    return found

########################################################################################################################
# Testing the implementation of the algorithm

large_sorted_list = range(1, 100000001)
elem_to_search = 100000000
print(large_sorted_list[-1])

from timeit import default_timer as time
# Recursive
start = time()
print(f"The number {elem_to_search} is contained in the list : {binary_search_recursive(large_sorted_list, elem_to_search)}")
end = time()
print(f"Recursive version of the binary search took {end - start} to find")

# Iterative
start = time()
print(f"The number {elem_to_search} is contained in the list : {binary_search_iterative(large_sorted_list, elem_to_search)}")
end = time()
print(f"Iterative version of the binary search took {end - start} to find")


