# Text_based_game
Basic Schematic for text - based game. 
    def __init__(self): 

        self.rooms = { 

            'Market Square': {'South': 'Serene Zen Garden'}, 

            'Serene Zen Garden': {'North': 'Market Square', 'East': 'Imposing Daimyo\'s Mansion', 'South': 'Shadowy Tea House'}, 

            'Imposing Daimyo\'s Mansion': {'West': 'Serene Zen Garden', 'East': 'Ancient Shinto Shrine'}, 

            'Ancient Shinto Shrine': {'West': 'Imposing Daimyo\'s Mansion', 'East': 'Haunting Forest Path'}, 

            'Shadowy Tea House': {'North': 'Serene Zen Garden', 'East': 'Secret Rebel Hideout', 'South': 'Imperial Palace'}, 

            'Secret Rebel Hideout': {'West': 'Shadowy Tea House'}, 

            'Haunting Forest Path': {'West': 'Ancient Shinto Shrine'}, 

            'Imperial Palace': {'North': 'Shadowy Tea House'} 

        } 

        self.items = { 

            'Serene Zen Garden': 'bag', 

            'Imposing Daimyo\'s Mansion': 'Samurai Sword', 

            'Ancient Shinto Shrine': 'Bottle of healing herbs', 

            'Shadowy Tea House': 'Map of Edo', 

            'Secret Rebel Hideout': 'Key to rebel Hideout', 

            'Haunting Forest Path': 'Mysterious Amulet', 

            'Imperial Palace': 'coded scroll' 

        } 

        self.start_room = 'Market Square' 

        self.villain_room = 'Imperial Palace' 

        self.inventory = [] 

        self.current_room = self.start_room 

  

    def move(self, direction): 

        if direction in self.rooms[self.current_room]: 

            self.current_room = self.rooms[self.current_room][direction] 

            print(f"You have moved to {self.current_room}.") 

            if self.current_room == self.villain_room: 

                if len(self.inventory) == len(self.items): 

                    print("Congratulations! You have collected all items and won the game!") 

                else: 

                    print("You have encountered the villain and lost the game!") 

                return False 

            else: 

                return True 

        else: 

            print("You can't move in that direction!") 

            return True 

  

    def get_item(self): 

        if self.current_room in self.items: 

            item = self.items[self.current_room] 

            if item not in self.inventory: 

                self.inventory.append(item) 

                print(f"You have collected the {item}.") 

            else: 

                print("You already collected this item.") 

        else: 

            print("There is no item to collect in this room.") 

  

    def play(self): 

        print("Welcome to the game!") 

        print(f"You are currently in the {self.current_room}.") 

        while True: 

            print(f"Current Inventory: {self.inventory}") 

            command = input("Enter a command (move/get/quit): ").strip().lower() 

            if command == 'move': 

                direction = input("Enter direction (North/South/East/West): ").strip().capitalize() 

                if not self.move(direction): 

                    break 

            elif command == 'get': 

                self.get_item() 

            elif command == 'quit': 

                print("Thank you for playing!") 

                break 

            else: 

                print("Invalid command!") 

  

if __name__ == "__main__": 

    game = Game() 

    game.play() 

 

		  
