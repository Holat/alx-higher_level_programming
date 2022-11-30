#!/usr/bin/python3
def pow(a, b):
    for i in range(1, b + 1):
        a *= a
    return (a)
print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
