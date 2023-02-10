import tkinter as tk
from tkinter import Label, messagebox, Button, Entry, Text, END
import random
""" Define main window"""
root = tk.Tk()
root.title("Hello wold")
root.geometry("500x750")

""" To DO 
		
		- make commands use more values rather than "self" allow player.name or enemy.name allow "enemy"

		- make a shop for potions

		- make functions to do the basic arithmetic so that code is 
		  cleaner and better
			set_health() can be callled inside player and not changed in
			attack_enemy
"""

# define important variables
global response # worked for a while then became local so it was made to be global
global user_input # worked for a while then became local so it was made to be global
user_input = tk.StringVar()
response = tk.StringVar()
START = 1.0

global player # worked for a while then became local so it was made to be global

main_entry = Entry(root, textvariable=user_input)
main_label = Label(root)
main_text = Text(root, width=52, height=9)
battle_text = Text(root, width=52, height=3)
main_button = Button(root, text="Proceed")
show_response = Label(root)

## Define classes


class Player():
    def __init__(self):
        self.name = tk.StringVar()
        self.Class = tk.StringVar()
        self.min_attack = 5
        self.max_attack = 10
        self.max_health = 60
        self.potion_heal_amount = 20
        self.potion_count = 2
        self.health = self.max_health
        self.level = 1
        self.enemy = Enemy()
        self.gold = 5
        # Initial Game State variables
        self.first_fight = True
        self.given_name = False
        self.given_class = False
        #battle, home
        self.state = "battle"

        self.labels = Label(
            root, text=str(self.name) + " Health: " + str(self.health)), Label(
                root, text="Level: " + str(self.level)), Label(
                    root, text="Potions: " + str(self.potion_count)), Label(
                        root, text="Loot: " + str(self.gold) + " gold!")

    # Deal with death
    def die(self):
        Game_Over()

    ## Deal with labels
    def show_labels(self):
        for i in self.labels:
            i.pack()

    def destroy_labels(self):
        for i in self.labels:
            i.destroy()
        self.labels = Label(
            root, text=str(self.name) + " Health: " + str(self.health)), Label(
                root, text="Level: " + str(self.level)), Label(
                    root, text="Potions: " + str(self.potion_count)), Label(
                        root, text="Gold: " + str(self.gold))

    def configure_labels(self):
        self.labels[0].configure(text=str(self.name) + " Health: " +
                                 str(self.health))
        self.labels[1].configure(text="Level: " + str(self.level))
        self.labels[2].configure(text="Potions: " + str(self.potion_count))
        self.labels[3].configure(text="Gold: " + str(self.gold))


class Enemy():
    def __init__(self):
        self.names = ("Ghost", "Zombie", "Skeleton")
        self.name = self.names[random.randrange(0, len(self.names))]
        self.min_attack = 5
        self.max_attack = 10
        self.min_health = 15
        self.max_health = 25
        self.health = random.randrange(self.min_health, self.max_health)
        self.level = 1
        self.gold = random.randrange(0, 2 * self.level)

        self.labels = Label(root,
                            text=str(self.name) + " Health: " +
                            str(self.health)), Label(
                                root, text="Level: " + str(self.level)), Label(
                                    root,
                                    text="Loot: " + str(self.gold) + " gold!")

    ## Deal with death
    def die(self):
        self.set_loot()
        show_response.configure(text="enemy died")

        if player.first_fight:
            player.first_fight = False
            New_Enemy(player)
            debrief()

        else:
            New_Enemy(player)

    def set_loot(self):
        self.has_gold = random.randrange(3)
        if self.has_gold > 1:
            self.gold = random.randrange(1 * self.level, 3 * self.level)
            player.gold += self.gold
            self.labels[2].configure(text=str(self.gold) + " gold")
        else:
            self.labels[2].configure(text="no gold for you")

    ## Deal with Labels
    def show_labels(self):
        for i in self.labels:
            i.pack()

    def destroy_labels(self):
        for i in self.labels:
            i.destroy()
        self.labels = Label(root,
                            text=str(self.name) + " Health: " +
                            str(self.health)), Label(
                                root, text="Level: " + str(self.level)), Label(
                                    root,
                                    text="Loot: " + str(self.gold) + " gold!")

    def configure_labels(self):
        self.labels[0].configure(text=str(self.name) + " Health: " +
                                 str(self.health))
        self.labels[1].configure(text="Level: " + str(self.level))
        self.labels[2].configure(text="Loot: " + str(self.gold) + " gold!")


## Define functions


## Go home
def go_home():
    battle_text.pack_forget()
    player.enemy.destroy_labels()
    player.destroy_labels()
    main_text.delete(START, END)

    player.state = "home"
    root.title("Home")
    main_label.config(text="Home sweet home! <3")
    player.configure_labels()
    player.show_labels()
    main_text.insert(
        END, "Welcome home\nPotion:\nself\n\nInventory:\nself\n\nGo:\nfight\n")


## Go fight
def go_fight():

    battle_text.pack_forget()
    battle_text.delete(START, END)
    player.enemy.destroy_labels()
    player.destroy_labels()
    main_text.delete(START, END)

    player.state = "battle"
    root.title("Battlefield")
    main_label.config(text="Battle")
    battle_text.pack()
    New_Enemy(player)

    player.configure_labels()
    player.enemy.configure_labels()
    player.show_labels()
    player.enemy.show_labels()


## Show Inventory
def show_inventory():
    battle_text.pack_forget()
    player.enemy.destroy_labels()
    player.destroy_labels()
    main_text.delete(START, END)

    root.title("Inventory")
    main_label.config(text="checking items")

    player.configure_labels()
    player.show_labels()


## RUN COMMAND
def run_command():
    command_and_point = user_input.get().strip().split(" ")
    command = command_and_point[0]
    point = command_and_point[1]
    if len(command_and_point) > 2:
        extra = command_and_point[2]
    main_entry.delete(0, END)
    response = "invalid command"

    if command.lower() == "name":
        if not player.given_name:
            player.name = point
            player.given_name = True
            response = "Named player: " + player.name
            select_class()
        else:
            response = "use command: \"Rename self [value]\""

    elif command.lower() == "class":
        if not player.given_class:
            player.Class = point
            player.given_class = True
            response = " given class " + player.Class
            mock_fight()
        else:
            response = "you cannot change your class"

    elif command.lower() == "rename":
        if point == "self":
            response = "renamed " + str(player.name) + " to " + str(extra)
            player.name = str(extra)

    elif command.lower() == "attack":
        if point == "self":
            attack_enemy(player, player)
            response = "attacked self"
        elif point.lower() == str(player.enemy.name).lower():
            attack_enemy(player, player.enemy)
            response = "attacked enemy"

    elif command.lower() == "potion":
        if player.potion_count < 1:
            response = "You have no potions left"
        elif point == "self":
            if player.health <= player.max_health - player.potion_heal_amount:
                player.health += player.potion_heal_amount
                player.potion_count -= 1
                response = "drank a potion"
            else:
                response = "You're in good shape don't waste it"
        elif point == str(player.enemy.name).lower():
            player.enemy.health += player.potion_heal_amount
            player.potion_count -= 1
            response = "Why did you do that?"

    elif command.lower() == "run":
        go_home()
        response = "ran home"

    elif command.lower() == "inventory":
        if player.state != "battle":
            if point == "self":
                show_inventory()
                response = "looking at inventory"
        else:
            response = "you are in battle"

    elif command.lower() == "go":
        if point == "fight":
            go_fight()
            response = "going to battle"
        if point == "home":
            go_home()
            response = "going home"

    show_response.configure(text=response)
    player.enemy.configure_labels()
    player.configure_labels()


## NAME PLAYER
def name_player():
    root.title("Name Player")

    main_label.configure(text="Welcome to the game")

    name_player_text = """Please enter a command in the text box Like:\n "name bob" (no "quotes")\n in the format [command] [value]\n Then click the Proceed button to run the command\n "name (your name)"
	"""

    main_text.insert(END, name_player_text)
    main_button.configure(command=run_command)

    main_label.pack()
    main_text.pack()
    main_entry.pack()
    main_button.pack()
    show_response.pack()


## SELECT CLASS
def select_class():
    root.title("Player Class")
    main_label.config(text="Choose a class")

    main_text.delete(START, END)
    select_class_text = """Please enter a command:\nclass:\nArcher - Warrior\n"""
    main_text.insert(END, select_class_text)


## Create New Enemy
def New_Enemy(player):
    player.enemy.destroy_labels()

    player.enemy = Enemy()
    player.enemy.enemy = player
    player.enemy.show_labels()
    player.enemy.configure_labels()

    main_text.delete(START, END)
    fighting_text = "Please enter a command:\nattack:\n" + player.enemy.name + "\n\npotion:\nself"
    main_text.insert(END, fighting_text)


## Fight Tutorial
def mock_fight():
    root.title("Fight Enemy")
    main_label.config(text="Battle")
    battle_text.pack()
    New_Enemy(player)

    main_text.delete(START, END)
    battle_tutorial_text = "Please enter a command:\nattack:\n" + player.enemy.name + "\n\npotion:\nself"
    main_text.insert(END, battle_tutorial_text)

    player.show_labels()
    player.enemy.show_labels()


## Tutorial is over, debrief
def debrief():
    player.first_fight == False
    root.title("Debrief")
    main_label.config(text="Tutorial is over")
    battle_text.pack_forget()
    player.enemy.destroy_labels()
    player.destroy_labels()
    player.enemy.configure_labels()
    player.configure_labels()
    main_text.delete(START, END)
    main_text.insert(
        END,
        "Things will look a bit different now...\nYou did well,\n remember to instruct your hero in this format:\n[command] [value]\nJust be careful you don't give your health potions to your enemy...\nThe trial is over, now return home and begin a journey!\nYour command is\"run home\" or \"go home\""
    )


## Attack enemy
def attack_enemy(attacker, enemy):
    battle_text.delete(START, END)
    attacker_damage = random.randrange(attacker.min_attack,
                                       attacker.max_attack)
    enemy_damage = random.randrange(enemy.min_attack, enemy.enemy.max_attack)

    battle_text.insert(
        END, attacker.name + " attacks " + enemy.name + " for " +
        str(attacker_damage) + " damage!")
    battle_text.insert(
        END, "\n" + enemy.name + " attacks " + attacker.name + " for " +
        str(enemy_damage) + " damage!")
    enemy.health -= attacker_damage
    attacker.health -= enemy_damage
    player.configure_labels()
    enemy.configure_labels()

    if attacker.health < 1:
        attacker.die()
    elif enemy.health < 1:
        enemy.die()


## Game Over
def Game_Over():
    root.destroy()
    print("game over")


player = Player()
name_player()
tk.mainloop()

