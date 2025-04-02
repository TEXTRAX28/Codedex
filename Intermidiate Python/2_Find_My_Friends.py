from geopy.distance import geodesic
my_location = (54.9784 , -1.6174) #latitude and longitude respectively

friend_1 = (40.7128, -74.0060) #latitude and longitude respectively
friend_2 = (35.6895, 139.6917) #latitude and longitude respectively
friend_3 = (-33.8688, 151.2093) #latitude and longitude respectively

all_location = (my_location[0], friend_1[0], friend_2[0], friend_3[0])

print("========")
print("Location")
print("========")
print(f"My Location: {my_location}")
print(f"Friend 1: {friend_1}")
print(f"Friend 2: {friend_2}")
print(f"Friend 3: {friend_3}\n")

print("========")
print("Distance")
print("========")
distance = geodesic(friend_1, my_location)
print(f"Distance: {distance}")

