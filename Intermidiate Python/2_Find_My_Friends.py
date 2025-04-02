# My location (Newcastle, UK)
my_location = (54.9784, -1.6174)

# Friends' locations (get from chatgpt)
friend_1 = (40.7128, -74.0060)  # New York, USA
friend_2 = (35.6895, 139.6917)  # Tokyo, Japan
friend_3 = (-33.8688, 151.2093) # Sydney, Australia

print(my_location,friend_1, friend_2, friend_3)

def estimate_distance(location1, location2):
    return abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])

if __name__ == '__main__':
    distances = {
        "New York": estimate_distance(my_location, friend_1),
        "Tokyo": estimate_distance(my_location, friend_2),
        "Sydney": estimate_distance(my_location, friend_2)
    }

    furthest_distance = max(distances, key= distances.get)

    print(f"The furthest distance from me is {distances}, with an estimated distance of {distances[furthest_distance]}")











