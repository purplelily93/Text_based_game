# Edo Quest: Hiroshi's Last Mission

# Consolidated game map with rooms, connections, and items
game_map = {
    "Market Square": {
        "description": "A bustling market filled with vendors and shoppers.",
        "north": "Serene Zen Garden",
        "east": "Shadowy Tea House",
        "west": "Imposing Daimyo's Mansion",
        "item": "coded scroll"
    },
    "Serene Zen Garden": {
        "description": "A tranquil garden with beautifully manicured trees and a koi pond.",
        "south": "Market Square",
        "east": "Ancient Shinto Shrine",
        "item": "bag"
    },
    "Imposing Daimyo's Mansion": {
        "description": "A grand mansion with high walls and guarded gates.",
        "east": "Market Square",
        "north": "Imperial Palace",
        "item": "Samurai Sword"
    },
    "Ancient Shinto Shrine": {
        "description": "A peaceful shrine with the scent of incense in the air.",
        "west": "Serene Zen Garden",
        "north": "Haunting Forest Path",
        "item": "Bottle of healing herbs"
    },
    "Shadowy Tea House": {
        "description": "A dimly lit tea house with the sound of soft music.",
        "west": "Market Square",
        "north": "Secret Rebel Hideout",
        "item": "Map of Edo"
    },
    "Secret Rebel Hideout": {
        "description": "A hidden hideout with signs of recent activity.",
        "south": "Shadowy Tea House",
        "item": "Mysterious Amulet"
    },
    "Haunting Forest Path": {
        "description": "A dark and eerie forest path with rustling leaves.",
        "south": "Ancient Shinto Shrine",
        "item": "Key to rebel Hideout"
    },
    "Imperial Palace": {
        "description": "The majestic palace of the Emperor, heavily guarded and grand.",
        "south": "Imposing Daimyo's Mansion",
        "item": None  # No item in the Imperial Palace
    }
}

# Initialize game state
current_room = "Market Square"
inventory = []
all_items = [
    "coded scroll",
    "bag",
    "Samurai Sword",
    "Bottle of healing herbs",
    "Map of Edo",
    "Mysterious Amulet",
    "Key to rebel Hideout"
]
tries = 16  # Maximum number of moves allowed

# Welcome message
def welcome_message():
    print("Welcome to Edo Quest: Hiroshi's Last Mission!")
    print("\nInstructions:")
    print("1. Explore the rooms to collect all seven unique items.")
    print("2. Move using 'north', 'south', 'east', or 'west'.")
    print("3. Type 'get' to pick up an item in the room.")
    print("4. You have 16 moves to collect all items.")
    print("5. Type 'quit' anytime to exit the game.")
    print("6. Collect all items to win!\n")
    print("Good luck, samurai!\n")

# Show player status
def show_status():
    print("\nYou are in the " + current_room)
    print("Description:", game_map[current_room]["description"])
    print("Inventory:", inventory)
    if game_map[current_room]["item"]:
        print("You see a " + game_map[current_room]["item"])
    exits = [direction.capitalize() for direction in game_map[current_room] if direction not in ["item", "description"]]
    print("Available exits: " + ", ".join(exits))
    print(f"Tries left: {tries}")

# Move to new room
def get_new_state(direction_from_user, current_room):
    if direction_from_user in game_map[current_room]:
        return game_map[current_room][direction_from_user]
    else:
        print("You can't go that way!")
        return current_room

# Pick up item
def get_item():
    global inventory
    item = game_map[current_room].get("item")
    if item:
        inventory.append(item)
        game_map[current_room]["item"] = None
        print("You have picked up the " + item)
        check_win()
    else:
        print("There's nothing to take here.")

# Check win condition
def check_win():
    if sorted(inventory) == sorted(all_items):
        print("\nCongratulations! You have collected all items, saved all samurai, and ended the evil Daimyo's reign!")
        exit()

# Check loss condition
def check_loss():
    if tries == 0:
        print("\nYou have been slain by the evil Daimyo's henchmen.")
        exit()

# Main game loop
def main():
    global current_room, tries
    welcome_message()

    while tries > 0:
        show_status()
        move = input("\nEnter your move (north/south/east/west, get, or quit): ").strip().lower()

        if move == "get":
            get_item()
        elif move in ["north", "south", "east", "west"]:
            current_room = get_new_state(move, current_room)
            tries -= 1
            check_loss()
        elif move == "quit":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid move!")

if __name__ == "__main__":
    main()

