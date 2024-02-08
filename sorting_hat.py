#Create a Sorting Hat (Choixpeau)

gryffindor = 0                    #Gryffindor
ravenclaw = 0                     #Ravenclaw
hufflepuff = 0                    #Hufflepuff
slytherin = 0                     #Slytherin

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~The Sorting Hat~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~Question 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ("Do you like Dawn or Dusk? \n 1)Dawn \n 2)Dusk \n")

Q1 = int(input("Enter answer (1/2): "))

#    1) Dawn => gryff and Raven = +1
#    2) Dusk => huff and sly = +1

if Q1 == 1:
    gryffindor +=  1
    ravenclaw += 1
elif Q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print ("Wrong Input.")

#~~~~~~~~~~~~~~~~~~~~Question 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ("When I’m dead, I want people to remember me as: \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold \n")

Q2 = int(input("Enter answer (1-4): "))

#    1) The Good => huff +2
#    2) The Great => sly +2
#    3) The Wise => raven +2
#    4) The Bold => gryff +2

if Q2 == 1:
    hufflepuff += 2
elif Q2 == 2:
    slytherin += 2
elif Q2 == 3:
    ravenclaw += 2
elif Q2 == 4:
    gryffindor += 2
else:
    print ("Wrong Input")

#~~~~~~~~~~~~~~~~~~~~Question 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ("Which kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum \n")

Q3 = int(input("Enter answer (1-4): "))

#    1) The violin => sly +4
#    2) The trumpet => huff +4
#    3) The piano => raven +4
#    4) The drum => gryff +4

if Q3 == 1:
    slytherin +=4
elif Q3 == 2:
    hufflepuff +=4
elif Q3 == 3:
    ravenclaw +=4
elif Q3 == 4:
    gryffindor +=4
else:
    print("Wrong Input")

#~~~~~~~~~~~~~~~~~~~~Results ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("Gryffindor: ", gryffindor)
elif ravenclaw > hufflepuff and ravenclaw > slytherin:
    print ("Ravenclaw: ", ravenclaw)
elif hufflepuff > slytherin:
    print ("Hufflepuff: ", hufflepuff)
else:
    print ("Slytherin: ", slytherin)
