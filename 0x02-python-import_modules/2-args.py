#!/usr/bin/python3
import sys

# Getting rid of the 0 number  argument
num_arguments = len(sys.argv) - 1

# Check the no of  arguments
if num_arguments == 0:
    print(f"0  arguments.")
elif num_arguments == 1:
    print(f"1 argument:")
else:
    print(f"{num_arguments} arguments:")

# Print the argument with its position
for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
