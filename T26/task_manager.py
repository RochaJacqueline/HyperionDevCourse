#=====importing libraries===========

from datetime import datetime

users_file = open('user.txt', 'r+')
users_info = {}
is_admin = False

#====Classes Section========
class Task():
    def __init__(self, id, username, task_name, description, date_assigned, due_date, completed):
        self.id = id
        self.username = username
        self.task_name = task_name
        self.description = description
        self.date_assigned = date_assigned
        self.due_date = due_date
        self.completed = completed.rstrip('\n')

    def get_username(self):
        return self.username

    def print(self):
        print(f"""─────────────────────────────────────────────────────────────────────────────────
        ID:\t\t\t{self.id}
        Task:\t\t\t{self.task_name}
        Assigned to:\t\t{self.username}
        Date assigned:\t\t{self.date_assigned}
        Due date:\t\t{self.due_date}
        Task completed:\t\t{self.completed}
        Task description:\t{self.description}
        """)

    def __str__(self):
        return f"{self.username}, {self.task_name}, {self.description}, {self.date_assigned}, {self.due_date}, {self.completed}\n"

    def is_completed(self):
        return self.completed == "Yes"

    def set_completed(self):
        self.completed = "Yes"

    def edit(self, username, due_date):
        self.username = username
        self.due_date = due_date

    def is_overdue(self):
        if (self.is_completed()): 
            return False

        now = datetime.now()
        due_date = datetime.strptime(self.due_date, '%d %b %Y')
        return now > due_date

#====Functions Section=========
def reg_user():
    while True:
        name_input = input("Please enter an username: ")

        if name_input in users_info:
            print("This username already exists. Please enter a different username.")
            continue

        password_input = input("Please enter a password: ")
        new_password = input("Please enter the same password again: ")

        if name_input in users_file:
            print("The username is already registered. You can register another one.")
        elif password_input != new_password:
            print("You did not enter the right password. Try again.")
        else:
            users_file.write(f"\n{name_input}, {password_input}")
            print("User added successfully.")
            break

def add_task():
    tasks_file = open('tasks.txt', 'a')

    name_input = input("Please enter an username: ")
    task_name = input("Please enter the title of the task: ")
    task_description = input("Please enter the description of the task: ")
    due_date = input("Please enter the due date of the task in the format: day month year ")
        
    # Gets the current date and formats it according to the date in tasks.txt file
    current_date = datetime.strftime(datetime.now(), '%d %b %Y')

    tasks_file.write(f"\n{name_input}, {task_name}, {task_description}, {current_date}, {due_date}, No")
    tasks_file.close()

def read_tasks():
    '''Function that reads all tasks from tasks.txt and returns them in a dictionary'''
    tasks = {}
    tasks_file = open('tasks.txt', 'r')
    for i, line in enumerate(tasks_file, 1):
        id = str(i)
        username, task_name, description, date_assigned, due_date, completed = line.split(", ")
        task = Task(id, username, task_name, description, date_assigned, due_date, completed)
        tasks[id] = task

    tasks_file.close()  
    return tasks

def write_tasks(tasks):
    '''Function that takes a list of tasks and writes to tasks.txt'''
    tasks_file = open('tasks.txt', 'w')
    for task in tasks:
        tasks_file.write(task.__str__())
    tasks_file.close()

def view_all():
    '''Prints all tasks'''
    tasks = read_tasks()
    for task in tasks.values():
        task.print()

def select_task_menu(tasks):
    '''Prompts a menu for the user to choose a task to edit'''
    for key, task in tasks.items():
        print(key)
        print(task)
        
    while True:
        task_id = input("Please select a task id (or -1 to exit): ")
        if (task_id == "-1"):
            return

        if (task_id not in tasks):
            print("Task does not exist")
            continue

        if (tasks[task_id].is_completed()):
            print("Cannot edit completed task")
            continue
        
        return tasks[task_id]

def edit_task_menu(task):
    '''Prompts a menu for the user to edit a task'''

    while True:
        option = input('''Select one of the following Options below:
    m - Mark as completed
    e - Edit task: ''').lower()

        if (option == 'm'):
            task.set_completed()
            break

        elif (option == 'e'):
            new_username = input("Please enter an username: ")
            new_due_date = input("Please enter the due date of the task in the format: day month year ")
            task.edit(new_username, new_due_date)
            break

        else:
            print("Invalid option!")

def view_mine():
    '''Prints the current user's tasks and prompts them to edit'''
    tasks = read_tasks()
    user_tasks = {}

    for id, task in tasks.items():
        if (task.get_username() == name_input):
            user_tasks[id] = task
        
    for task in user_tasks.values():
        task.print()
        
    task = select_task_menu(user_tasks)
    if (task != None):
        edit_task_menu(task)
        write_tasks(tasks.values())

def generate_task_report(tasks):
    task_report = open("task_overview.txt", "w")

    total_tasks = len(tasks)
    completed_tasks = 0
    overdue_tasks = 0

    for task in tasks:
        if (task.is_completed()):
            completed_tasks += 1

        if (task.is_overdue()):
            overdue_tasks += 1

    incompleted_tasks = total_tasks - completed_tasks
    incompleted_pct = incompleted_tasks / total_tasks
    overdue_pct = overdue_tasks / total_tasks

    report = f"""Number of tasks:\t\t{total_tasks}
        Completed tasks:\t\t{completed_tasks}
        Incomplete tasks:\t\t{incompleted_tasks}
        Incomplete percentage:\t\t{100*incompleted_pct:.2f}%
        Overdue tasks:\t\t{overdue_tasks}
        Overdue percentage:\t\t{100*overdue_pct:.2f}%
        """

    task_report.write(report)
    task_report.close()

def generate_user_report(users, tasks):
    user_report = open("user_overview.txt", "w")
    total_users = len(users)
    total_tasks = len(tasks)

    user_report.write(f"""Number of registered users:\t{total_users}
Number of generated tasks:\t{total_tasks}\n\n""")

    user_tasks_dict = {}
    for user in users:
        user_tasks_dict[user] = []

    for task in tasks:
        user_tasks_dict[task.get_username()].append(task)
    
    for user, user_tasks in user_tasks_dict.items():
        total_assigned = len(user_tasks)
        if (total_assigned > 0):
            pct_assigned = total_assigned / total_tasks
            total_completed = 0
            total_overdue = 0
            for task in user_tasks:
                if (task.is_completed()):
                    total_completed += 1

                if (task.is_overdue()):
                    total_overdue += 1
            
            pct_completed = total_completed / total_assigned
            pct_incomplete = 1 - pct_completed
            pct_overdue = total_overdue / total_assigned

            report = f"""─────────────────────────────────────────────────────────────────────────────────
User:\t\t\t\t\t\t\t{user}
Number of tasks assigned:\t\t{total_assigned}
Total tasks percentage:\t\t\t{100*pct_assigned:.2f}%
Complete tasks percentage:\t\t{100*pct_completed:.2f}%
Incomplete tasks percentage:\t{100*pct_incomplete:.2f}%
Overdue percentage:\t\t\t\t{100*pct_overdue:.2f}%
"""
        else:
           report = f"""─────────────────────────────────────────────────────────────────────────────────
User:\t\t\t\t\t\t\t{user}
Number of tasks assigned:\t\t{total_assigned}
"""
    
        user_report.write(report) 

    user_report.close()
    
#====Login Section=========

# Saves all usernames and passwords from user.txt, in users_info as a list
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
    # Presenting the menu to the user and making sure that the user input is coneverted to lower case.
    if is_admin:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate report
    ds - Display statistics 
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
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'ds' and is_admin:
        
        tasks_file = open('tasks.txt', 'r')
        
        tasks = len(tasks_file.readlines())
        print(f"\nThe total number of tasks is: {tasks}")
        # Resets the users_file to beginning
        users_file.seek(0,0)
        users = len(users_file.readlines())
        print(f"\nThe total number of users is: {users}\n")

        tasks_file.close()

    elif menu == 'gr' and is_admin:
        tasks = read_tasks()
        generate_task_report(tasks.values())
        generate_user_report(users_info, tasks.values())

    elif menu == 'e':
        print('Goodbye!!!')
        users_file.close()
        exit()

    else:
        print("You have made a wrong choice. Please Try again")