from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
u_name = input("Name your character: ")

my_player = Player(u_name, room["outside"])

# Write a loop that:
#
# - Prints the current room name
# - Prints the current description (the textwrap module might be useful here).
# - Waits for user input and decides what to do.
#
# - If the user enters a cardinal direction, attempt to move to the room there.
# - Print an error message if the movement isn't allowed.
#
# - If the user enters "q", quit the game.
def advgame(u_name):

    print(f"Greetings, {my_player.name} you are at {my_player.room}")

    while True:
        direction = input("Move your character (n,s,e,w) or press q to quit: ").lower().split(" ")
        if direction == "q":
            print("Exiting your adventure, Have a great day")
            # print("There is nothing in that direction try a different direction")
            break
        elif direction != 'n' or 'e' or 'w' or 's':
            print("You cannot move in that direction - please pick a new one")
        elif direction == "n":
            print("You have chosen to move North")
        elif direction == "s":
            print("You have chosen to move South")    
        elif direction == "e":
            print("You have chosen to move East")
        elif direction == "w":
            print("You have chosen to move West")
        else:
            print("You cannot move in that direction - please pick a new one")        

# room movement conditionals for Outside Cave Entrance (north is valid)
        if my_player.room == "Outside Cave Entrance" and direction == "n":
            # print{f'{my_player.name} ",moved to a new room"')
            # my_player.move
            my_player.room = my_player.room.n_to
            print(f'{my_player.name} "you are now in the {my_player.room}"')
        elif my_player.room == "Outside Cave Entrance" and direction != "n":
            print(f'"You cannot move {direction} from {my_player.room}, choose a different direction') 
# room movement conditions for Foyer (north, south, east are valid)
        elif my_player.room == 'Foyer' and direction == 'n':
            player.current_room = my_player.current_room.n_to
        elif my_player.room == 'Foyer' and direction == 's':
            player.current_room = my_player.current_room.s_to
        elif my_player.room == 'Foyer' and direction == 'e':
            player.current_room = my_player.current_room.e_to        
        elif my_player.room == 'Foyer' and direction == 'w':
            print(f'"You cannot move {direction} from {my_player.room}, choose a different direction') 
# room movement conditionals for overlook (south is valid)
        elif my_player.room == "Grand Overlook" and direction == "s":
            my_player.room = my_player.room.s_to
            print(f'{my_player.name} "you are now in the {my_player.room}"')
        elif my_player.room == "Grand Overlook" and direction != "s":
            print(f'"You cannot move {direction} from {my_player.room}, choose a different direction')
        # elif direction[0] in ["n", "s", "e", "w"]:
        #     my_player.movement(direction[0])
        elif direction[0] =="q":
            print("Exiting your adventure, Have a great day")
            exit()
        else:
                