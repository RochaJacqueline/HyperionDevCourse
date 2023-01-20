# Task 1

def week_days():
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for days in week_days:
        print(days)


def second_hello():
    sentence = input("Please enter a sentence: ")
    words = sentence.split()
    words[1] = "Hello"
    sentence = ' '.join(words)
    print(sentence)

week_days()
second_hello()