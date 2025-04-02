print("===================================")
print("Welcome To The Currency Calculator!")
print("===================================")

pesos = int(input("What do you have left in pesos?: "))
soles = int(input("What do you have left in soles?: "))
reais = int(input("What do you have left in reais?: "))

total = pesos*0.0002389 + soles*0.27 + reais*0.1745489

print(f"The total is: {total}")