import argparse

def add(x,y):
	return x+y

parser = argparse.ArgumentParser()
parser.add_argument("-x", help="first argument", type=int) #add an optional argument using - will make it non positional
parser.add_argument("-y", help="second argument", type=int, required=True)

args = parser.parse_args()

if __name__ == "__main__":
	pass
	#print(args)
	#print(args.x)
	print(add(args.x, args.y))
