#Anna Toledo
#Journal One prompt Four
#Declare a class describing my favorite animal
#data members represent the following physical parameters
# -Length of the arms (float) 3.75 feet
# -Number of eyes (int) 2 
# -Does it have a tail? (bool) yes
# -Is it furry? (bool) yes

#write initialization function that sets the values of the data members
# when an instance of the class is created.

#write a member function of the class to print out and describe the data members 
# describing the phyiscal characteristics of the animal. 

#class tiger

class Tiger:
	#my animal class

	#set the default information
	def __init__(self, armlength=3.75,eyenum=2,tail=True,furry=True):
		self.armlength=armlength
		self.eyenum=eyenum
		self.tail=tail
		self.furry=furry

	#print here.
	def print(self):
		print("This is a tiger!")
		print(f"Length of arms in feet = {self.armlength}")
		print(f"Number of eyes = {self.eyenum}")
		print(f"Tigers have a tail, true or false? = {self.tail}")
		print(f"Tigers are furry, true or false? = {self.furry}")


#main function
def main():

	#set default number for armlength, num of eyes, tail, and furry
	armlength=3.75
	eyenum=2
	tail=True
	furry=True

	#initialize the object and sets all of them to the default.
	new = Tiger(armlength=armlength,eyenum=eyenum,tail=tail,furry=furry)
	#runs class command print, which prints the above script.
	new.print()

#run the program.
if __name__ == '__main__':
	main()