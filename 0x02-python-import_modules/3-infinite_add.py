#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    addition = 0
    for i in range(1, n):
        addition += int(argv[i])
    print(addition)
