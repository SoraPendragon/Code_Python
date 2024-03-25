#Class
#Favorite Cities Class

class City :
    def __init__(self, name, country, population, landmarks, mayor, founding_year) :
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.mayor = mayor
        self.founding_year= founding_year

istres = City("Istres", "France", 43.478, ["Porte d'Arles", "Jet d'eau", "Etang de l'Olivier"], "Mr Bernardini", 966)

tokyo = City("Tokyo", "Japan", 13.960000,["Tokyo Tower", "Tsukiji Market", "Akihabara"], "Koike Yoriko", 1950)

print(vars(istres))

print(vars(tokyo))