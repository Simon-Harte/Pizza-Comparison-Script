import math
from decimal import *
from os import system, name
from time import sleep
#import pyinputplus as pyip

# defining the pizza class
class Pizza:

	# constructor for pizza class.
	# takes diameter argument
	def __init__(self, diameter):
		self.diameter = diameter
		
	# returns the area of the pizza
	def area(self):
		radius = self.diameter / 2
		return math.pi * radius**2
		

# used when only one pizza is being ordered
def onePizza():
    	
	people = int(input('\nHow many of you are there?\n'))
	
	diameter = float(input('\nHow wide is your pizza in inches?\n'))
	
	pizza1 = Pizza(diameter)
	print()
	print('\n\tThe pizza has an area of\n\n\t% l3.2f in^2.\n\tYou each get \n\n\t% 3.2f in^2 of pizza.\n' % (pizza1.area(), (pizza1.area() / people)))

# this method takes the amount of people, and a string representing the size of the pizza, and calculates and returns how much pizza each person would get
def pizzaPerPerson(people, size):
    	
    pizzaNumber = int(input('\nHow many ' + size + ' pizzas are there?\n'))
    diameter = float(input('\nHow wide are the pizzas in inches?\n'))
    pizza = Pizza(diameter)
    totalPizzaArea = pizza.area() * pizzaNumber
    pizzaPerPerson = totalPizzaArea / people
    return pizzaPerPerson

	

# used when two or more pizzas are being ordered.
# can be used to compare pizzas of different sizes	
def comparePizza():
	people = int(input('\nHow many of you are there?\n'))
	
	smallPizzaPerPerson = pizzaPerPerson(people, "small")
	
	largePizzaPerPerson = pizzaPerPerson(people, "large")
	
	if smallPizzaPerPerson > largePizzaPerPerson:
		print('\nYou are better off getting a smaller pizzas!\n\nYou will each get\n\n\t% 3.2f in^2.\n\nIf you shared large pizzas, you would recieve only \n\n\t% 3.2f in^2.\n' % (smallPizzaPerPerson, largePizzaPerPerson))
	elif smallPizzaPerPerson < largePizzaPerPerson:
		print('\nYou should share a large pizza!\n\nSharing large pizzas nets you each\n\n\t% 3.2f in^2\n\nIf you got small pizzas, you would each only get\n\n\t% 3.2f in^2\n\n' % (largePizzaPerPerson, smallPizzaPerPerson))

# the main method
def main():
	print('Welcome to the Pizza Area Calculator!\n')
	sleep(2)
	while True:
		choice = int(input('\nDo you want to get the area of one pizza or compare larger pizzas with smaller ones?\n\n\t1. Just one, please\n\n\t2. Id like to compare, please.\n\n\t3. Exit\n\n'))
	
		if choice == 1:
			onePizza()
			choice2 = input('Do you want to compare again? (Y/N)')
			if choice2 == 'N' or choice == 'n':
				break
		elif choice == 2:
			comparePizza()
			choice2 = input('Do you want to compare again? (Y/N)')
			if choice2 == 'N' or choice == 'n':
				break
		elif choice == 3:
			break
		
	print('\nBye!')
	
if __name__ == "__main__":
	main()
