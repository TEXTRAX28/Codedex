class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def __bool__(self):
        return self.is_caught

    def speak(self):
        print(self.name)
        print(self.name)

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")
        if self.is_caught == True:
            print(f"{self.name} has been caught")
        else:
            print(f"{self.name} has not been caught")

if __name__ == "__main__":
    pokemon1 = Pokemon(25, "Pikachu", "Electric", "It has small electric sacs on both its cheeks. If threatened, it loose electric charges from the sacs", True)
    # if pokemon1.is_caught == True:
    pokemon1.display_details()