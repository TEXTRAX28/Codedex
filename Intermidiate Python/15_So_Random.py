import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(suffix_list):
    return [word.capitalize() for word in suffix_list]

def fire_in_name(name):
    return "Fire" in name

def concatenate_names(name1, name2):
    return name1 + ' ' + name2

def display():
    print("Generated Fantasy Random Names")
    for name in random_names:
        print(name)

    print("Names Containing Fire: ")
    for name in fire_name:
        print(name)

    print("Concatenated Names: ")
    print(reduced_name)

capitalize_suffixes = capitalize_suffix(suffixes)
random_names = [create_fantasy_name(prefixes, capitalize_suffixes) for i in range(10)]
fire_name = list(filter(fire_in_name, random_names))

if fire_name:
    reduced_name = reduce(concatenate_names, fire_name)
else:
    reduced_name = "No names with 'Fire'"



if __name__ == '__main__':
    display()

