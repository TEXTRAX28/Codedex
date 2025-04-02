import math
import random

def choice():
    planets = [
        ('Mercury', 2440),
        ('Venus', 6052),
        ('Earth', 6371),
        ('Mars', 3390),
        ('Saturn', 58232)
    ]
    ch = random.choice(planets)
    print(f"The planet is {ch}")
    area = 4 * math.pi * ch[1] ** 2
    return f"The area of {ch[0]} is {area:.2f}"

if __name__ == '__main__':
    print(choice())

