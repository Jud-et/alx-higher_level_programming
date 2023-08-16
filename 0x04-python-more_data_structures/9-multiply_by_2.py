#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    new_dictionary = a_dictionary.copy()
     # Iterate through the key-value pairs in the input dictionary
    for value in new_dictionary:
        new_dictionary[value] *= 2
    return new_dictionary
