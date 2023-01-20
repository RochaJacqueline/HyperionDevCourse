# error handling

# GUI: tkinter

while True:
    try:
        choice =  int(input("Enter a number: "))
        print(choice)
        break
    except ValueError:
        print("You entered a word, not a number.")
        choice = "ERR"
    except FileExistsError:
        print("The file doesn't existe?")


if choice == "ERR":
    print("Hey this program crashed.")
else:
    print(choice)