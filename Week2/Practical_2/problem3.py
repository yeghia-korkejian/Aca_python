import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="display a name of a given number", type=str)
args = parser.parse_args()
print ("Welcome,", args.name,"!")