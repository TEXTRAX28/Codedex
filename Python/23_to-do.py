todo_list = ["Get quarters", "Do laundry", "Take a walk", "Get a haircut", "Make some tea", "Complete Lists chapter", "Call mom", "Watch My Hero Academie"]

print(todo_list[0])
print(todo_list[1])
print(todo_list[2:5])
try:
    print(todo_list[9])
except IndexError:
    print("Invalid input")