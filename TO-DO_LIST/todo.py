tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(index, "-", task)

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully.")

def delete_task():
    show_tasks()
    task_no = int(input("Enter task number to delete: "))
    if 1 <= task_no <= len(tasks):
        tasks.pop(task_no - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- TO DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice.")

main()
