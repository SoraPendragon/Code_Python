#A game with python

from math import *
import random

user_hp = 10    #Sailor HP
reader_hp = 3   #Tries -> chance you can restart a loop.

print ("Hello, is it you that will come with me today?")
reader_name = input("What's the name of my dear reader? ")

print ("A pleasure to meet you", reader_name, "! What should we do today?")
print ("You have", reader_hp,"try for this story")
print ("Shall we go outside? See if the sea is happy today?(1) \nOr should we stay in bed?(2) ")


while user_hp > 0 and reader_hp >= 0:
    restart_loop = False
    user_hp = 10    #Sailor HP
    choice = int(input("What do you want to do? "))
    if choice == 1:
        print ("-------------------------- A Day on a Boat --------------------------")
        print ("---------------- Or: Why did I choose this project?  ----------------")             
        print ("The sea look beautiful, you can see a miles away! \n Oh no! An Octopus is attacking the ship! \n Quick! Grab your tool, you need to defend the ship! ")
        print ("------------------------------- _____ -------------------------------")
        print ("------------------------------ /     \ ------------------------------")
        print ("------------------------------ I 0 0 I ------------------------------")
        print ("-------------------------- ___ \  w  /  ___ -------------------------")
        print ("------------------------- /   \ -- --  /   \ ------------------------")
        print ("------------------- __    I   /  /I\   \   I   __ -------------------")                 #J'ai perdu 15 Min à faire ce truc, on peut m'expliquer pourquoi?
        print ("------------------ /  \   \     / I \     /   /  \ ------------------")
        print ("------------------ \_______\___/  I  \___/_______/ ------------------")
        print ("------------------ / __     __    I    __     __ \ ------------------")
        print ("----------------- I /  \   /  \  / \  /  \   /  \ I -----------------")
        print ("------------------ \___/   \____/   \____/   \___/ ------------------")
        print ("---------------------------------------------------------------------")
        print ("You have", reader_hp,"lifes")
    elif choice == 2 :
        print("Oh no, your bed sheet is trying to swallow you whole!")
        user_hp = 0
        print (reader_name,"... I'm sorry... We can't do it")
        print ("You have", reader_hp, "try left")
        if restart_loop:
            continue
    else:
        choice = int(input("Please enter a valid choice to start your adventure: "))

    #Choix 1
    monster_hp = 5
    mon_move = {
        "Tentacle": 1,
        "Head" : 2,
        "Double Tentacle" : 4,
    }

    user_move = {
        "It's a Critical hit!" : 5,
        "You land a Normal Hit" : 2,
        "You Missed..." : 0,
    }

    while user_hp > 0 and monster_hp > 0:
        
        print ("Your turn!")
        user_attack = int(input("Attack(1) or Defend(2)! It's your choice: "))
        monster_attack = random.choice(list(mon_move))         # Choose the Attack for the Monster : Tentacule (1 dmg), Head (2 dmg), Double Tentacule (4 Dmg)
        
        if user_attack == 1 :
            print ("You punch the octopus in the face")
            user_damage = random.choice(list(user_move))
            monster_hp -= user_move[user_damage]
            print (user_damage)
            print ("the Monster use", monster_attack)
            print ("It deal",mon_move[monster_attack],"damage")
            user_hp = user_hp - mon_move[monster_attack]
        elif user_attack == 2:
            print ("You defend yourself")
            user_hp = user_hp - (mon_move[monster_attack] // 2)
        else:
            choice = int(input("Please enter a valid action"))
        
        print ("the Monster use", monster_attack)
        print ("You lose", mon_move[monster_attack],"HP")
        print ("HP left", user_hp)
        print ("The Monster has", monster_hp, "HP left")

    if user_hp >= 0 and monster_hp <= 0 :
        print ("You win!")
        print ("Time to eat your lunch!")
    else :
        print ("You loose...")
        reader_hp -= 1
        restart_loop = True
        user_hp = 10
        monster_hp = 5

    if user_hp <= 0:
        reader_hp -= 1

    if monster_hp <= 0 :
        print ("test fin boucle")
        break

    if restart_loop:
        continue

if reader_hp <= 0:
    print ("----------------------- At least you tried... -----------------------")
    print ("----------------------------- Game Over -----------------------------")


while user_hp > 0 and reader_hp > 0:
    restart_loop = False
    print ("You had a good fight try to remember it for the rest of the day")
    print ("It's time to wash the ")

    if restart_loop:
        continue