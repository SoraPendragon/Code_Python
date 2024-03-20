#A game with python
#Terminal Adventure

from math import *
import random

#Sailor HP
user_hp = 10                                                                            
#Tries -> chance you can restart a loop.
reader_hp = 3 
loop = 0

print ("Hello, is it you that will come with me today?")
reader_name = input("What's the name of my dear reader? ")
while reader_hp > 0:
    loop += 1 
    #print ("this is the loop n°",loop)   #//
    #Pirate Attack - Random
    user_move = {
        "It's a Critical hit!" : 5,
        "You land a Normal Hit" : 2,
        "You Missed..." : 0,
    }

    #First Loop - OctoFight or BedDeath
    while user_hp > 0 and reader_hp >= 0: 
        print ("A pleasure to meet you", reader_name, "! What should we do today?")
        print ("You have", reader_hp,"try for this story")                                                  
        restart_loop = False
        #Sailor HP
        user_hp = 10    
        print ("Shall we go outside? See if the sea is happy today?(1) \nOr should we stay in bed?(2) ")
        choice = int(input("What do you want to do? "))
        #Start Adventure -> OctoFight
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
        #Bed Death - Start Again
        elif choice == 2 :
            print("Oh no, your bed sheet is trying to swallow you whole!")
            user_hp = 0
            print (reader_name,"... I'm sorry... We can't do it")
            print ("You have", reader_hp, "try left")
            if restart_loop:
                continue
        #Skip The loop    
        elif choice == 3 :                                                                  
            print ("---------------------- Skipped the First Loop -----------------------")
            break
        #Wrong Input
        else:                                                                               
            choice = int(input("Please enter a valid choice to start your adventure: "))
            user_hp = -17
            restart_loop = True    

        #Monster HP
        monster_hp = 5 
        #Monster Move - Random                                                                     
        mon_move = {                                                                        
            "Tentacle": 1,
            "Head" : 2,
            "Double Tentacle" : 4,
        }


        #Fight Loop - 1
        while user_hp > 0 and monster_hp > 0:                                                
            
            print ("Your turn!")
            user_attack = int(input("Attack(1) or Defend(2)! It's your choice: "))
        
            #Choose the Attack for the Monster :
            #Tentacule (1 dmg), Head (2 dmg), Double Tentacule (4 Dmg)
            monster_attack = random.choice(list(mon_move))
            #User Choice : Attack
            
            if user_attack == 1 : 
                print ("You punch the octopus in the face")
                user_damage = random.choice(list(user_move))
                monster_hp -= user_move[user_damage]
                print ("-", user_damage)
                print ("--------------- You deal", user_move[user_damage], "damage ------------------")
                print ("the Monster use", monster_attack)
                print ("--------------- It deal",mon_move[monster_attack],"damage -------------------")
                user_hp = user_hp - mon_move[monster_attack]
            #User Choice : Defend    
            elif user_attack == 2:                                                          
                print ("You defend yourself")
                user_hp = user_hp - (mon_move[monster_attack] // 2)
            #Wrong Input
            else:                                                                           
                choice = int(input("Please enter a valid action"))
                user_hp = -17
                restart_loop = True                           
            
            print ("------------------ You lose", mon_move[monster_attack],"HP -------------------")
            if user_hp < 0:
                print ("0 HP left")
            else:
                print ("HP left", user_hp)
            print ("The Monster has", monster_hp, "HP left")

        #Win the Fight
        if user_hp >= 0 and monster_hp <= 0 :                                               
            print ("You win!")
            print ("Time to eat your lunch!")
        #Wrong Input - Restart Loop
        elif user_hp == -17 :
            user_hp = 10
            monster_hp = 5
            restart_loop = True
        #Loose the Fight
        else :                                                                              
            print ("--------------------------- You loose... ----------------------------")
            reader_hp -= 1
            user_hp = 10
            monster_hp = 5
            print ("------------------------- Time to try again! ------------------------")
            restart_loop = True
            
        #Lost One Try
        if user_hp <= 0:                                                                    
            reader_hp -= 1
        #Check End Loop
        if monster_hp <= 0 :                                                                
            print ("End of the fight")
            break
        #Restart Loop
        if restart_loop:                                                                    
            continue
    
    #Game Over
    if reader_hp <= 0:                                                                      
        print ("----------------------- At least you tried... -----------------------")
        print ("----------------------------- Game Over -----------------------------")
        break  
    #Continue to the next loop
    else:      
        while loop == 1:                                                                             
            print ("I didn't have a good fight like this in ages... Thanks mate!")
            print ("Time to take a look around my ship. *whistle* What a mess! I know i was drunk yesterday but didn't know that i left the ship like this... ")
            print ("Sorry dear", reader_name,"... It's time to clean the ship....")
            print ("What do you want to clean first? \nPut the Deck in order?(1) \nOr go to my Room? It need a little(Big) cleaning too you know? (2)")
            print ("Pssst... We can also Choose to not clean at all but it will be harder later for me...(3)")
            choice = int(input("What do you choose? "))
            #The Cutlass : deal +2 each attack :
            if choice == 1 :                                                                    
                print ("You choose to Clean the Deck!")
                print ("Oh look at that! Hiding behind a barrel, you found my trusty Cutlass!")
                print ("I finally feel more at ease now that i have it.")
                print ("We never know what the sea has in store for us...")
                print ("-------------------- You have obtained a Cutlass --------------------")
                print ("--------------------- You deal more damage now ----------------------")
                print ("------------------------- Cutlass = Dmg +2 --------------------------")
                cutlass = True
                coat = False                                                                    #I will bring peace with the power of friendship and this big knife I found...  
            #The Buccaneer Coat : loose less HP, - 2 each dmg you take
            elif choice == 2 :                                                                  
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
                #Open Window
                if windows == 1 :                                                              
                    print ("------------------------ You open the Window ------------------------")
                    print ("Oh...")
                    print ("------ The dark Shape was in fact just a coat on the hanger... ------")
                    print ("Man... Can we never talk about that again... please", reader_name, "?")
                #Let the Pirate Fight in the dark
                elif windows == 2 :                                                            
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
                #Wrong Input
                else:                                                                          
                    windows = int(input("Please enter a valid choice: "))
                    user_hp = -17
                    restart_loop = True    
                print ("---------------- You have obtained a Bouccaneer Coat ----------------")
                print ("--------------------- You take less damage now ----------------------")
                print ("--------------------- Bouccarneer Coat = Def +2 ---------------------")
                coat = True
                cutlass = False
            #No Stuff to continue
            elif choice == 3:                                                                  
                print ("Haaa, finally someone who understand me!")
                print ("I hate to clean! Thanks mates!")
            #Wrong Input
            else:                                                                              
                choice  = int(input("Please enter a valid choice: "))
                user_hp = -17
                restart_loop = True  
             #Cleaning Duty -> Coat or Cutlass for fight  
            if choice == 1 or choice == 2:
                print ("What a beautiful day...after all this cleaning, I'm Hungry!") 
                print ("It's already noon! Time to prepare Lunch")
            #No Stuff to Continue, Harder for future fight
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
            break    
        #Skip if already a Loop

    #Pirate Knife Attack - Random
    user_knife = {
        "It's a Critical hit!" : 7,
        "You land a Normal Hit" : 4,
        "You grazed it!" : 2,
        "You Missed..." : 0,
    }

    #Monster HP
    monster_hp = 7                                                                      

    #Second Loop - Fight (Seagull) 
    while user_hp > 0 and reader_hp > 0 and monster_hp > 0:
        restart_loop = False
        #Monster Move - Random
        mon_move = {                                                                        
            "Wing Kick": 3,
            "Peck" : 4,
            "Double Peck" : 6,
        }
        
        print ("Your turn!")
        print ("I have", user_hp,"HP left")
        #User Input
        user_attack = int(input("Attack(1) or Defend(2)! It's your choice: "))
        #Choose the Attack for the Monster : 
        #Wing Kick (3 dmg), Peck (4 dmg), Double Peck (6 Dmg)
        monster_attack = random.choice(list(mon_move))

        #User Choice : Attack 
        if user_attack == 1 :
            #Attack With Knife                                                           
            if cutlass == True:
                user_damage = random.choice (list(user_knife))
                monster_hp -= user_knife[user_damage]
                print (user_damage)
                print ("--------------- You deal", user_knife[user_damage], "damage ------------------")
                #print ("Check knife dmg:",user_damage)   #//
            #Attack without Knife
            else:
                user_damage = random.choice(list(user_move))
                monster_hp -= user_move[user_damage]
                print (user_damage)
                print ("--------------- You deal", user_move[user_damage], "damage ------------------")
                #print ("Check Hand dmg:", user_damage)   #//
            
            #Check msg for Monster HP
            if monster_hp < 0:
                print ("The Monster has 0 HP left")
            else:
                print ("The Monster has", monster_hp, "HP left")
            
            #Check if Monster has enough HP to attack
            if monster_hp > 0:
                print ("the Monster use", monster_attack)
                print ("It deal",mon_move[monster_attack],"damage")
                if coat == True:
                    coat_dmg = mon_move[monster_attack] - 2
                    user_hp = user_hp - coat_dmg  
                    #print ("check coat_dmg: ")              #//
            #Monster Can't Attack because no HP
                else:
                    user_hp = user_hp - mon_move[monster_attack]
                    #print ("Check no coat dmg")             #//

        #User Choice : Defend        
        elif user_attack == 2:                                                          
            print ("You defend yourself")
            print ("the Monster use", monster_attack)
            #Defend with Coat
            if coat == True:                                                            
                coat_dmg = (mon_move[monster_attack] - 2) // 2
                user_hp = user_hp - coat_dmg
                #print ("check coat_dmg")                #//
            #Defend without Coat
            else:                                                                       
                user_hp = user_hp - (mon_move[monster_attack] // 2)
                #print ("check no coat dmg")             #// 
            
            #Check msg for Monster HP
            if monster_hp < 0:
                print ("The Monster has 0 HP left")
            else:
                print ("The Monster has", monster_hp, "HP left")
        elif user_attack == 3:
            print ("---------------------- Skipped the Second Loop -----------------------")
            monster_hp = 0
            break
        #Wrong Input 
        else:                                                                           
            choice = int(input("Please enter a valid action"))
            user_hp = -17
            restart_loop = True                           
        
        #Msg Loose HP With and Without Coat
        if user_hp > 0 and coat == False:
            print ("###### You lose", mon_move[monster_attack],"HP ######")
        elif user_hp > 0 and coat == True:
            print ("------- You lose", coat_dmg,"HP -------")
        else:
            print ("###### You lose 0 HP ######")
        
        print ("HP left:", user_hp)

        #Win the Fight
        if user_hp > 0 and monster_hp <= 0 :                                            
            print ("You win!")
            print ("Time to eat!")
            break
        #Wrong Input - Restart Loop
        elif user_hp == -17 :
            user_hp = 10
            monster_hp = 5
            restart_loop = True
        # Continue
        elif user_hp > 0 and monster_hp > 0:                                            
            continue
        #Loose the Fight
        else :                                                                          
            print ("--------------------------- You loose... ----------------------------")
            reader_hp -= 1
            user_hp = 10
            monster_hp = 7
            print ("------------------------- Time to try again! ------------------------")
            print (reader_hp, "try left")
            restart_loop = True

        #Restart Loop Monster
        if restart_loop:                                                                    
            continue

    #Game Over
    if reader_hp <= 0:                                                                      
        print ("----------------------- At least you tried... -----------------------")
        print ("----------------------------- Game Over -----------------------------")
    #Continue to the next loop
    else:
        if loop == 1:                                                                            
            print ("Aaaaah this Octopus was delicious!")
            print ("Damn this Seagull! She almost made me overcooked my food!")
            print ("Okay! So now, what can we do now,", reader_name,"?\nI'm not really in the mood to fish now...")
            print ("Oh i know! With the Seagull and what's left of the Octopus i can cook dinner tonight!")
            print ("And One less task to do today!") 
            #Yes i didn't want to code this one
            print ("So I can either cook...again...(1 - Please don't choose this one 😢)")
            print ("Or we can sleep until tonight!(2) Oh yeah i really like this plan!")
            print ("Plus,I'm suuuuuper tired with these fight! Let's do that!")
            print ("Oh yeah i forgot... You choose... ")
            choice = int(input("So? What am I doing? "))

            if choice == 1:
                print ("------- You hear a crack in the sky as you enter the letter 1 -------")
                print ("---- The sky become dark as the eyes of the pirate become white -----")
                for i in range(1, 5, 1) :
                    if i < 2:
                        print ("---------- So? What am I doing? 1 ----------")
                    elif i <= 3:
                        print ("---------- So? What am I doing? ### ----------")
                    else:
                        print ("----------So? What am I doing? 2 ----------")
                print ("------ You watch with Horror as the number 1 turn slowly in a 2 -----")
                print ("Oh I knew you would choose to nap! You really are my best mate,", reader_name, "!")
                print ("...")
                print ("What? What cooking task? I can always do that tonight, no?")
                print ("You tell me that you chose to cook? Hum... Strange")
                print ("-------------------- You hear the pirate mumbled -------------------")
                print("*He's not suppose to know when i do that...*")
                print ("Maybe you missclisk? It happens everytime with other mate don't worry!")
            elif choice == 2:
                print ("Oh I knew you would choose to nap! You really are my best mate,", reader_name, "!")
                print ("Good so i'll come back tonight! I let the deck to you ok? \nTake care of my ship for me will you?")
            else:
                choice = int(input("Please enter a valid choice: "))
                user_hp = -17
                restart_loop = True

            print ("---------- Thanks to his nap, the pirate regain all his HP ---------")
            user_hp = 10
            print (user_hp, "HP left")
            print ("--- As the afternoon came to an end, you see the pirate come out of the cabin ---")
            print ("aaaarh what a good nap! What time is it?")
            print ("Oh this late! **** I wasn't planning to sleep this long!")
            print ("Quick, I'll grab the pan and the seeagull, grab the rest what's left of the Octopus!")
            print ("--- Both of you start to cook and by the time the dinner is ready the sun is setting ---")
            print ("--------------------- You both eat in the light of the setting sun ---------------------")
            print ("------------- You remember with nostalgia at you adventure with the pirate -------------")
            print ("------------------ After finishing dinner, the Pirate clear his troat ------------------")
            print ("Ok there is one last choice, you need to make...")
            print ("With what do you want to finish the day? A beer or a song?")
            print ("I have the finest rum for you,", reader_name,"!")
            print ("And I have prepared a fine song of our adventure!")
            print ("But i can't do both, and a pirate's rum is something sacred!(1)")
            print ("This song is about our day together after all!(2)")
            print ("--------------------- The pirate is watching you with a kind look ---------------------")
            choice = int(input("So what do you want to finish our day with!? "))

            if choice == 1:
                print ("Good, i would have choose the rum too! Sit my dear friend!")
                print ("Let met tell you some story before you go...")
                print ("-------------------- Both of you drinks till the end of the night ---------------------")
                print ("---------------------- The pirate seems to have too many drinks -----------------------")
                #Need to put the if for the Cutlass = True
                if cutlass == True:
                    print ("----- You see him playing with his cutlass and trying to launch it on some barrel -----")
                    print ("---- With the Alcool's effect, at one point, the pirate stop to go fetch the knife ----")
                    print ("---------- Both of you forgot about the knife and continue to talk all night ----------")
                    print ("-------------------------- The pirate no longer have a knife --------------------------")
                    print ("--------------------------------- Pirate Dmg = Dmg -2 ---------------------------------")
                else: 
                    print ("------- You both enjoy the moonlight ray and continue to enjoy the Pirate's song ------")
                print ("------------------ With the joy of the night you both start to dance ------------------")
                #Need to put the if Coat = True
                if coat == True:
                    print ("------------------ The pirate is feeling hot, he takes off his coat -------------------")
                    print ("--------------------------------- Pirate Def = Def -2 ---------------------------------")
                else:
                    print ("------------------ Witht the night continuing you start to feel tired -----------------")
                print ("The night is well advanced now... Maybe we need to go to sleep!")
                print ("One last time... thanks,", reader_name, ". I hope we see each other again")
                print ("you were really a good reader for me.")
                print ("Restart me when you'll miss me!")
                print ("---------------------------------------------------------------------------------------")
                print ("------------------------------- It's the end of the game ------------------------------")
                print ("---------------------------------- Thanks for playing ---------------------------------")
                print ("---------------------------- And sorry for the bad code ^^' ---------------------------")
                print ("---------------------------------------------------------------------------------------")
                break
            #Siren Come On the Ship
            elif choice == 2:
                print ("So you trust me enough to sing our night away huh?")
                print ("I will do my best then!")
                print ("It's singin' time!")
                print ("----------------- When the pirate start to sing, you start to laugh... ----------------")
                print ("--------------------------- He is very bad at singing haha ----------------------------")
                print ("---- As the night continue to advance, the pirate start to randomly sing other song ---")
                print ("---------- Song after song, you're used to the horrible voice of the pirate -----------")
                print ("------------------------ Suddenly you hear the water moving... ------------------------")
                print ("--------------------------- A creature jumps high in the sky --------------------------")
                print ("---------------- With the moonlight, you see voluptous form and a fin -----------------")
                print ("-------------- The Creature land on the ship and watch you and the pirate -------------")
                print ("-------------------- A Siren glare at you with sleep depraved eyes --------------------")
                print ("Is it you who sing like in the night?")
                print ("You don't know that there is people that like to sleep at night?")
                print ("---------- Both you and the pirate look at each other with a dumbfounded face ---------")
                print ("Okay... I see you're in no position to talk...")
                print ("If you're like all the other pirate that comes in these place often, you will not listen to me")
                print ("Since i'm a beauty and I, in fact, need my beauty sleep, I will kill you now!")
                print ("Sorry, you look cute but i don't want to take any risk to loose my sleep...")
                print ("---------- Coming to his senses faster than you, the pirate prepare to battle ---------")

        monster_hp = 13
        print ("------------------------------------ Battle start! ------------------------------------")
        print ("Quick! I need you to choose for me, mate!")
        #Fight with the siren
        while user_hp > 0 and monster_hp > 0:
            restart_loop = False
            #Monster Move - Random
            mon_move = {                                                                        
                "Claw Strike": 3,
                "A Beauty Scream in the Night!" : 6,
                "Fin Blow" : 5,
            }
            #Pirate Knife Attack - Random
            user_knife = {
                "It's a Critical hit!" : 8,
                "You land a Normal Hit" : 6,
                "You grazed it!" : 4,
                "You Missed..." : 0,
            }

            print ("------------------------------------- Your turn! --------------------------------------")
            print ("I have", user_hp,"HP left")
            #User Input
            user_attack = int(input("Attack(1) or Defend(2)! It's your choice: "))
            #Choose the Attack for the Monster : 
            #Wing Kick (3 dmg), Peck (4 dmg), Double Peck (6 Dmg)
            monster_attack = random.choice(list(mon_move))

            #User Choice : Attack 
            if user_attack == 1 :
                #Attack With Knife                                                           
                if cutlass == True:
                    user_damage = random.choice (list(user_knife))
                    monster_hp -= user_knife[user_damage]
                    print (user_damage)
                    print ("--------------- You deal", user_knife[user_damage], "damage ------------------")
                    #print ("Check knife dmg:",user_damage)   #//
                #Attack without Knife
                else:
                    user_damage = random.choice(list(user_move))
                    monster_hp -= user_move[user_damage]
                    print (user_damage)
                    print ("--------------- You deal", user_move[user_damage], "damage ------------------")
                    #print ("Check Hand dmg:", user_damage)   #//
                
                #Check msg for Monster HP
                if monster_hp < 0:
                    print ("The Monster has 0 HP left")
                    print ("You win!")
                    print ("Time to end this!")
                    break
                else:
                    print ("The Monster has", monster_hp, "HP left")
                    print ("You win!")
                    print ("Time to end this!")
                
                #Check if Monster has enough HP to attack
                if monster_hp > 0:
                    print ("the Monster use", monster_attack)
                    print ("It deal",mon_move[monster_attack],"damage")
                    if coat == True:
                        coat_dmg = mon_move[monster_attack] - 2
                        user_hp = user_hp - coat_dmg  
                        #print ("check coat_dmg: ")              #//
                #Monster Can't Attack because no HP
                    else:
                        user_hp = user_hp - mon_move[monster_attack]
                        #print ("Check no coat dmg")             #//
            #User Choice : Defend        
            elif user_attack == 2:                                                          
                print ("You defend yourself")
                print ("the Monster use", monster_attack)
                #Defend with Coat
                if coat == True:                                                            
                    coat_dmg = (mon_move[monster_attack] - 2) // 2
                    user_hp = user_hp - coat_dmg
                    #print ("check coat_dmg")                #//
                #Defend without Coat
                else:                                                                       
                    user_hp = user_hp - (mon_move[monster_attack] // 2)
                    #print ("check no coat dmg")             #// 
                
                #Check msg for Monster HP
                if monster_hp < 0:
                    print ("The Monster has 0 HP left")
                    print ("You win!")
                    print ("Time to end this!")
                    break
                else:
                    print ("The Monster has", monster_hp, "HP left")
                    print ("You win!")
                    print ("Time to end this!")
            #Wrong Input 
            else:                                                                           
                choice = int(input("Please enter a valid action"))
                user_hp = -17
                restart_loop = True                        
            
            #Msg Loose HP With and Without Coat
            if user_hp > 0 and coat == False:
                print ("###### You lose", mon_move[monster_attack],"HP ######")
            elif user_hp > 0 and coat == True:
                print ("------- You lose", coat_dmg,"HP -------")
            else:
                print ("###### You lose 0 HP ######")
            
            print ("HP left:", user_hp)

            #Win the Fight
            if user_hp > 0 and monster_hp <= 0 :                                            
                print ("You win!")
                print ("Time to end this!")
                break
            #Wrong Input - Restart Loop
            elif user_hp == -17 :
                user_hp = 10
                monster_hp = 5
                restart_loop = True
            # Continue
            elif user_hp > 0 and monster_hp > 0:                                            
                continue
            #Loose the Fight
            else :                                                                          
                print ("--------------------------- You loose... ----------------------------")
                reader_hp -= 1
                user_hp = 10
                monster_hp = 13
                print ("------------------------- Time to try again! ------------------------")
                print (reader_hp, "try left")
                restart_loop = True
            
            if loop > 1 and user_hp > 0 and monster_hp < 0:
                break

            #Restart Loop
            if restart_loop:                                                                    
                continue
    
    if user_hp > 0 and monster_hp <= 0 :
        print ("--------------------------- The Siren scream has she dies... --------------------------")
        print ("------------- Finally after all this adventure, you can both be at ease... ------------")
        print ("-------------------------- The Pirate looks at you, exhausted -------------------------")
        print ("---------------- He stretch his body and after clearing his throat say ----------------")
        print ("The night is well advanced now... Maybe we need to go to sleep!")
        print ("One last time... thanks,", reader_name, ". I hope we see each other again")
        print ("You were really a good reader for me.")
        print ("Restart me when you'll miss me!")
        print ("---------------------------------------------------------------------------------------")
        print ("------------------------------- It's the end of the game ------------------------------")
        print ("---------------------------------- Thanks for playing ---------------------------------")
        print ("---------------------------- And sorry for the bad code ^^' ---------------------------")
        print ("---------------------------------------------------------------------------------------")
        break
    else:
        continue