"""
The linear search is rarely used practically because other search algorithms such as the binary search algorithm and
hash tables allow significantly faster searching in comparison to linear search.

The time complexity of linear search is equal to O(n)
"""


def linear_search(arr, val):
    for item in arr:
        if item == val:
            return True
    return False


########################################################################################################################
# Testing the implementation of the algorithm

large_sorted_list = range(1, 100000001)
elem_to_search = 100000000
print(large_sorted_list[-1])

from timeit import default_timer as time

start = time()
print(f"The number {elem_to_search} is contained in the list : {linear_search(large_sorted_list, elem_to_search)}")
end = time()
print(f"Recursive version of the binary search took {end - start} to find")
