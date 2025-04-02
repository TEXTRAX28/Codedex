import json

data = "task.json"

def load_task():
    try:
        with open(data, 'r') as file:
            content = file.read().strip()
            return json.loads(content) if content else []
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_task(task):
    with open(data, 'w') as file:
        json.dump(task, file, indent=4)


def add_task(task):
    tasks = load_task()
    if not any(t["task"] == task for t in tasks):
        tasks.append({"task": task, "completed": False})
        save_task(tasks)
        print(f"Added task: {task}")

    while True:
        input_add_task = input("Do you want to add another task? (y/n): ").lower()
        if input_add_task == "n":
            break
        else:
            next_task = input("Enter the next task: ").lower()
            if any(t["task"] == next_task for t in tasks):
                print("You already have this task.")
            else:
                tasks.append({"task": next_task, "completed": False})
                save_task(tasks)
                print(f"Added task: {next_task}")


def view_task():
    tasks = load_task()
    print("Your To-Do list:")
    if not tasks:
        print("No task available")
        return
    else:
        display()


def complete_task(input_complete):
    tasks = load_task()
    if 1 <= input_complete <= len(tasks):
        tasks[input_complete - 1]["completed"] = True
        save_task(tasks)
        print(f"Completed task: {tasks[input_complete-1]['task']}")
    else:
        print(f"Invalid task")


def remove_task(input_remove):
    tasks = load_task()
    if 1 <= input_remove <= len(tasks):
        remove_input = tasks[input_remove-1]["task"]
        tasks.pop(input_remove-1)
        save_task(tasks)
        print(f"Removed task: {remove_input}")
    else:
        print("Invalid task")

def display():
    tasks = load_task()
    for i, value in enumerate(tasks, start=1):
        status = "[✓]" if value["completed"] else "[ ]"
        print(f"{i}. {value['task']} - {status}")



def main():
    print("===============")
    print("To-Do List")
    print("===============")

    while True:
        print("1. View Task")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Remove Task")
        user_input = int(input("Enter your choice: "))

        if user_input == 1: #viewing the current task
            view_task()
        elif user_input == 2: #adding the task
            input_add = input("Enter your task: ").lower()
            add_task(input_add)
        elif user_input == 3: #mark as complete
            tasks = load_task()
            display()
            input_complete = int(input("Enter your task that you want to mark as complete: "))
            complete_task(input_complete)
        elif user_input == 4: #removing the task
            display()
            input_remove = int(input("Enter your task: "))
            remove_task(input_remove)
            display()
        else:
            print("Invalid Input")

        input_loop = input("Do you want to continue? (y/n): ").lower()
        if input_loop == "n":
            break
        else:
            continue


if __name__ == '__main__':
    main()


