#=====importing libraries===========

from datetime import datetime

users_file = open('user.txt', 'r+')
users_info = {}
is_admin = False

#====Login Section====

# Saves all usernames and passwords from user.txt, in users_info as a dictionary
for line in users_file:
    login, password = line.split(', ')
    users_info[login] = password.strip("\n")

while True:
    name_input = input("Please type your username: ")
    password_input = input("Please type your password: ")

    if users_info.get(name_input) == None:
        print("Error: you didn't enter a valid username. Try again.")
    elif users_info[name_input] != password_input:
        print("Error: you didn't enter a valid password. Try again.") 
    else:
        is_admin = name_input.lower() == "admin"
        break

while True:
    #presenting the menu to the user and making sure that the user input is coneverted to lower case.
    if is_admin:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    s - Statistics
    e - Exit
    : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()

    if menu == 'r':
        if not is_admin:
            print("Sorry, you're not allowed to register users.")
            continue
        
        name_input = input("Please enter an username: ")
        password_input = input("Please enter a password: ")
        new_password = input("Please enter the same password again: ")
        
        if password_input != new_password:
            print("You did not enter the right password. Try again.")
        else:
            users_file.write(f"\n{name_input}, {password_input}")
            print("User added successfully.")

    elif menu == 'a':
        tasks_file = open('tasks.txt', 'a')

        name_input = input("Please enter an username: ")
        task_name = input("Please enter the title of the task: ")
        task_description = input("Please enter the description of the task: ")
        due_date = input("Please enter the due date of the task in the format: day month year ")
        
        # Gets the current date and formats it according to the date in tasks.txt file
        current_date = datetime.strftime(datetime.now(), '%d %b %Y')

        tasks_file.write(f"\n{name_input}, {task_name}, {task_description}, {current_date}, {due_date}, No")
        tasks_file.close()

    elif menu == 'va':
        tasks_file = open('tasks.txt', 'r')
        for line in tasks_file:
            username, task, description, date_assigned, due_date, completed = line.split(", ")

            print("─────────────────────────────────────────────────────────────────────────────────\n")
            print(f"Task:\t\t\t{task}\n")
            print(f"Assigned to:\t\t{username}\n")
            print(f"Date assigned:\t\t{date_assigned}\n")
            print(f"Due date:\t\t{due_date}\n")
            print(f"Task completed:\t\t{completed}\n")
            print(f"Task description:\t{description}\n")

        tasks_file.close()

    elif menu == 'vm':
        
        tasks_file = open("tasks.txt", 'r')
        for line in tasks_file:
            username, task, description, date_assigned, due_date, completed = line.split(", ")
        
            if name_input == username:
                print("─────────────────────────────────────────────────────────────────────────────────\n")
                print(f"Task:\t\t\t{task}\n")
                print(f"Assigned to:\t\t{username}\n")
                print(f"Date assigned:\t\t{date_assigned}\n")
                print(f"Due date:\t\t{due_date}\n")
                print(f"Task completed:\t\t{completed}\n")
                print(f"Task description:\t{description}\n")

        tasks_file.close()

    elif menu == 's' and is_admin:
        '''In this block you will put code that will display statistics, i.e. the total number of tasks and total number of users'''
        tasks_file = open('tasks.txt', 'r')
        
        tasks = len(tasks_file.readlines())
        print(f"\nThe total number of tasks is: {tasks}")
        # Resets the users_file to beginning
        users_file.seek(0,0)
        users = len(users_file.readlines())
        print(f"\nThe total number of users is: {users}\n")

        tasks_file.close()

    elif menu == 'e':
        print('Goodbye!!!')
        users_file.close()
        exit()

    else:
        print("You have made a wrong choice, Please Try again")