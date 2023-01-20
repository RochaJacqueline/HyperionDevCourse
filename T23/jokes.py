# Task 2

import random

jokes = [
    "What did one pirate say to the other when he beat him at chess?<>Checkmatey." 
    "I burned 2000 calories today<>I left my food in the oven for too long.",
    "I startled my next-door neighbor with my new electric power tool. <>I had to calm him down by saying “Don’t worry, this is just a drill!”",
    "I broke my arm in two places. <>My doctor told me to stop going to those places.",
    "I quit my job at the coffee shop the other day. <>It was just the same old grind over and over.",
    "I never buy anything that has Velcro with it...<>it’s a total rip-off.",
    "I used to work at a soft drink can crushing company...<>it was soda pressing.",
]

random_index = random.randint(0, len(jokes) - 1)

print(jokes[random_index])