#Guessing Game
import random
x = random.randrange(1,101)
y=0
while y<101:
	guess = int(input(' what number from 1 -100 did the computer pick?'))

	if guess == x:
		y = y+1
		print ("you got it with %d tries" %y)
		exit ()
	elif guess > x:
		y = y+1
		print("%d is too high, try again" %(guess))
	elif guess < x:
		y=y+1
		print("%d is too low, try again" %(guess))
	else: 
		print("%d is not in range" %(guess))