#Condition to use the Cyclone 

height = int(input("What is you Height? "))
credits = int(input("How many credits do you have? "))

if height >= 137 and credits >= 10:
    print ("Enjoys the ride!")
elif height < 137 and credits >= 10:
    print ("You're not tall engouh to ride...")
elif height >= 137 and credits < 10:
    print("You don't have enough credits")
else:
    print("you don't meet the requirement to ride")