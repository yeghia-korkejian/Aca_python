import sys

list1 = ["hello", 1, True]

print(list1)

list1.extend(sys.argv[1:])

print(list1)