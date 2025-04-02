def moon_phase(phase):
    if phase == "new moon":
        return "🌑"
    elif phase == "waxing crescent":
        return "🌒"
    elif phase == "first quarter":
        return "🌓"
    elif phase == "waxing gibbous":
        return "🌔"
    elif phase == "full moon":
        return "🌕"
    elif phase == "waning gibbous":
        return "🌖"
    elif phase == "last quarter":
        return "🌗"
    elif phase == "waning crescent":
        return "🌘"
    else:
        return "Invalid input"

if __name__ == "__main__":
    answer = moon_phase('new moon')
    print(answer)