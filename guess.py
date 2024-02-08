#Guess a Number

guess = 0

tries = 0


while guess != 6 and tries <= 6:
  guess = int(input("Guess the number:  "))
  tries += 1

if tries > 6:
  print('Too many tries, Restart the code')
else:
    print("You got it!")
