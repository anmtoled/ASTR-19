#Anna Toledo
#Journal One Prompt Three

#Create function f(x) that returns x**3 + 8.
#In main, call f(x) with x = 9 and print result
#Create if statement that executues if result is larger than 27, and prints "YAY!"

#returns the equation below
def f(x):
	return (x**3 + 8)
	
#main will set variable x to 9, then print return statement of f(x)
#main has if statement that will print YAY if f(x) is larger than 27
def main():
	x = 9
	print(f(x))
	if f(x) > 27:
		print("YAY!")

if __name__ == '__main__':
	main()