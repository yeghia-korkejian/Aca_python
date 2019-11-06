import argparse
parser = argparse.ArgumentParser()
parser.add_argument("text",
 help="Add text which is 7 or more characters long and has an odd number of characters", type=str)
args = parser.parse_args()
if len(args.text) % 2 == 0 or len(args.text) < 7 :
    print ("Add text which is 7 or more characters long and has an odd number of characters")
else:
    print("The old string: " + args.text)
    a = args.text[(len(args.text) // 2)-1 : (len(args.text) // 2)+2]
    print("Middle 3 characters: " + a)
    print("The new string: " + args.text.replace(a ,a.upper()))