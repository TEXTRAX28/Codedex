import random

def choices():
    symbols = ['🍒',' 🍇', '🍉', '7️⃣']
    random1 = random.choice(symbols)
    random2 = random.choice(symbols)
    random3 = random.choice(symbols)

    print(f"{random1} | {random2} | {random3}")

    if random1 == random2 == random3:
        print("Jackpot! 💰")
    else:
        print("Try again")

if __name__ == '__main__':
    choices()


