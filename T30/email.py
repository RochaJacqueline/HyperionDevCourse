#An Email Simulation

#====Class Section========

class Email():
    def __init__(self, email_contents, from_address):
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

    def __str__(self) -> str:
        return f"From: {self.from_address}\n{self.email_contents}"

#====Functions Section=======

def add_email(contents, address):
    inbox.append(Email(contents, address))

def get_count():
    return len(inbox)

def get_email(i):
    # Iterates over inbox, marks it as read and shows emails contents
    if i in range(0, len(inbox)):
        inbox[i].mark_as_read()
        return inbox[i].email_contents

def get_unread_emails():
    unread_emails = []
    # Iterates over inbox, and adds unread emails to a new list
    for email in inbox:
        if not email.has_been_read:
            unread_emails.append(email)
    return unread_emails

def get_spam_emails():
    spam_emails = []
    # Iterates over inbox, and adds spam emails to a new list
    for email in inbox:
        if email.is_spam:
            spam_emails.append(email)
    return spam_emails

def delete(i):
    if i in range(0, len(inbox)):
        inbox.pop(i)

def show_all_emails():
    """ Prints all email's contents available in inbox, with their indices """
    count = get_count()

    if count == 0:
            print(f"\nThere are no emails in the list.")
    else:
        print(f"\nThere are {count} emails in the list:")
        # Prints index and email's content in the format: index - content
        for i in range(count):
            print(f"{i} - {inbox[i].email_contents}")

def print_emails(emails):
    """ Prints list of emails """
    for email in emails:
        print(f"{str(email)}\n")

inbox = []
user_choice = ""

while user_choice != "quit":
    # Gets user's menu choice
    user_choice = input("What would you like to do - read/mark spam/send/show unread/show spam/delete/quit? ")
    
    if user_choice == "read":
        show_all_emails()

        email_index = int(input("\nPlease enter the email index: "))
        # Saves email's content for a certain email index
        email = get_email(email_index)
        # If there is no contents for user's chosen index, prints an error message. Otherwise prints contents
        if email == None:
            print("Error: the email does not exist.")
        else:
            print(get_email(email_index))

    elif user_choice == "mark spam":
        show_all_emails()
        # Marks an email chosen by user as spam 
        email_index = int(input("\nPlease enter the email index: "))
        inbox[email_index].mark_as_spam()

    elif user_choice == "send":
        # Promps the user for email's content and address
        content = input("Please enter the email content: ")
        address = input("Please enter the email address of the sender: ")
        add_email(content, address)

    elif user_choice == "show unread":
        # Prints all unread emails
        print_emails(get_unread_emails())

    elif user_choice == "show spam":
        # Prints all spam emails
        print_emails(get_spam_emails())

    elif user_choice == "delete":
        show_all_emails()
        email_index = int(input("\nPlease enter the index of the email to be deleted: "))
        # Saves email's content for a certain email index
        email = get_email(email_index)
        # If there is no contents for user's chosen index, prints an error message. Otherwise deletes email from inbox
        if email == None:
            print("Error: the email does not exist.")
        else:
            delete(email_index)

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
