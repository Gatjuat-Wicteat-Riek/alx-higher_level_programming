#!/usr/bin/bash/python3
if __name__ == "__main__":
    """Print the addition of all the arguments"""
    import sys
    numTotal = 0
    for i in range(len(sys.argv) - 1):
        numtotal += int(sys.argv[i + 1])
    print("{}".format(numtotal))
