# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, direction= None, items=None):
        self.name = name
        self.current_room = current_room
        self.direction = direction
        self.items = items

    def movement(self, direction):
        move = getattr(self.room, f"{direction}_to")
        if move != None:
            self.room = move
            print(self.room)
        