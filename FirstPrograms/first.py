import random

flat_sign = "\u266D"
sharp_sign = "\u266F"
quarter_note = "\u2669 "
eighth_note = "\u266A"
half_rest = "rest "
whole_rest = "w rest "

#List of greetings to be chosen at random
greetings = {"hello", "Hi there", "Wazzuuhh"}

#Print a random greeting by sampling it with the random method
print(random.sample(greetings, 1))

available_notes = {quarter_note, eighth_note, half_rest, whole_rest}

current_note = random.sample(available_notes, 1)

print(current_note)