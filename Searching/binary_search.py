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


def iterative_search(elements_list_sorted, element):
    """
    Iterative Binary Search Function
    It returns location of x in given array arr if present,
    else returns -1
    """
    index_start = 0
    index_last = len(elements_list_sorted) - 1

    while index_start <= index_last:

        index_mid = index_start + (index_last - index_start) / 2

        if elements_list_sorted[index_mid] == element:
            # Check if element is present at mid
            return index_mid
        elif elements_list_sorted[index_mid] < element:
            # If element is greater, ignore left half
            index_start = index_mid + 1
        else:
            # If element is smaller, ignore right half
            index_last = index_mid - 1

    # If we reach here, then the element was not present
    return -1


def recursive_search(element_list_sorted, element):
    """
    Recursive Binary Search Function
    It returns location of x in given array arr if present,
    else returns -1
    """
    length_list = len(element_list_sorted)
    index_start = 0
    index_last = length_list - 1

    index_select = 0

    index_mid = index_start + (index_last - index_start) / 2

    if length_list == 1:
        if element_list_sorted[0] == element:
            index_select = 0
        else:
            index_select = -1

    if length_list == 2:
        if element_list_sorted[0] == element:
            index_select = 0
        elif element_list_sorted[1] == element:
            index_select = 1
        else:
            index_select = -1
    else:
        if element_list_sorted[index_mid] == element:
            # Check if element is present at mid
            index_select = index_mid
        elif element_list_sorted[index_mid] < element:
            # If element is greater, ignore left half
            # Beware we are shifting the start position
            # in the upcoming recursive call

            index = recursive_search(
                element_list_sorted[index_mid + 1:], element
            )

            index_select = (index_mid + 1) + index if index != -1 else -1
        else:
            # If element is smaller, ignore right half
            index_select = recursive_search(
                element_list_sorted[: index_mid], element
            )

    return index_select

# Running the code

LIST_OF_ELEMS = [2, 3, 4, 10, 40, 44, 45, 89, 101, 112, 178, 205]
"""
print iterative_search(LIST_OF_ELEMS, 101)  # will print 8
print iterative_search(LIST_OF_ELEMS, 300)  # will print -1
print iterative_search(LIST_OF_ELEMS, -254645)  # will print -1
print iterative_search(LIST_OF_ELEMS, 2)  # will print 0
print recursive_search(LIST_OF_ELEMS, 178)  # will print 10
print recursive_search(LIST_OF_ELEMS, 1616164)  # will print -1
print recursive_search(LIST_OF_ELEMS, 10)  # will print 3
print recursive_search(LIST_OF_ELEMS[0:2], -8451854)  # will print -1
"""
