import os.path
import operator
from os import path

PC_dict = {}
NPC_dict = {}
combatant_dict = {}

def PC_setup():
    global PC_dict
    PC_count = int(input("Enter number of PCs: "))

    # I want some way to save PCs so we can just prompt for their initiatives...
    # Definitely possible but a little tricky to convert a list to a dict, then
    # insert values iteratively through each key. For now we prompt on startup.
    for i in range(PC_count):
        name = input("Enter PC name: ")
        initiative = int(input("Enter PC initiative: "))
        PC_dict[name] = initiative
    # Sort it up
    PC_dict = dict(sorted(PC_dict.items(), key=operator.itemgetter(1), reverse=True))


def NPC_setup():
    global NPC_dict
    NPC_count = int(input("Enter number of NPCs: "))

    for i in range(NPC_count):
        name = input("Enter NPC name: ")
        initiative = int(input("Enter NPC initiative: "))
        NPC_dict[name] = initiative
    # Sort
    NPC_dict = dict(sorted(NPC_dict.items(), key=operator.itemgetter(1), reverse=True))

def combatant_setup():
    global combatant_dict
    combatant_dict.update(PC_dict)
    combatant_dict.update(NPC_dict)
    combatant_dict = dict(sorted(combatant_dict.items(), key=operator.itemgetter(1), reverse=True))

PC_setup()
print("\n")
NPC_setup()
combatant_setup()
print("\n")
print("Your initiative order is:\n" + str(combatant_dict))
