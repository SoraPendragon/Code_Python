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

while user_hp > 0 and reader_hp >= 0:                                                   #First Loop - OctoFight or BedDeath
    restart_loop = False
    user_hp = 10    #Sailor HP
    print ("Shall we go outside? See if the sea is happy today?(1) \nOr should we stay in bed?(2) ")
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
        print ("---------------------- Skipped the First Loop -----------------------")
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
            print ("-", user_damage)
            print ("--------------- You deal", user_move[user_damage], "damage ------------------")
            print ("the Monster use", monster_attack)
            print ("--------------- It deal",mon_move[monster_attack],"damage -------------------")
            user_hp = user_hp - mon_move[monster_attack]
        elif user_attack == 2:                                                          #User Choice : Defend
            print ("You defend yourself")
            user_hp = user_hp - (mon_move[monster_attack] // 2)
        else:                                                                           #Wrong Input
            choice = int(input("Please enter a valid action"))                           
        
        print ("the Monster use", monster_attack)
        print ("------------------ You lose", mon_move[monster_attack],"HP -------------------")
        if user_hp < 0:
            print ("0 HP left")
        else:
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
    choice = int(input("What do you choose? "))
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
        print ("You choose to clean the Room")
        print ("Why did you choose to do this? I hated when my mother wanted me to clean my room! :'[")
        print ("It's dark in here... I forgot to open the curtain this morning. Wait... You see this dark shape on the desk? Someone is on the ship with us...")
        print ("Show yourself! I see you! You don't want to taste the fury of my fist don't you?!")
        print ("... If you're not coming to me, I'll go to you! Ahaah")
        print ("-------------------- The pirate jump on the shape! -------------------")
        print ("-------------- It grab the shape and fall on the floor --------------")
        print ("---- You see them roll together and you hear the Pirate growling ----")
        print ("--------- Maybe a little light will help him win this fight?---------")
        print ("Open the Windows?(1) \nOr maybe you trust you guy enough and you're sure it's going to be ok?(2)")
        windows = int(input("What do you do? "))
        if windows == 1 :                                                              #Open Window
            print ("------------------------ You open the Window ------------------------")
            print ("Oh...")
            print ("------ The dark Shape was in fact just a coat on the hanger... ------")
            print ("Man... Can we never talk about that again... please", reader_name, "?")
        elif windows == 2 :                                                            #Let the Pirate Fight in the dark
            print ("--------------- You let the Pirate continue his fight ---------------")
            print ("------------------- You hear him stifle a scream --------------------")
            user_hp -= 1
            print ("The pirate loose 1 Hp")
            print ("He have", user_hp, "Hp left")
            print ("With the light coming from the door, you see that this shape do not move like a human ")
            print ("Its arm aren't even fighting back, it just move with the movement of the pirate")
            print ("You finally decide to open the curtain of the Windows and you see it...")
            print ("------ The dark Shape was in fact just a coat on the hanger... ------")
            print ("The pirate see it too. He quickly stand up and, after clearing his troat, says: ")
            print ("Well... It was a fine enemy! Haha... Maybe next time I will put the hanger next to the door")
            print ("You know... Just to see it when i open the door... haha...")
            print ("The Pirate grab his coat and put it")
        else:                                                                          #Wrong Input
            windows = int(input("Please enter a valid choice: "))    
    
        print ("---------------- You have obtained a Bouccaneer Coat ----------------")
        print ("--------------------- You take less damage now ----------------------")
        print ("--------------------- Bouccarneer Coat = Def +2 ---------------------")
        coat = True                                                                 #loose less HP each time you defend : Buccaneer jacket def +2
        cutlass = False
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

if choice == 1 or choice == 2:
    print ("What a beautiful day...after all this cleaning, I'm Hungry!") 
    print ("It's already noon! Time to prepare Lunch")
else : 
    print ("Since i'm not cleaning, i think i will write some verse for this evening song")
    print ("All good pirate must sing after having dinner! With a little bit of rum of course...")
    print ("------ The pirate was so focused on his song that he didn't see the time pass ------")
    print ("Oh, it's already noon! Time to eat! I'm hungry!")

print ("So,", reader_name,"What can we eat ? Oh I know! The Octopus from this morning!")
print ("---- The pirate takes out a frying pan and a stove from behind some other barrel ----")
print ("-------- While he start to cook the octopus you hear a sound in the distance --------")
print ("Qwaaaack")
print ("Argh a bloody seagull... We're far from any land what is it doing here...")
print ("----- As the sound becoome louder, you see a Gigantic Bird landing on the Deck ------")
print ("------------------- It immediatly start to look at the frying pan -------------------")
print ("Oh no it's my lunch! If you want to eat go fish elsewhere!")
print ("------------- The pirate take place between the stove and the seagulls --------------")
print ("-------------- She doesn't seem to like the attitude of the pirate... ---------------")
print ("---------------------- She start to scream and rush toward him! ---------------------")
print ("-------------------------- it's time to fight the seagulls --------------------------")


monster_hp = 7                                                                      #Monster HP

while user_hp > 0 and reader_hp > 0:                                                    #Second Loop - Stuff/Eat and then Fight (Seagull or I don't know) 
    while monster_hp > 0:
        restart_loop = False
        mon_move = {                                                                        #Monster Move - Random
            "Wing Kick": 3,
            "Peck" : 4,
            "Double Peck" : 6,
        }
        
        print ("Your turn!")
        print ("I have", user_hp,"HP left")
        user_attack = int(input("Attack(1) or Defend(2)! It's your choice: "))
        monster_attack = random.choice(list(mon_move))                                  #Choose the Attack for the Monster : 
                                                                                        #Tentacule (1 dmg), Head (2 dmg), Double Tentacule (4 Dmg)
        if user_attack == 1 :                                                           #User Choice : Attack 
            if cutlass == True:
                user_damage = random.choice (list(user_knife))
                monster_hp -= user_knife[user_damage]
                print (user_damage)
                print ("--------------- You deal", user_knife[user_damage], "damage ------------------")
                print ("Check knife dmg:",user_damage)   #//
            else:
                user_damage = random.choice(list(user_move))
                monster_hp -= user_move[user_damage]
                print (user_damage)
                print ("--------------- You deal", user_move[user_damage], "damage ------------------")
                print ("Check Hand dmg:", user_damage)   #//
            
            if monster_hp < 0:
               print ("The Monster has 0 HP left")
            else:
                print ("The Monster has", monster_hp, "HP left")
            
            if monster_hp > 0:
                print ("the Monster use", monster_attack)
                print ("It deal",mon_move[monster_attack],"damage")
                if coat == True:
                    coat_dmg = mon_move[monster_attack] - 2
                    user_hp = user_hp - coat_dmg  
                    print ("check coat_dmg: ")              #//
                else:
                    user_hp = user_hp - mon_move[monster_attack]
                    print ("Check no coat dmg")             #//
                        
        elif user_attack == 2:                                                          #User Choice : Defend
            print ("You defend yourself")
            print ("the Monster use", monster_attack)
            if coat == True:                                                            #Defend with Coat
                coat_dmg = (mon_move[monster_attack] - 2) // 2
                user_hp = user_hp - coat_dmg
                print ("check coat_dmg")                #//
            else:                                                                       #Defend without Coat
                user_hp = user_hp - (mon_move[monster_attack] // 2)
                print ("check no coat dmg")             #// 
            
            if monster_hp < 0:
               print ("The Monster has 0 HP left")
            else:
                print ("The Monster has", monster_hp, "HP left")   
        else:                                                                           #Wrong Input
            choice = int(input("Please enter a valid action"))                           
        
        if user_hp > 0 and coat == False:
            print ("###### You lose", mon_move[monster_attack],"HP ######")
        elif user_hp > 0 and coat == True:
            print ("------- You lose", coat_dmg,"HP -------")
        else:
            print ("###### You lose 0 HP ######")
        
        print ("HP left:", user_hp)

        if user_hp > 0 and monster_hp <= 0 :                                            #Win the Fight
            print ("You win!")
            print ("Time to continue our day!")
            break
        elif user_hp > 0 and monster_hp > 0:                                            # Continue
            continue
        else :                                                                          #Loose the Fight
            print ("--------------------------- You loose... ----------------------------")
            reader_hp -= 1
            user_hp = 10
            monster_hp = 7
            print ("------------------------- Time to try again! ------------------------")
            print (reader_hp, "try left")
            restart_loop = True

        if restart_loop:                                                                    #Restart Loop
            continue