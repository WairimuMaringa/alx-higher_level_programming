#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv) - 1

    if len_argv == 0:
        print("{} arguments.".format(len_argv))
    elif len_argv == 1:
        print("{} argument:".format(len_argv))
    else:
        print("{} arguments:".format(len_argv))

        if len_argv >= 1:
            len_argv = 0
            for arg in sys.argv:
                if len_argv != 0:
                    print("{}: {}".format(len_argv, arg))
                    len_argv += 1
