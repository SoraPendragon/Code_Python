#Checking Grades

grade = int(input ("What score did you get? "));            #int(input ("What score did you get? "))

if grade < 0 or grade >100:
    print ("Enter a real score, please!")
else:
    if grade >= 55:
        print ("You passed!!!")
    else:
        print ("You failed...")