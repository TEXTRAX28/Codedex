my_favorite_fruits = {"Watermelon", "Banana", "Pear"}
her_favorite_fruits = {"Apple", "Strawberry", "Watermelon"}

print("=== The First Way (dict) ===")
print(set(my_favorite_fruits).union(her_favorite_fruits))
print(set(my_favorite_fruits).intersection(her_favorite_fruits))
print(set(my_favorite_fruits).difference(her_favorite_fruits))
print("")

print("=== The Second Way (dict) ===")
union = my_favorite_fruits | her_favorite_fruits
intersection = my_favorite_fruits & her_favorite_fruits
difference = my_favorite_fruits - her_favorite_fruits

print(union)
print(intersection)
print(difference)
print("")

print("=== The Third Way (list) ===")
my_favorite_fruits_list = ["Watermelon", "Banana", "Pear"]
her_favorite_fruits_list = ["Apple", "Strawberry", "Watermelon"]
print(my_favorite_fruits_list.__add__(her_favorite_fruits_list))

