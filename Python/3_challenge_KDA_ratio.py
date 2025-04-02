def kill_death_assist():
    KDA = (kill+assist)/death
    print(f"Your KDA is {KDA}")

if __name__ == '__main__':
    kill = int(input("How many is your kill?: "))
    assist = int(input("How many is your assist?: "))
    death = int(input("How many is your death?: "))
    kill_death_assist()