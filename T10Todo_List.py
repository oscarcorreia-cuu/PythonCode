import os

# Function to add a new task to the to-do list
def add_task(filename):
    try:
        task = input("Enter the task to add: ")
        with open(filename, 'a') as file:
            file.write(task + '\n')
        print(f"Task '{task}' added successfully.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

# Function to view all tasks in the to-do list
def view_tasks(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        with open(filename, 'r') as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks available.")
        else:
            print("To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

# Function to delete a specific task from the to-do list
def delete_task(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        with open(filename, 'r') as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks available to delete.")
            return

        view_tasks(filename)  # Show current tasks
        task_num = int(input("Enter the number of the task to delete: "))

        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            with open(filename, 'w') as file:
                file.writelines(tasks)
            print(f"Task '{deleted_task.strip()}' deleted successfully.")
        else:
            print("Invalid task number. Please try again.")

    except FileNotFoundError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
    except IOError as e:
        print(f"An error occurred while modifying the file: {e}")

# Main function to manage the to-do list
def todo_list_manager():
    filename = 'todo_list.txt'

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task(filename)
            elif choice == 2:
                view_tasks(filename)
            elif choice == 3:
                delete_task(filename)
            elif choice == 4:
                print("Exiting the To-Do List Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the To-Do List Manager
todo_list_manager()
