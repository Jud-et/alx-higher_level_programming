#!/usr/bin/python3
#import the module
from calculator_1 import add, sub, div, mul
if __name__ == '__main__':
        #define variables
        a = 10
        b = 5
        print("{} + {} = {}".format(a, b, add(a, b)))
        print("{} - {} = {}".format(a, b, sub(a, b)))
        print("{} * {} = {}".format(a, b, mul(a, b)))
        print("{} / {} = {}".format(a, b, div(a, b)))
