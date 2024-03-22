#The reel fun begins
#Built-in Function


lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

#input() - already said : permit to enter some text
pkfaire = input("this is a test of the input: ")

#print() - already said : permit to show text in the box
print (pkfaire)

#range() - already said : limit the impression of i in this for loop
for i in range (0, 5, 1):
    print (i)
    i += 1

#len - already said : print the lenght of the list lego_parts
print(len(lego_parts))

#import - already seen : import a library
import random
num = random.randint(0, 1)   # Generates a random number that's either 0 or 1
if num > 0.5:
  print('Heads')
else:
  print('Tails')

#int - already seen : permit to enter some number in the box
num = int(input("Test Input: "))
print ("Is this your num :", num)

#max() - already seen : print the the value with higher number in the list lego_parts
print (min(lego_parts))

#min()  - already seen : print the the value with lowest number in the list lego_parts
print (max(lego_parts))

#Bin - not seen previously : convert the x value in a binary string
print(bin(28))