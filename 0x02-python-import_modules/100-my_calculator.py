#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    len_args = len(sys.argv)
    if len_args != 4:
        print("Usage: {0} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        if op == "+":
            print("{} + {} = {}".format(a, b, calc.add(a, b)))
        elif op == "-":
            print("{} - {} = {}".format(a, b, calc.sub(a, b)))
        elif op == "*":
            print("{} * {} = {}".format(a, b, calc.mul(a, b)))
        elif op == "/":
            print("{} / {} = {}".format(a, b, calc.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
