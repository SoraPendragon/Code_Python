#Fortune Cookie

import random
answer = [
    "Don't pursue happiness – create it.",
    "All things are difficult before they are easy.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "Someone in your life needs a letter from you.",
    "Don't just think. Act!",
    "Your heart will skip a beat.",
    "The fortune you search for is in another cookie.",
    "Help! I'm being held prisoner in a Chinese bakery!",
]


def fortune():
    #print (random.choice(answer))
    random_fortune = random.randint(0,7)
    print (random_fortune)
    if random_fortune == 0:
        print (answer[0])
    elif random_fortune == 1:
        print (answer[1])
    elif random_fortune == 2:
        print (answer[2])
    elif random_fortune == 3:
        print (answer[3])
    elif random_fortune == 4:
        print (answer[4])
    elif random_fortune == 5:
        print (answer[5])
    elif random_fortune == 6:
        print (answer[6])
    else:
        print (answer[7])

fortune()
fortune()
fortune()