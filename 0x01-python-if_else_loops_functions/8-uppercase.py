#!/usr/bin/pythoon 3 
def uppercase(s):
    output = ""
    for char in s:
        if 'a' <= char <= 'z':
            output += chr(ord(char) - 32)
        else:
            output += char
    print(output)
