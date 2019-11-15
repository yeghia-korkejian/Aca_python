import argparse
dict1 = {"key1":"value1","key2":"value2","key3":"value3"}
print (dict1)

parser = argparse.ArgumentParser()

parser.add_argument("key",type=str)
parser.add_argument("value",type=str)

args = parser.parse_args()

dict1[args.key] = args.value
print (dict1)