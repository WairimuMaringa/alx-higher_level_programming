#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    args = len(sys.argv)

    for x in range(1, args):
        result += int(sys.argv[x])

        print("{:d}".format(result))
