#Convert Currency

co = int(input ("What do you have left in pesos? "))
pe = int(input ("What do you have left in soles? "))
br = int(input ("What do you have left in reais? "))

usd = co * (0.00025) + pe * 0.27 + br * 0.20

print ("you have ",usd,"$")