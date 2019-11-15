import argparse

set1 = {1, 2, 3, 4, 5, 6}

print(set1)

parser = argparse.ArgumentParser()

parser.add_argument("x",type=int)

args = parser.parse_args()

set1.add(args.x)

print(set1)