class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False

Restaurant1 = Restaurant()
print(Restaurant1.name)

Restaurant.name = "blank"
print(Restaurant1.name)

Restaurant.name = "McDonald's"
print(Restaurant1.name)