def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def exponent(a,b):
    return a ** b

if __name__ == '__main__':
    print("This is a calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    choice = int(input("Choose one: "))
    if choice == 1:
        input_a = int(input("Enter a: "))
        input_b = int(input("Enter b: "))
        print(f"The result of {input_a} + {input_b} = {add(input_a,input_b)}")
    elif choice == 2:
        input_a = int(input("Enter a: "))
        input_b = int(input("Enter b: "))
        print(f"The result of {input_a} - {input_b} = {subtract(input_a,input_b)}")
    elif choice == 3:
        input_a = int(input("Enter a: "))
        input_b = int(input("Enter b: "))
        print(f"The result of {input_a} x {input_b} = {multiply(input_a,input_b)}")
    elif choice == 4:
        input_a = int(input("Enter a: "))
        input_b = int(input("Enter b: "))
        print(f"The result of {input_a} : {input_b} = {divide(input_a,input_b)}")
    elif choice == 5:
        input_a = int(input("Enter a: "))
        input_b = int(input("Enter b: "))
        print(f"The result of {input_a} ** {input_b} = {exponent(input_a,input_b)}")


