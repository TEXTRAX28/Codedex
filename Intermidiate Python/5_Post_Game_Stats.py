# List of players
players = [
    {
        "name": "Patrick Mahomes",
        "position": "Quarterback",
        "jersey_number": 15,
        "yards_gained": 300,
        "touchdowns": 3
    },
    {
        "name": "Travis Kelce",
        "position": "Tight End",
        "jersey_number": 87,
        "yards_gained": 120,
        "touchdowns": 2
    },
    {
        "name": "Tyreek Hill",
        "position": "Wide Receiver",
        "jersey_number": 10,
        "yards_gained": 150,
        "touchdowns": 1
    },
    {
        "name": "Clyde Edwards-Helaire",
        "position": "Running Back",
        "jersey_number": 25,
        "yards_gained": 60,
        "touchdowns": 0
    }
]

#print out all the player name in the dictionary
for player in players:
    print(player["name"])

#edit the value
player = []
for player in players:
    if player["name"] == "Clyde Edwards-Helaire":
        player["yards_gained"] += 40
        player["touchdowns"] += 1
        print(player)

#delete in a dictionary
for player in players:
    if player["name"] == "Tyreek Hill":
        player.pop("yards_gained")
        print(player)

#changing the jersey number in Patrick Mahomes to 23
for player in players:
    if player["name"] == "Patrick Mahomes":
        player["jersey_number"] = 23
        print(player)
