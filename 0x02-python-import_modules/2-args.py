#!/usr/bin/python3
if __name__ == "__main__":
    import sys

<<<<<<< HEAD
count = len(sys.argv) - 1
if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))
for i in range(count):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
=======
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
>>>>>>> c007f23f604fade8bdf498a5b77e5d24ac796d9f
