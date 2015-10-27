import sys
import random

 
ans = True





while ans:

	question = raw_input("Ask the magic 9 ball a question: (type quit to quit the program) ")


	

	answers = random.randint(1,9)


    
	if question == "quit":

		sys.exit()

	
	
	elif answers == 1:

		print "Good stuff"


	elif answers == 2:

		print "Outlook bad"

	
	elif answers == 3:

		print "Keep Going"


	elif answers == 4:

		print "Almost there"


	elif answers == 5:

		print "Hello"


	elif answers == 6:

		print "Don't stop now"

	
	elif answers == 7:

		print "My reply is no"


	elif answers == 8:

		print "My sources say no"

	elif answers == 9:

		print "The final number"
