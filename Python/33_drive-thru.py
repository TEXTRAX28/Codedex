def get_item():
    list_item = []
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")
    while True:
        item_choice = int(input("What do you want?: "))
        if item_choice == 1:
            list_item.append("Cheeseburger")
        elif item_choice == 2:
            list_item.append("Fries")
        elif item_choice == 3:
            list_item.append("Soda")
        elif item_choice == 4:
            list_item.append("Ice Cream")
        elif item_choice == 5:
            list_item.append("Cookie")
        else:
            print("Invalid number")
            continue

        choice = input("Anything else? (y/n): ").lower()
        if choice == "y":
            continue
        elif choice == "n":
            print("Thank you!, Your order is:")
            for value,item in enumerate(list_item):
                print(f"{value+1}. {item}")
            break
        else:
            print("Invalid input")

def welcome():
    print("=======================")
    print("Welcome to McDonald's!")
    print("=======================")

if __name__ == "__main__":
    welcome()
    get_item()


