"""
If X and Y are 2 arrays of same length such that X[i] corresponds to Y[i] then
reorder X based on Y after Y is sorted
"""


def re_order(arr, arr_to_sort):
    """
    Reorder arr based on arr_to_sort
    when arr_to_sort is sorted
    """
    corresponds = zip(*sorted(zip(arr_to_sort, arr)))  # ask what does * do?
    corresponds.reverse()
    return corresponds


def main():
    """
    Running the code
    """
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    arr_to_sort = [0, 1, 1, 0, 1, 2, 2, 0, 1]

    reordered_arr = re_order(arr, arr_to_sort)

    print reordered_arr[0]
    print reordered_arr[1]

    arr = [5, 1, 3, 0, 5, 8]
    arr_to_sort = [9, 2, 4, 6, 7, 9]

    reordered_arr = re_order(arr, arr_to_sort)

    print reordered_arr[0]
    print reordered_arr[1]

if __name__ == "__main__":
    main()
