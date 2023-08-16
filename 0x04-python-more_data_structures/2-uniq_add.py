#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_set = set()

    # Iterate through the elements in the list
    for num in my_list:
        unique_set.add(num)

    # Calculate the sum of unique integers
    sum_unique = sum(unique_set)

    return sum_unique
