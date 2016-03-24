#Assignment: (Homework 4) 
# 
#Description: (Square and Circle Generator) 
# www
#Author: (Robert Crismon) 
# 
#Completion Time: (2-3 hours) 
# 
#In completing this program, I obtained help or worked with the following: 
#(Help was acquired from the python.org website on turtle commands)

from turtle import *
from random import *

#--------------------------------------------------------

user_input_1 = 0
user_input_2 = 0

print("***Turtle Graphics Shape Generator***")
print("1. Draw squares")
print("2. Draw circles")
user_input_1 = input("Selection: ")
user_input_1 = int(user_input_1)


if user_input_1 == 1:
	x = 0
	user_input_2 = input("Enter the number of squares to draw: ")
	user_input_2 = int(user_input_2)
	x = input("Enter square width: ")
	x = int(x)
	counter = 0
	while counter < user_input_2:
		#begin drawing square
		forward(x)
		left(90)
		forward(x)
		left(90)
		forward(x)
		left(90)
		forward(x)
		left(80)
			
		counter = counter + 1
		
elif user_input_1 == 2:
	x = 0
	y = 0
	counter = 0
	user_input_2 = input("Enter the number of circles to draw: ")
	user_input_2 = int(user_input_2)
	x = input("Enter initial circle radius: ")
	x = int(x)
		
	while counter < user_input_2:
		#begin drawing circle
		circle(x)
		counter = counter + 1
		x = x + 20
		y = y - 20
		penup()
		goto(0, y)
		pendown()
