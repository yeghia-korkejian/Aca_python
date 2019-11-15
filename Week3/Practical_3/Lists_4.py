import argparse

list4 =  [0, "hi", 2, 100, 300, 2, 2]

print("list4 = " , list4)

parser = argparse.ArgumentParser()

parser.add_argument("x", help="WOW" , type=int)

args = parser.parse_args()

list4.remove(args.x)
print (list4)