#A game with python

from math import *
import random

user_hp = 10    #HP du perso
reader_hp = 3   #Les Try possibles

print ("Hello, is it you that will come with me today?")
reader_name = input("What's the name of my dear reader? ")

print ("A pleasure to meet you", reader_name, "! What should we do today?")
print ("Shall we go outside? See if the sea is happy today?(1) \nOr should we stay in bed?(2) ")
choice = int(input("What do you want to do? "))

if reader_hp <= 0:
    print ("You have", reader_hp, "Try left")
    print ("Game Over...")
    
if choice == 1:
    print ("-------------------------- A Day on a Boat --------------------------")
    print ("---------------- Or: Why did I choose this project?  ----------------")
    print ("The sea look beautiful, you can see a miles away! \n The ship need some love, maybe try to wash the deck?(1)\n Oh I know! We can go fish our lunch!(2) ")
    print ("I have", user_hp,"HP")
    print ("You can try ", reader_hp,"times")
elif choice == 2 :
    print("Oh no, your bed sheet is trying to swallow you whole!")
    reader_hp = 0
    print (reader_name,"... I'm sorry... We can't do it")
    reader_hp = reader_hp - 1
else:
    choice = int(input("Please enter a valid choice to start your adventure: "))