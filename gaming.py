# Define the rooms and their connections
rooms = {
    'Hall': {
        'description': 'You are in a grand hall with marble floors and a large chandelier.',
        'exits': {'north': 'Library', 'east': 'Kitchen'},
        'items': ['key']
    },
    'Library': {
        'description': 'You are in a quiet library filled with shelves of books.',
        'exits': {'south': 'Hall'},
        'items': []
    },
    'Kitchen': {
        'description': 'You are in a kitchen with a large table and a stove.',
        'exits': {'west': 'Hall', 'north': 'Dining Room'},
        'items': ['apple']
    },
    'Dining Room': {
        'description': 'You are in a dining room with a long table and several chairs.',
        'exits': {'south': 'Kitchen'},
        'items': []
    }
}

# Define the player
player = {
    'current_room': 'Hall',
    'inventory': []
}

# Function to display the current room's description
def describe_room(room_name):
    room = rooms[room_name]
    print(room['description'])
    if room['items']:
        print('You see the following items: ' + ', '.join(room['items']))
    print('Exits: ' + ', '.join(room['exits'].keys()))

# Function to move the player to a different room
def move_player(direction):
    current_room = player['current_room']
    if direction in rooms[current_room]['exits']:
        player['current_room'] = rooms[current_room]['exits'][direction]
        describe_room(player['current_room'])
    else:
        print('You cannot go that way.')

# Function to pick up an item
def pick_up_item(item):
    current_room = player['current_room']
    if item in rooms[current_room]['items']:
        rooms[current_room]['items'].remove(item)
        player['inventory'].append(item)
        print(f'You picked up {item}.')
    else:
        print('That item is not here.')

# Main game loop
def game_loop():
    describe_room(player['current_room'])
    while True:
        command = input('> ').strip().lower()
        if command in ['quit', 'exit']:
            print('Thanks for playing!')
            break
        elif command.startswith('go '):
            direction = command.split()[1]
