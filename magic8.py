#Making a Magic 8 Ball 

import random

question = input("Question: ")

mag = random.randint(1,9)

#print ("Magic 8 Ball :", mag)

if mag == 1:
    print ("Yes - definitely.")
elif mag == 2:
    print ("It is decidedly so.")
elif mag == 3:
    print ("Without a doubt.")
elif mag == 4:
    print("Reply hazy, try again.")
elif mag == 5:
    print("Ask again later.")
elif mag == 6:
    print ("Better not tell you now.")
elif mag == 7:
    print ("My sources say no.")
elif mag == 8:
    print ("Outlook not so good.")
else:
    print("Very doubtful.")

