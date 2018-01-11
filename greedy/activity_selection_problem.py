"""
The activity selection problem is a combinatorial optimization problem
concerning the selection of non-conflicting activities to perform within a
given time frame, given a set of activities each marked by a start time (si)
and finish time (fi). The problem is to select the maximum number of
activities that can be performed by a single person or machine, assuming that
a person can only work on a single activity at a time.
"""


def select_max_activities(activities):
    """
    Returns a maximum list of activities that can be done by a
    single person, one at a time.

    :param activities: list of tuples containing start and finish
    ex: [(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]
    """
    activities.sort(key=lambda x: x[1])

    max_activities = []
    max_activities.append(activities[0])

    pos = 0

    for idx, val in enumerate(activities):
        if idx > pos:
            if activities[idx][0] >= activities[pos][1]:
                max_activities.append(val)
                pos = idx

    return max_activities


def main():
    """
    Running the code
    """
    activities = [(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]

    print select_max_activities(activities)


if __name__ == "__main__":
    main()
