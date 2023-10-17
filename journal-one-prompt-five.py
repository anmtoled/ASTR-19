#Anna Toledo
#Journal One prompy five

#Reference to lectures, ASTR Python handout #2, and W3schools for the right stack function.
#link:https://www.w3schools.com/python/numpy/numpy_array_join.asp#:~:text=Joining%20NumPy%20Arrays&text=In%20SQL%20we%20join%20tables,it%20is%20taken%20as%200.

#write out a table of the function sin(x)
# where x is tabulated between 0 and 2pi with a thousand entries
#follow basic Python structure, including a main program function.

import numpy as np

def main():

	#create an array with a thousand entries between 0 and 2pi
	x = np.linspace(0,2*np.pi, 1000)
	#create copy of original array that we will add sin(x) to
	y = x.copy()
	#update y so that way it is now sin(y)
	y = np.sin(y)

	#create new array that has the two lists stacked and vertical.
	z = np.stack((y,x), axis=1)

	#print statement
	print("Below is a table where x is between 0 and 2pi.")
	print("Sin(x) vs. x")
	print(z)

if __name__ == '__main__':
	main()
