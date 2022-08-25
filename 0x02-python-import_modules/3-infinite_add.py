#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    argmnts = sys.argv[0]

    for i in sys.argv:
        if argmnts != i:
            result += int(i)
            print(result)
