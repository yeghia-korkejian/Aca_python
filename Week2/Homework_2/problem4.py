import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text" ,type=str)

args = parser.parse_args()

print("The given string: " + args.text)
print("The USA/usa count is: " + str(args.text.count("USA") + args.text.count("usa")))
a = args.text.replace("usa" , "USA")
print("The new string: " + a.replace("USA"  , "Armenia"))