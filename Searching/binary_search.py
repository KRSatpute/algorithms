"""
Search a sorted array by repeatedly dividing the
search interval in half. Begin with an interval
covering the whole array. If the value of the
search key is less than the item in the middle of
the interval, narrow the interval to the lower
half. Otherwise narrow it to the upper half.
Repeatedly check until the value is found or the
interval is empty.

"""


def iterative_search(sorted_list_of_elems, element):
    """
    Iterative Binary Search Function
    It returns location of x in given array arr if present,
    else returns -1
    """
    start_index = 0
    last_index = len(sorted_list_of_elems) - 1

    while start_index <= last_index:

        mid_index = start_index + (last_index - start_index) / 2

        if sorted_list_of_elems[mid_index] == element:
            # Check if element is present at mid
            return mid_index
        elif sorted_list_of_elems[mid_index] < element:
            # If x is greater, ignore left half
            start_index = mid_index + 1
        else:
            # If x is smaller, ignore right half
            last_index = mid_index - 1

    # If we reach here, then the element was not present
    return -1


def recursive_search(sorted_list_of_elems, element):
    """
    Recursive Binary Search Function
    It returns location of x in given array arr if present,
    else returns -1
    """
    start_index = 0
    last_index = len(sorted_list_of_elems) - 1

    mid_index = start_index + (last_index - start_index) / 2

    if mid_index == 0 and sorted_list_of_elems[mid_index] != element:
        return -1

    if sorted_list_of_elems[mid_index] == element:
        # Check if element is present at mid
        return mid_index
    elif sorted_list_of_elems[mid_index] < element:
        # If element is greater, ignore left half
        # Beware we are shifting the start position
        # in the upcoming recursive call

        index = recursive_search(
            sorted_list_of_elems[mid_index + 1:], element
        )

        return (mid_index + 1) + index if index != -1 else -1
    else:
        # If element is smaller, ignore right half
        return recursive_search(
            sorted_list_of_elems[: mid_index], element
        )

    # If we reach here, then the element was not present
    return -1

# Running the code
"""
LIST_OF_ELEMS = [2, 3, 4, 10, 40, 44, 45, 89, 101, 112, 178, 205]

print iterative_search(LIST_OF_ELEMS, 101)  # will print 8
print iterative_search(LIST_OF_ELEMS, 300)  # will print -1
print iterative_search(LIST_OF_ELEMS, 1)  # will print -1
print iterative_search(LIST_OF_ELEMS, 2)  # will print 0

print recursive_search(LIST_OF_ELEMS, 101)  # will print 8
print recursive_search(LIST_OF_ELEMS, 300)  # will print -1
print recursive_search(LIST_OF_ELEMS, 1)  # will print -1
print recursive_search(LIST_OF_ELEMS, 2)  # will print 0
"""
