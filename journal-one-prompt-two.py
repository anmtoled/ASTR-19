#Anna Toledo
#Session Two Prompt
#Credit to https://stackoverflow.com/questions/13872049/print-empty-line for ...
#...reminding me that print() will create a blank line, to keep return statement clean

#Print sum of two floating point numbers
#Print difference between two integers
#Print product of floating point number and integer

#Each case, program prints out data type of resulting answer

#Prints sum of two floating point numbers
def TwoFloatPoint():
	x = float(1.6)
	y = float(56.8)
	c = x+y
	print(x,"+",y,"=",c)
	print('The number',c, 'has a data type of ',type(c))

#Prints difference between two integers
def IntegerDifference():
	x = int(12)
	y = int(5)
	c = x-y
	print(x,"-",y,"=",c)
	print('The number',c, 'has a data type of ',type(c))

def FloatAndInteger():
	x = float(24.89)
	y = int(54)
	c = x * y
	print(x,"*",y,"=",c)
	print('The number',c, 'has a data type of ',type(c))


def main():
	TwoFloatPoint()
	print()
	IntegerDifference()
	print()
	FloatAndInteger()

if __name__ == '__main__':
	main()
