# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = [] 

    def move_to(self, movement, current_location):
        attribute  = movement + '_to'

        if hasattr(current_location, attribute):
            return getattr(current_location, attribute)

            print('\nYou cannot go this way - pick a new direction')

            return current_location

    def pickup_item(self, item):
        if self.current_room.items.count(item) > 0:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.pick_up()
        else:
            print(f'A {item.name} is not in this room.')

    def drop_item(self, item):
        if self.items.count(item) > 0:
            self.current_room.items.append(item)
            self.items.remove(item)
            item.drop()
        else:
            print(f"You do not have a {item.name} to drop")

    def print_items(self):
        if not self.items:
            print("You do not have any items")
        else:
            print("You have the following items: ")
            for x in self.items:
                print(x.name)
                