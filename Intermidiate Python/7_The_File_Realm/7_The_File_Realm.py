liked_songs = {
    "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Ghost": "Justin Bieber"
}

def write_liked_songs_to_file(liked_songs, file_name='liked_songs.txt'):
    with open("liked_songs.txt", 'w') as f:
        f.write("Liked Songs:\n")
        for song,name in liked_songs.items(): #.items to return keys and value
            f.write(f"{song} by {name}\n")

def write_liked_songs_to_file_seperate_keys_and_values(liked_songs, file_name='liked_songs_keys.txt'):
    with open("liked_songs_keys.txt", 'w') as f:
        f.write("Artist:\n")
        for song in liked_songs.keys():
            f.write(f"{song}\n")
        f.write(f"\n")

        f.write("Album:\n")
        for song in liked_songs.keys():
            f.write(f"{song}\n")

write_liked_songs_to_file(liked_songs)
write_liked_songs_to_file_seperate_keys_and_values(liked_songs)