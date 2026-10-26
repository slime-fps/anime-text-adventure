# Nicholas Calatayud
# IT 140 Project Two - Anime Text Adventure Game
# Collect six magical items before facing Kuro.


def show_instructions():
    """Display the game goal and available commands."""
    print('Anime Text Adventure: Defeat Kuro')
    print('Collect all 6 magical items before entering the Demon Throne Room!')
    print('Move commands: go north, go south, go east, go west')
    print('Collect an item: get item name')


def show_status(current_room, inventory, rooms):
    """Show the player's location, inventory, and nearby item."""
    print('\n--------------------------')
    print('You are in the', current_room)
    print('Inventory:', inventory)
    if 'item' in rooms[current_room]:
        print('You see a', rooms[current_room]['item'])
    print('--------------------------')


def main():
    # Each room lists its connected rooms and any collectible item.
    rooms = {
        'Castle Entrance': {'west': 'Potion Room', 'north': 'Demon Throne Room'},
        'Potion Room': {'east': 'Castle Entrance', 'north': 'Armory', 'item': 'Healing Potion'},
        'Armory': {'south': 'Potion Room', 'north': 'Slime Cavern', 'item': 'Magic Sword'},
        'Slime Cavern': {'south': 'Armory', 'east': 'Ancient Library', 'item': 'Slime Core'},
        'Ancient Library': {'west': 'Slime Cavern', 'east': 'Dragon Shrine', 'item': 'Ancient Spellbook'},
        'Dragon Shrine': {'west': 'Ancient Library', 'south': 'Crystal Chamber', 'item': 'Dragon Armor'},
        'Crystal Chamber': {'north': 'Dragon Shrine', 'west': 'Demon Throne Room', 'item': 'Magic Crystal'},
        'Demon Throne Room': {'south': 'Castle Entrance', 'east': 'Crystal Chamber'}
    }

    current_room = 'Castle Entrance'
    inventory = []
    items_needed = 6
    show_instructions()

    # Keep playing until the player reaches the villain.
    while True:
        show_status(current_room, inventory, rooms)
        command = input('Enter your move: ').strip().lower()

        if command.startswith('go '):
            direction = command[3:].strip()
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print('You moved to the', current_room)
            else:
                print('Invalid direction. You cannot go that way.')

        elif command.startswith('get '):
            item_name = command[4:].strip()
            room_item = rooms[current_room].get('item')
            if room_item and item_name == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]['item']
                print(room_item, 'added to your inventory!')
            else:
                print('Invalid item. That item is not in this room.')

        else:
            print('Invalid command. Try go north or get item name.')

        # The player wins only if all six items are collected before meeting Kuro.
        if current_room == 'Demon Throne Room':
            if len(inventory) == items_needed:
                print('\nCongratulations! You collected all 6 items and defeated Kuro!')
            else:
                print('\nKuro defeated you! GAME OVER!')
            print('Thanks for playing!')
            break


if __name__ == '__main__':
    main()