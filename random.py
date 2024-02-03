import random

#random(module):allows for generationof random numbers
#roll function:To randomly generate value of dice when rolled

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)

    return roll

value=roll()
print(value)