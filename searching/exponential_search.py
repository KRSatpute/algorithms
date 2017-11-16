"""
The idea is to start with subarray size 1 compare
its last element with x, then try size 2, then 4
and so on until last element of a subarray is not
greater.
Once we find an index i (after repeated doubling of i),
we know that the element must be present between i/2
and i (Why i/2? because we could not find a greater
value in previous iteration)
"""

from binary_search import recursive_search as binary_search


def search(element_list_sorted, element):
    """
    Exponential search involves two steps:

    1. Find range where element is present
    2. Do Binary Search in above found range.
    """
    length_list = len(element_list_sorted)

    if element_list_sorted[0] == element:
        return 0

    index = 1
    while index < length_list and\
            element_list_sorted[index] <= element:
        index *= 2

    binary_search_result = binary_search(
        element_list_sorted[(index / 2): min(index, length_list)], element
        )
    return (index / 2) + binary_search_result\
        if binary_search_result != -1 else -1

# Running the code
"""
LIST_OF_ELEMS = [0, 1, 1, 2, 3, 5, 8, 13, 21,
                 34, 55, 89, 144, 233, 377, 610, 987]
print search(LIST_OF_ELEMS, 144)  # will print 12
print search(LIST_OF_ELEMS, 165415)  # will print -1
print search(LIST_OF_ELEMS, 13)  # will print 7
print search(LIST_OF_ELEMS, 987)  # will print 16
print search(LIST_OF_ELEMS, -232)  # will print -1
print search(LIST_OF_ELEMS[0:1], 0)  # will print 0
"""
