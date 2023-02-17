# T30
# email.com

class Email():
    def __init__(self, from_address, subject_line, email_contents, has_been_read, is_spam):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False 

    def mark_as_spam(self):
        self.is_spam = True

    def get_subject_line(self):
        return self.subject_line    

    def mark_as_read(self):
        self.has_been_read = True

    def __str__(self):
        output = f"From: {self.from_address}\n\n"
        output += f"Content: \n {self.email_contents}"

inbox = []

inbox.append(Email("a", "a", "hahahha"))
inbox.append(Email("b", "b", "hahahha"))
inbox.append(Email("c", "c", "hahahha"))
inbox.append(Email("d", "d", "hahahha"))

def get_email():
    for index, email in enumerate(inbox, 1):
        print(f"{index}. {email.get_subject_line()}")

    choice = int(input("Enter email index: ")) - 1

    email = inbox[choice]
    print(email)
    email.mark_as_read()

get_email()