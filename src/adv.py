from room import Room
from player import Player
from item import Item

import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Create items
items = {
    'sword': Item('sword', 'Use it to slay bad guys'),
    'bag': Item('bag', 'Use it to carry your loot'),
    'torch': Item('torch', 'Use to see in the dark'),
    'loot': Item('loot', "Use it to buy more gear")
}

# Add items to room

room['foyer'].items.append(items['torch'])
room['overlook'].items.append(items['sword'])
room['outside'].items.append(items['bag'])
room['treasure'].items.append(items['loot'])

# Main

# Make a new player object that is currently in the 'outside' room.
user = Player('Bilbo', room['outside'])

# Write a loop that:
while True:
    print(f"\n\nGreetings {user.name}\nYou are in the: {user.current_room}")

    for txt in textwrap.wrap(user.current_room.print_description()):
        print(f"{txt}\n")
        print(f"\nItems in the room: {user.current_room.list_items()}")    

    direction = input('Enter a direction (n, s, e, w) or enter q to abandon your adventure').lower() 

    if direction in ['n', 's', 'e', 'w']:
        user.current_room = user.move_to(direction, user.current_room)
        continue
    elif direction == 'q':
        print('Thank you for playing come back soon adventurer')
        break
    else:
        # direction != 'n' or 's' or 'e' or 'w' or 'q':
        # user.current_room = user.current_room
        print("You provided invalid input - Please try again") 
    
           

