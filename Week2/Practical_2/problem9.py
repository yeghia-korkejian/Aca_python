import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="some text", type=str)

parser.add_argument("start_index", help="display a square of a given number",type=int)

parser.add_argument("end_index", help="display a square of a given number",type=int)

args = parser.parse_args()

print("The given text:" , args.text)
print("Start index:" , args.start_index)
print("End index:" , args.end_index)
print(args.text[args.start_index:args.end_index])