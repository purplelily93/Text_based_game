# Nicole Lumbert
# Edo Quest: Hiroshi's  Last Mission.


# Define a consolidated dictionary linking rooms, their connections, and items
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

# Welcome message and brief instructions on how to navigate game
def welcome_message():
    print("Welcome to the Edo Adventure!")
    print("\nInstructions:")
    print("1. Explore the different rooms to find and collect all seven unique items.")
    print("2. You can move between rooms using the commands 'north', 'south', 'east', and 'west'.")
    print("3. Use the command 'get' to pick up an item in the room.")
    print("4. You have 16 tries to collect all the items. If you run out of tries, you lose the game.")
    print("5. Type 'quit' at any time to exit the game.")
    print("6. Collect all the items to win the game!")
    print("\nGood luck on your adventure!\n")

# Room status to let player know what is in their inventory and which room they are in.
def main():
    global current_room, tries
    welcome_message()

    while tries > 0:  # Loop continues as long as the player has tries left
        show_status()
        move = input("\nEnter your move (north/south/east/west, get, or quit): ").strip().lower() # User input action to perform

        if move == "get":
            get_item()
        elif move in ["north", "south", "east", "west"]:
            current_room = get_new_state(move, current_room)
            tries -= 1  # Deduct a try for each move
            check_loss()  # Check if the player has run out of tries
        elif move == "quit":
            print("Thank you for playing! Goodbye!")
            break  # Exit the game loop
        else:
            print("Invalid move!")

        # Win check is inside the loop to allow game to end once all items are collected
        check_win()

# Initialize game state
current_room = "Market Square"
inventory = []
all_items = ["coded scroll", "bag", "Samurai Sword", "Bottle of healing herbs", "Map of Edo", "Mysterious Amulet",
             "Key to rebel Hideout"]
tries = 16  # Maximum number of moves allowed


def show_status():
    print("\nYou are in the " + current_room)
    print("Description:", game_map[current_room]["description"])
    print("Inventory:", inventory)
    if game_map[current_room]["item"]:
        print("You see a " + game_map[current_room]["item"])
    print("Available exits: " + ", ".join(
        [direction.capitalize() for direction in game_map[current_room] if direction not in ["item", "description"]]))
    print(f"Tries left: {tries}")


def get_new_state(direction_from_user, current_room):
    if direction_from_user.lower() in game_map[current_room]:
        return game_map[current_room][direction_from_user.lower()]
    else:
        print("You can't go that way!")
        return current_room  # Stay in the current room if the move is invalid

# Get-item loop
def get_item():
    global inventory
    item = game_map[current_room].get("item")
    if item:
        inventory.append(item)
        game_map[current_room]["item"] = None  # Remove the item from the room after it's picked up
        print("You have picked up the " + item)
        check_win()
    else:
        print("There's nothing to take here.")

# Game auto-check for win or loss of player.
def check_win():
    if sorted(inventory) == sorted(all_items):
        print("\nCongratulations! You have collected all items, saved all samurai, and put an"
              "end to the evil Daimyo!")
        exit()


def check_loss():
    if tries == 0:
        print("\nYou have been slain by the evil Daimyo's henchmen.")
        exit()

if __name__ == "__main__":
    main()
