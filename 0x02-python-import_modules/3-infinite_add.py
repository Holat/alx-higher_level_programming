#!/usr/bin/python3
from sys import argv
aSum = 0
for i in range(1, len(argv)):
    aSum += int(argv[i])
print(aSum)
