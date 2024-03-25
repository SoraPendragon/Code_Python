#Class
#Restaurant Class + Bob's Burger

class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False

bobs_burger = Restaurant()

bobs_burger.name = "Bob\'s Burgers"
bobs_burger.category = "American Diner"
bobs_burger.rating = 4.7
bobs_burger.delivery = False

sugo_dicantina = Restaurant()

sugo_dicantina.name = "Sugo Di Cantina"
sugo_dicantina.category = "Pasta Restaurant"
sugo_dicantina.rating = 5.5
sugo_dicantina.delivery = False

ofrench_tacos = Restaurant()

ofrench_tacos.name = "O\'French Tacos"
ofrench_tacos.category = "Tacos"
ofrench_tacos.rating = 4.2
ofrench_tacos.delivery = True

print(vars(bobs_burger))

print(vars(sugo_dicantina))

print(vars(ofrench_tacos))