#A game with python

from math import *

user_hp = 10
reader_hp = 3 #Les Try possible



print ("Hello, is it you that will come with me today?")
user_name = input("What's the name of my dear reader? ")

print ("A pleasure to meet you", user_name, "! What should we do today?")
print ("Shall we go outside? See if the sea is happy today?(1) \nOr should we stay in bed?(2) ")
choice = int(input("What do you want to do? "))

if reader_hp <= 0:
    print ("You have", reader_hp, "Life Point")
    print ("Game Over...")
    
if choice == 1:
    print ("---------------- Welcome Aboard MotherTrucker ----------------")
    print("The sea look beautiful, you can see a miles away! \n The ship need some love, maybe try to give the ")

elif choice == 2 :
    print("Oh no, your bed sheet is trying to swallow you whole! \n You need to fight it! Quick! \n Punch it!(1) \n ...Or you can just say give up and give up on your productivity...(2)")
    reader_hp = 0
else:
    choice = int(input("Please enter a valid choice to start your adventure: "))