"""
Jump Search is a searching algorithm for sorted arrays.
The idea is to search fewer elements(than linear search) by jumping ahead by fixed steps or sipping some elements in
place of searching all the elements.

In the worst case we have to do n/m jumps and if the last checked value is greater than the element to be searched for,
we perform m-1 comparisons more for linear search. Therefore the total number of comparisons in the worst case
will be ((n/m) + m-1). The value of the function ((n/m) + m-1) will be minimum when m = sqrt(n).
Therefore, the best step size is m = sqt(n)

    __IMPORTANT POINTS___

    * Works only on sorted arrays
    * The optimal size of a block to be jumped is (sqrt(n)). This makes the time complexity of jump search O(sqrt(n))
    * The time complexity of jump search is between Linear Search O(n) and Binary Search O(log(n)).
    * Binary Search is better tha Jump Search but Jump Search has an advantage that we traverse back only once. This is
    more efficient in systems here traversing back is more costly.
"""

def jump_search(arr, val):
    # The block size to be jumped
    left_bound = 0
    right_bound = int(len(arr) ** (1/2))

    while arr[right_bound] <= val and right_bound < len(arr) - 1:

        left_bound = right_bound
        right_bound += right_bound

        if right_bound > len(arr) - 1:
            right_bound = len(arr) - 1

    for elem in arr[left_bound:right_bound + 1]:
        if elem == val:
            return True

    return False

########################################################################################################################
# Testing the implementation of the algorithm

large_sorted_list = range(1, 10000001)
elem_to_search = 10000000
print(large_sorted_list[-1])

from timeit import default_timer as time

start = time()
print(f"The number {elem_to_search} is contained in the list : {jump_search(large_sorted_list, elem_to_search)}")
end = time()
print(f"Jump search took {end - start} to find the element")
