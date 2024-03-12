#A game with python

from math import *
import random

user_hp = 10                                                                            #Sailor HP
reader_hp = 3                                                                           #Tries -> chance you can restart a loop.

print ("Hello, is it you that will come with me today?")
reader_name = input("What's the name of my dear reader? ")

user_move = {                                                                           #Pirate Attack - Random
    "It's a Critical hit!" : 5,
    "You land a Normal Hit" : 2,
    "You Missed..." : 0,
}

print ("A pleasure to meet you", reader_name, "! What should we do today?")
print ("You have", reader_hp,"try for this story")
print ("Shall we go outside? See if the sea is happy today?(1) \nOr should we stay in bed?(2) ")


while user_hp > 0 and reader_hp >= 0:                                                   #First Loop - OctoFight or BedDeath
    restart_loop = False
    user_hp = 10    #Sailor HP
    choice = int(input("What do you want to do? "))
    if choice == 1:                                                                     #Start Adventure -> OctoFight
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
    elif choice == 2 :                                                                  #Bed Death - Start Again
        print("Oh no, your bed sheet is trying to swallow you whole!")
        user_hp = 0
        print (reader_name,"... I'm sorry... We can't do it")
        print ("You have", reader_hp, "try left")
        if restart_loop:
            continue
    elif choice == 3 :                                                                  #Skip The loop
        print ("Skipped the First Loop")
        break
    else:                                                                               #Wrong Input
        choice = int(input("Please enter a valid choice to start your adventure: "))    

    monster_hp = 5                                                                      #Monster HP
    mon_move = {                                                                        #Monster Move - Random
        "Tentacle": 1,
        "Head" : 2,
        "Double Tentacle" : 4,
    }



    while user_hp > 0 and monster_hp > 0:                                               #Fight Loop 
        
        print ("Your turn!")
        user_attack = int(input("Attack(1) or Defend(2)! It's your choice: "))
        monster_attack = random.choice(list(mon_move))                                  #Choose the Attack for the Monster : 
                                                                                        #Tentacule (1 dmg), Head (2 dmg), Double Tentacule (4 Dmg)
        if user_attack == 1 :                                                           #User Choice : Attack 
            print ("You punch the octopus in the face")
            user_damage = random.choice(list(user_move))
            monster_hp -= user_move[user_damage]
            print (user_damage)
            print ("the Monster use", monster_attack)
            print ("It deal",mon_move[monster_attack],"damage")
            user_hp = user_hp - mon_move[monster_attack]
        elif user_attack == 2:                                                          #User Choice : Defend
            print ("You defend yourself")
            user_hp = user_hp - (mon_move[monster_attack] // 2)
        else:                                                                           #Wrong Input
            choice = int(input("Please enter a valid action"))                           
        
        print ("the Monster use", monster_attack)
        print ("You lose", mon_move[monster_attack],"HP")
        print ("HP left", user_hp)
        print ("The Monster has", monster_hp, "HP left")

    if user_hp >= 0 and monster_hp <= 0 :                                               #Win the Fight
        print ("You win!")
        print ("Time to eat your lunch!")
    else :                                                                              #Loose the Fight
        print ("--------------------------- You loose... ----------------------------")
        reader_hp -= 1
        user_hp = 10
        monster_hp = 5
        print ("------------------------- Time to try again! ------------------------")
        restart_loop = True
        

    if user_hp <= 0:                                                                    #Lost One Try
        reader_hp -= 1

    if monster_hp <= 0 :                                                                #Check End Loop
        print ("end of the fight")
        break

    if restart_loop:                                                                    #Restart Loop
        continue

if reader_hp <= 0:                                                                      #Game Over
    print ("----------------------- At least you tried... -----------------------")
    print ("----------------------------- Game Over -----------------------------")
else:                                                                                   #Continue to the next loop
    print ("I didn't have a good fight like this in ages... Thanks mate!")
    print ("Time to take a look around my ship. *whistle* What a mess! I know i was drunk yesterday but didn't know that i left the ship like this... ")
    print ("Sorry dear", reader_name,"... It's time to clean the ship....")
    print ("What do you want to clean first? \nPut the Deck in order? or go my Room?(1) \nIt need a little(Big) cleaning too you know? (2)")
    print ("Pssst... We can also Choose to not clean at all but it will be harder later for me...(3)")
    choice = int(input("What do you choose?"))
    if choice == 1 :                                                                    #The Cutlass
        print ("You choose to Clean the Deck!")
        print ("Oh look at that! Hiding behind a barrel, you found my trusty Cutlass!")
        print ("I finally feel more at ease now that i have it.")
        print ("We never know what the sea has in store for us...")
        print ("-------------------- You have obtained a Cutlass --------------------")
        print ("--------------------- You deal more damage now ----------------------")
        print ("------------------------- Cutlass = Dmg +2 --------------------------")
        cutlass = True                                                                  #deal +2 each attack : 
        coat = False                                                                    #I will bring peace with the power of friendship and this big knife I found...  
    elif choice == 2 :                                                                  #The Buccaneer Coat
        print ("You choose to clean the  Room")
        print ("Why did you choose to do this? I hated when my mother wanted me to clean my room! :'[")
        print ("It's dark in here... I forgot to open the curtain this morning. Wait... You see this dark shape on the desk? Someone is on the ship with us...")
        print ("Show yourself! I see you! You don't want to taste the fury of my fist don't you?!")
        print ("... If you're not coming to me, I'll go to you! Ahaah")
        print ("-------------------- The pirate jump on the shape! -------------------")
        print ("-------------- It grab the shape and fall on the floor --------------")
        print ("---- You see them roll together and you hear the Pirate growling ----")
        print ("--------- Maybe a little light will help him win this fight?---------")
        windows = int(input("Open the Windows?(1) \n Or maybe you trust you guy enough and you're sure it's going to be ok?(2)"))
        if windows == 1 :                                                              #Open Window
            print ("------------------------ You open the Window ------------------------")
            print ("Oh...")
            print ("------ The dark Shape was in fact just a coat on the hanger... ------")
        elif windows == 2 :                                                            #Let the Pirate Fight in the dark
            print ("--------------- You let the Pirate continue his fight ---------------")
            print ("------------------- You hear him stifle a scream --------------------")
            user_hp -= 1
            print ("The pirate loose 1 Hp")
            print ("He have", user_hp, " Hp left")
            print ("With the light coming from the door, you see that this shape do not move like a human ")
            print ("Its arm aren't even fighting back, it just move with the movement of the pirate")
            print ("You finally decide to open the curtain of the Windows and you see it...")
            print ("------ The dark Shape was in fact just a coat on the hanger... ------")
            print ("The pirate see it too. He quickly stand up and, after clearing his troat, says: ")
            print ("Well... It was a fine enemy! Haha... Maybe next time I will put the hanger next to the door")
            print ("You know... Just to see it when i open the door... haha...")
            print ("The Pirate grab his coat and put it")
            print ("---------------- You have obtained a Bouccaneer Coat ----------------")
            print ("--------------------- You take less damage now ----------------------")
            print ("--------------------- Bouccarneer Coat = Def +2 ---------------------")
            coat = True                                                                 #loose less HP each time you defend : Buccaneer jacket def +2
            cutlass = False
        else:                                                                          #Wrong Input
            windows = int(input("Please enter a valid choice: "))    
    elif choice == 3:                                                                  #No Stuff to continue
        print ("Haaa, finally someone who understand me!")
        print ("I hate to clean! Thanks mates!")
    else:                                                                              #Wrong Input
        choice  = int(input("Please enter a valid choice: "))                  
        
user_knife = {                                                                           #Pirate Knife Attack - Random
    "It's a Critical hit!" : 7,
    "You land a Normal Hit" : 4,
    "You grazed it!" : 2,
    "You Missed..." : 0,
}

while user_hp > 0 and reader_hp > 0:                                                    #Second Loop - Stuff/Eat and then Fight (Seagull or I don't know) 
    restart_loop = False
    print ("I have", user_hp," HP left")



    print ("Your turn!")
    user_attack = int(input("Attack(1) or Defend(2)! It's your choice: "))
    monster_attack = random.choice(list(mon_move))                                  #Choose the Attack for the Monster : 
                                                                                    #Tentacule (1 dmg), Head (2 dmg), Double Tentacule (4 Dmg)
    if user_attack == 1 :                                                           #User Choice : Attack 
        
        
        if cutlass :
            user_damage = random.choice (list(user_knife))
            monster_hp -= user_knife[user_damage]
        else:
            user_damage = random.choice(list(user_move))
            monster_hp -= user_move[user_damage]
        print (user_damage)
        print ("the Monster use", monster_attack)
        print ("It deal",mon_move[monster_attack],"damage")
        if coat :
            user_hp = user_hp - mon_move[monster_attack] - 2   
        else:
            user_hp = user_hp - mon_move[monster_attack]
    elif user_attack == 2:                                                          #User Choice : Defend
        print ("You defend yourself")
        user_hp = user_hp - (mon_move[monster_attack] // 2)
    else:                                                                           #Wrong Input
        choice = int(input("Please enter a valid action"))                           
     
    print ("the Monster use", monster_attack)
    if mon_move[monster_attack] < 0 :
        print ("You lose 0 HP")
    else:
        print ("You lose", mon_move[monster_attack],"HP")
    
    print ("HP left", user_hp)
    print ("The Monster has", monster_hp, "HP left")



    if monster_hp <= 0 :
        print ("end of the fight")
        break

    if restart_loop:
        continue