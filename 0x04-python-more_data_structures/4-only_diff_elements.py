#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create a set of elements present in both sets
    common_set = set_1.intersection(set_2)

    # Create a set of elements present in only set_1
    diff_set_1 = set(filter(lambda item: item not in common_set, set_1))

    # Create a set of elements present in only set_2
    diff_set_2 = set(filter(lambda item: item not in common_set, set_2))

    # Combine the two sets of unique elements
    unique_diff_set = diff_set_1.union(diff_set_2)

    return unique_diff_set
