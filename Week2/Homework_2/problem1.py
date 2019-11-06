import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("--num_y",type=int, default=0)

parser.add_argument("--num_d",type=int, default=0)

args = parser.parse_args()
a = datetime.datetime.now()
print ("Current date: " , a)
if args.num_y:
    print('Given years: ' , args.num_y)
else:
    print ('Given years: not given')
if args.num_d:
    print('Given days: ' , args.num_d)
else:
    print ('Given days: not given')
b = (args.num_y*365 + args.num_d)
c = datetime.timedelta(days = b)

print ("Final date: " , a + c)