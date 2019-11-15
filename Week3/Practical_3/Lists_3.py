import argparse

list2 =  [0, "hi", 2, 100, 300, 2, 2]

print("list2 = " , list2)

parser = argparse.ArgumentParser()

parser.add_argument("x", help="WOW",type=int)

args = parser.parse_args()

print("Number of " + str(args.x) + "s = " + str(list2.count(args.x)))