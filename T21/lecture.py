# Capstone II

# how to do GUI 

tasks_read = open('data.txt', 'r')
#

data = tasks_read.readlines()

for line in data:
    split_data = line.split(", ")

    output = '-----------------\n' # fsymbols.com
    output += f'Assigned to:\t\t\t{split_data[0]}'
    output += f'Task:\t\t\t{split_data[1]}'
    output += f'Description:\t\t\t{split_data[2]}'
    output += f'Assigned date:\t\t\t{split_data[3]}'
    output += f'Due date:\t\t\t{split_data[4]}'
    output += f'Is completed:\t\t\t{split_data[5]}'
    output += '\n'
    output += '-----------------\n'

    print(output)


for pos, line in enumerate(data, 1):
    split_data = line.split(", ")
    output = f'--------[{pos}]---------\n'
    output += f'Assigned to:\t\t\t{split_data[0]}'
    output += f'Task:\t\t\t{split_data[1]}'
    output += f'Description:\t\t\t{split_data[2]}'
    output += f'Assigned date:\t\t\t{split_data[3]}'
    output += f'Due daya:\t\t\t{split_data[4]}'
    output += f'Is completed:\t\t\t{split_data[5]}'
    output += '\n'
    output += '-----------------\n'

    print(output)

while True:
    task_choice = int(input("Please select a task number: "))-1

    if task_choice <= 0 or task_choice > len(data):
        print("You have selected an invalid option, try again.")
        continue

    edit_data = data[task_choice]
    #print(edit_data)
    break

while True:

    output = '---------[Select an option]-------\n'
    output += '1- Edit due date\n'
    output += '2- Mark as completed\n'
    output += '-----------------\n'

    choice = int(input(output))

    if choice <= 0 or choice >= 3:
        print(" Invalid option")
        continue

    if choice == 1:
        print("") #Todo I need to do this thing

    elif choice == 2:
        split_data = edit_data.split(", ")
        split_data[-1] = "Yes\n"
        new_data = ", ".join(split_data)
        data[task_choice] = new_data


    task_write = open('data.txt', 'w')
    for line in data:
        task_write.write(line)

    break

task_write.close()
tasks_read.close()
