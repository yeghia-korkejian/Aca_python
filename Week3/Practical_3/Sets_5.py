import argparse
set3 = {2,4,6,10,12}
parser = argparse.ArgumentParser()

parser.add_argument("x",type=int)

args = parser.parse_args()

if min(set3)< args.x and args.x<max(set3):
    print("True")
else:
    print("False")