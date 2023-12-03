#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    n = len(sys.argv)

    if n == 1:
        print(str(n - 1) + " arguments.")
    else:
        if n == 2:
            print(str(n - 1) + " argument:")
            print("1: ", sys.argv[1])
        else:
            print(str(n - 1) + " arguments:")
            for i in range(1, n):
                p = str(i)
                print(p + ": ", sys.argv[i])
