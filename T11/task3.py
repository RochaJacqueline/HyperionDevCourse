# Task 3

# Requests user's inputs and saves them in cycling, running, and swimming  
cycling = int(input("Please enter how much time in minutes it took to complete the cycling event: "))
running = int(input("Please enter how much time in minutes it took to complete the running event: "))
swimming = int(input("Please enter how much time in minutes it took to complete the swimming event: "))
triathlon = cycling + running + swimming

# Creates conditions for different total times of triathlon, prints the result and respective award
if triathlon <= 100:
    print(f"The total time taken to complete the triathlon was {triathlon} minutes, and the award will be Provincial Colours.")

elif triathlon <= 105:
    print(f"The total time taken to complete the triathlon was {triathlon} minutes, and the award will be Provincial Half Colours.")

elif triathlon <= 110:
    print(f"The total time taken to complete the triathlon was {triathlon} minutes, and the award will be Provincial Scroll.")

else:
    print(f"The total time taken to complete the triathlon was {triathlon} minutes, and there will be no award.")