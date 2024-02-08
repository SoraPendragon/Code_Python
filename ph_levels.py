#Check whether a pH level is acidic, basic or neutral

ph = int(input("Enter a pH value between 0 and 14: "))

if ph < 0 or ph > 14:
    print ("please enter a real value btw 0 and 14: ")
else:
    if ph > 7:
        print ("Basic")
    elif ph < 7:
        print ("Acidic")
    else:
        print ("Neutral")