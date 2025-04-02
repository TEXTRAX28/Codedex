def dog_years(name, age):
    age = age * 7

    return f"{name} is {age} human years old"

if __name__ == '__main__':
    print(dog_years('Landon', 3))
    print(dog_years('Red Bean', 6))
    print(dog_years('Cooper', 2))