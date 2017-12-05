"""
The activity selection problem is a combinatorial optimization problem
concerning the selection of non-conflicting activities to perform within a
given time frame, given a set of activities each marked by a start time (si)
and finish time (fi). The problem is to select the maximum number of
activities that can be performed by a single person or machine, assuming that
a person can only work on a single activity at a time.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir, "reordering"))
    )
import reordering


def select_max_activities(start, finish):
    """
    Returns a maximum set of activities that can be done by a
    single person, one at a time.

    start: An array that contains start time of all activities
    finish: An array that conatins finish time of all activities
    """
    return reordering.reorder.re_order(start, finish)


def main():
    """
    Running the code
    """
    arr = [5, 1, 3, 0, 5, 8]
    arr_to_sort = [9, 2, 4, 6, 7, 9]

    print select_max_activities(arr, arr_to_sort)

if __name__ == "__main__":
    main()
