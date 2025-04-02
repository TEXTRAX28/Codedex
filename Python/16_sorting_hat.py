def question_1():
    global Gryffindor, Ravenclaw, Hufflepuff, Slytherin
    print("Do you like Dawn or Dusk?")
    print("1) Dawn")
    print("2) Dusk")
    input_1 = input("Enter your choice: ")

    if input_1 == "1":
        Gryffindor += 1
        Ravenclaw += 1
    elif input_1 == "2":
        Hufflepuff += 1
        Slytherin += 1
    else:
        print("Invalid input")

def question_2():
    global Gryffindor, Ravenclaw, Hufflepuff, Slytherin
    print("When I'm dead, I want people to remember me as")
    print("1) The Good")
    print("2) The Great")
    print("3) The Wise")
    print("4) The Bold")
    input_2 = input("Enter your choice: ")

    if input_2 == "1":
        Hufflepuff += 2
    elif input_2 == "2":
        Slytherin += 2
    elif input_2 == "3":
        Ravenclaw += 2
    elif input_2 == "4":
        Gryffindor += 2
    else:
        print("Invalid input")

def question_3():
    global Gryffindor, Ravenclaw, Hufflepuff, Slytherin
    print("Which kind of instrument most pleases your ear?")
    print("1) The violin")
    print("2) The trumpet")
    print("3) The piano")
    print("4) The drum")
    input_2 = input("Enter your choice: ")

    if input_2 == "1":
        Slytherin += 4
    elif input_2 == "2":
        Hufflepuff += 4
    elif input_2 == "3":
        Ravenclaw += 4
    elif input_2 == "4":
        Gryffindor += 4
    else:
        print("Invalid input")


if '__main__' == __name__:
    Gryffindor = 0
    Ravenclaw = 0
    Hufflepuff = 0
    Slytherin = 0

    question_1()
    question_2()
    question_3()

    print(f"Gryffindor: {Gryffindor}")
    print(f"Ravenclaw: {Ravenclaw}")
    print(f"Hufflepuff: {Hufflepuff}")
    print(f"Slytherin: {Slytherin}")