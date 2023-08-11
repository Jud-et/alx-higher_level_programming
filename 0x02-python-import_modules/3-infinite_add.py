#!/usr/bin/python3
import sys

if __name__ == '__main__':
    # Initialize the sum to 0
    sum_result = 0

    # Loop through each argument and add it to the sum
    for arg in sys.argv[1:]:
        sum_result += int(arg)

    # Print the sum result followed by a new line
    print(sum_result)
