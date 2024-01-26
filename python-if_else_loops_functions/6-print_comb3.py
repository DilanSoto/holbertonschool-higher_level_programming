#!/usr/bin/python3
for n in range(0, 9):
    for m in range(n + 1, 10):
        if n < 8:
            print("{:02d}".format(n * 10 + m), end=", ")
        else:
            print("{:02d}".format(n * 10 + m))
