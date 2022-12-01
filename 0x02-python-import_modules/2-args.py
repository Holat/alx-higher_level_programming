#!/usr/bin/python3
from sys import argv
length = len(argv)
print(f'{length - 1} {"argument." if length == 1 else "arguments:"}')

for i in range(1,length):
    print(f'{i}: {argv[i]}')
