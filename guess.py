from random import randint 

def getRandomNumber ():
	return (randint(0,100)) 


def askUser ():
	num = raw_input("Give me a number: ")
	return int(num)

def compGetNum ():
	return (randint(0,100))

count = 1
correct = False

print "Welcome to the guessing game.  Try to pick a number between 1 and 100 before the computer does"
answer = getRandomNumber()
print answer
while correct != True:
	guess = askUser()
	compGuess = compGetNum()
	if guess < answer:
		print "Your guess of %s is too low" % guess
		count = count + 1
	elif guess > answer:
		print "Your guess of %s is too high" % guess
		count = count + 1
	else:
		print "Correct!  %s was the number and it took you %s guesses" % (guess, count)
		correct = True