#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        my_list = []

    c = 0
        try:
            for i in range(x):
                if type(my_list[i]) == int:
                    print("{:d}".format(my_list=[i]), end="")
                    c += 1
    except IndexError:
        pass
    print()
    return c
