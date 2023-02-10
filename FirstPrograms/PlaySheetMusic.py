
import pygame
import time
import tkinter as tk
from tkinter import Button, Label, messagebox, Entry, Text, Canvas
from functools import partial
import random


root = tk.Tk()
root.title("Decorate your musical staff")
root.geometry("500x300")
# Pygame music player
pygame.mixer.init()
piano_note = "Sound Files\g.mp3"

main_canvas = Canvas(root, bg="white", width=400, height=250)

# Where and what all the objects are
staff_line_positions = [[0, 40], [0, 60], [0, 80], [0, 100], [0, 120],
											  [0, 160], [0, 180], [0, 200], [0, 220], [0, 240]]
staff_measure_positions = [[]]
# list of buttons left on the staff
measure_buttons = [[]]
# list of measures labels that have replaced the buttons
measures = [[]]

# List of every single note that's been created
measure_texts = [[]]

# Create a time signiture (number of notes in a meausure, how fast to play - smaller numbers play faster - 4 is real time)
time_sig = (4, 4)



# Character codes
flat_sign = "\u266D"
sharp_sign = "\u266F"
quarter_note = "\u2669"
eighth_note = "\u266A"
half_rest = "𝄼"
whole_rest = "𝄻"


def draw_staff():
	for i in staff_line_positions:
		main_canvas.create_line(0, i[1], 400, i[1])


def draw_measures():
	# First Staff
	main_canvas.create_line(20, 40, 20, 120)
	for i in range(4):

		for j in range(6):

			x = 80 + 60 * j
			y = 40 + 20 * i
			main_canvas.create_line(x, y, x, y+20)
			staff_measure_positions.append([x-20, y])
	# Second Staff
	main_canvas.create_line(20, 160, 20, 240)
	for i in range(4):

		for j in range(6):

			x = 80 + 60 * j
			y = 160 + 20 * i
			main_canvas.create_line(x, y, x, y+20)
			staff_measure_positions.append([x-20, y])


def create_measures():
	for i in staff_measure_positions:
		measures.append(Label(root, text="", width=6, height=1))


def add_notes_to_measure(number):
	print("Add notes called")
	# Destroy button and add label
	measure_buttons[number].destroy()
	measures[number].place(x=staff_measure_positions[number]
	                       [0], y=staff_measure_positions[number][1])
	# create the text to insert
	# list of notes to choose and how many notes left in the measure
	notes_left = time_sig[0]
	available_notes = ['♩', '𝄼', '♪', '𝄻']
	#The text that each note will be added to and then be added to the total list
	measure_text = ""

	# use a formula to add notes without going over notes left in the measure
	while notes_left > 0:
		current_note = available_notes[random.randrange(len(available_notes))]
	
		if current_note == '♩' and notes_left >= 1:
			measure_text = measure_text + quarter_note + " "
			notes_left -= 1
			print("- added: " + current_note)
		elif current_note == '𝄼' and notes_left >= 2:
			# Make a lower chance for long pauses
			if random.randrange(10) > 7:
				measure_text = measure_text + " " + half_rest + " "
				notes_left -= 2
				print("- added: " + current_note)
		elif current_note == '𝄻' and notes_left > 3:
			# Make a lower chance for long pauses
			if random.randrange(10) > 7:
				measure_text = measure_text + "  " + whole_rest + "  "
				notes_left -= 4
				print("- added: " + current_note)
		elif current_note == '♪' and notes_left >= 0.5:
			measure_text = measure_text + eighth_note
			notes_left -= 0.5
			print("- added: " + current_note)
		print(str(notes_left) + " notes left")
	print(measure_text)
	# configure the label and add the created text to master text list
	measures[number].configure(text=measure_text)
	measure_texts.append(measure_text)


def create_note_buttons():
	# button number
	number = 0
	# add a button to the list of buttons
	for i in staff_measure_positions:
		measure_buttons.append(Button(root, text=" ", justify="left", command=partial(
		    add_notes_to_measure, number+1), width=6, height=1))
		number += 1


def add_note_buttons():
	for i in range(len(measure_buttons)-1):
		if i > 0:
			measure_buttons[i].place(x=staff_measure_positions[i]
			                         [0], y=staff_measure_positions[i][1])


def test_sound():
    print('test sound')
    print(measure_texts)
    pygame.mixer.music.load(piano_note)
    pygame.mixer.music.play(loops=0)


def play_song():
	print("playing song")
	for i in measure_texts:
		print("\nMeasure: " + str(i))
		for j in range(len(i)):
			print(" " + str(i[j]), end = " ")
			if i[j] == "\u2669":
				pygame.mixer.music.load(piano_note)
				pygame.mixer.music.play(loops=0)
				time.sleep(1*time_sig[1]/4)
			elif i[j] == "\u266A":
				pygame.mixer.music.load(piano_note)
				pygame.mixer.music.play(loops=0)
				time.sleep(0.5*time_sig[1]/4)
			elif i[j] == "𝄼":
				time.sleep(0.5*time_sig[1]/4)
			elif i[j] == "𝄻":
				time.sleep(1*time_sig[1]/4)
			
# add the canvas to the screen
main_canvas.pack()


# draw everything
draw_staff()
draw_measures()

create_note_buttons()
add_note_buttons()
create_measures()

# add buttons to the bottom of the window
play_button = Button(root, text = "Play", command = play_song).pack()
test_button = Button(root, text = "Test", command = test_sound).pack()

# main loop draws everything repeatedly
tk.mainloop()