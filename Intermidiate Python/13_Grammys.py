# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42),
            ('Just Like That', 5.05),
            ('Song 3', 6.8),
            ('Leave The Door Open', 4.02),
            ('I Can\'t Breath', 4.47),
            ('Bad Guy', 3.14)]

def duration_more_than_5(song):
    return song[1] > 5

def minute_to_second(minute):
    return minute[1]*60

def add_all_duration(add):
    return add[1] + add[2] + add[3]

filter_playlist = list(filter(duration_more_than_5, playlist))
print(filter_playlist)

map_playlist = list(map(minute_to_second, playlist))
print(map_playlist)




