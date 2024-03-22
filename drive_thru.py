#Drive-Thru

food = [
    '🍔 Cheeseburger',  #1
    '🍟 Fries',         #2
    '🥤 Soda',          #3
    '🍦 Ice Cream',     #4
    '🍪 Cookie'        #5
]

def welcome():
    print ("-------- Welcome! --------")   
    print ("- May I take your Order? -")
    print ("1 - 🍔 Cheeseburger")
    print ("2 - 🍟 Fries")
    print ("3 - 🥤 Soda")
    print ("4 - 🍦 Ice Cream")
    print ("5 - 🍪 Cookie")


def get_item(x):
    x = choice
    return food[x-1]

welcome()
choice  = int(input("What is the n° of your product: "))
print (get_item(choice))