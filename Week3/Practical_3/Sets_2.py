import argparse

set2 = {1, 2, 3, 4, 5, 6}

print(set2)

parser = argparse.ArgumentParser()

parser.add_argument("x",type=int)

args = parser.parse_args()

set2.remove(args.x)

print(set2)