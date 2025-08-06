import os

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a task
def add_task(task, tasks):
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

# Remove a task
def remove_task(index, tasks):
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed task: {removed}")
    except IndexError:
        print("Invalid task number.")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main CLI loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task, tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to remove: ")) - 1
                remove_task(index, tasks)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
