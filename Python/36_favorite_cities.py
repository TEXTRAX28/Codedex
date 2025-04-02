class city:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

city1 = city("Aurora City", "Celestia", 2500000, ["Ethereal Tower", "Moonlight Gardens", "Celestial Bridge"])
city2 = city("Verdantia", "Elaris", 1800000, ["Emerald Falls", "Verdant Spire", "Sunlit Plaza"])
city3 = city("Zephyria", "Aerilon", 3200000, ["Skyward Tower", "Nimbus Bay", "Horizon Market"])

print(vars(city))
print(vars(city1))
print(vars(city2))
print(vars(city3))