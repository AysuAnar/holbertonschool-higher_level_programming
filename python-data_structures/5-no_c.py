#!/usr/bin/python3
def no_c(my_string):
    removing = "c"
    new_one = ""
    for char in my_string:
        if char.lower() not in removing.lower():
            new_one += char
    return new_one
