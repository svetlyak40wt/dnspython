import sys

if sys.version > '3':
    long = int

    def cmp(a, b):
        return (a > b) - (a < b)
