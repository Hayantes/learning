to_do_list = []

def adding_tasks():
    more_tasks = True
    while more_tasks:
        task_name = input("Write here task you want to add: ")
        to_do_list.append(task_name)
        response = input("Do you want to add more tasks? (yes/no): ").strip().lower()
        more_tasks = response == "yes"
    return to_do_list

def view_task():
    print(to_do_list)
    return to_do_list

def complete_task():
    for i in range(len(to_do_list)):
        print(to_do_list[i])
        mark_as_completed = input("Do you want to mark this task as completed? (yes/no): ").strip().lower()
        if mark_as_completed == "yes":
            to_do_list[i] = to_do_list[i] + " [COMPLETED]"
            print(to_do_list)
        else:
            print(to_do_list)
            continue
    return to_do_list

def delete_task(to_do_list):
    if not to_do_list:  # Check if the list is empty
        print("Your to-do list is empty. Nothing to delete.")
        return to_do_list

    # Display all tasks with their indexes
    print("Your current to-do list:")
    for i, task in enumerate(to_do_list):
        print(f"{i + 1}. {task}")

    # Ask the user which task to delete
    try:
        task_index = int(input("Enter the number of the task you want to delete: ")) - 1  # Convert to zero-based index
        if 0 <= task_index < len(to_do_list):  # Check if the index is valid
            deleted_task = to_do_list.pop(task_index)  # Remove the task
            print(f"Task '{deleted_task}' has been deleted.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    # Print the updated list
    print("Updated to-do list:", to_do_list)
    return to_do_list

while True:
    print("Welcome to your To-Do list! Here is your menu where you can modify your To-Do list")
    print("Enter 1 to Add Tasks to your list")
    print("Enter 2 to View Tasks in your list")
    print("Enter 3 to Mark your tasks as completed")
    print("Enter 4 to delete your tasks")
    print("Enter 5 to exit from app")
    userChoice = int(input())
    if userChoice == 1:
        adding_tasks()
        print("Your to-do list:", to_do_list)
    elif userChoice == 2:
        view_task()
    elif userChoice == 3:
        complete_task()
    elif userChoice == 4:
        delete_task(to_do_list)
    else:
        print("Goodbye!")
        break


