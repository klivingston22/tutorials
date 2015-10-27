print("Welcome to guess the number")
number=10
guess=int(raw_input("enter a guess"))

if guess < number :
	print "Guess too low"
elif guess > number :
	print "Guess too high"
else :
	print "Guess Correct"
