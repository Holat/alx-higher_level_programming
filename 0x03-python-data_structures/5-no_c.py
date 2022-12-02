#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if ord(i) == 67 or ord(i) == 99:
            i = chr(32)

    return my_string
