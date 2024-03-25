#Class
#Pokedex

class Pokemon :
    def __init__(self, entry, name, types, description, height, weight, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.height = height
        self.weight = weight
        self.is_caught = is_caught

    def speak(self):
        print (self.name,",", self.name,"!")
    
    def display_details (self):
        print ("Entry Number:", int(self.entry))
        print ("Name:", str(self.name))

        if len(self.types) == 1:
            print ("Type:", str(self.types[0]))
        else :
            print ("Type:", str(self.types[0]), "/", str(self.types[1]))

        print ("Description:", str(self.description))
        print ("Height:", float(self.height))
        print ("Weight:", float(self.weight), "lbs")
        
        if self.is_caught :
            print (self.name, "has already been caught!")
        else:
            print (self.name,"hasn't already been caught!")

pikachu = Pokemon(35, "Pikachu", ["Electric"], "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.",1.04, 13.2, True)
pikachu.speak()
pikachu.display_details()

bulbi = Pokemon(1, "Bulbasaur", ["Grass", "Poison"], "For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.", 2.04, 15.2, True)
bulbi.speak()
bulbi.display_details()

mew = Pokemon(151, "Mew", ["Psychic"], "When viewed through a microscope, this Pokémon’s short, fine, delicate hair can be seen.", 1.04, 8.8, False)
mew.speak()
mew.display_details()

shaymin = Pokemon(492, "Shaymin", ["Grass"], "It can dissolve toxins in the air to instantly transform ruined land into a lush field of flowers.", 0.08, 4.6, False)
shaymin.speak()
shaymin.display_details()