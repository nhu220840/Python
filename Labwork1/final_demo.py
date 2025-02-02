import threading

class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

class PlayerCharacter(Character):
    def __init__(self, name, level, health, inventory):
        super().__init__(name, level, health)
        self.inventory = inventory

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nInventory: {self.inventory}"
    
    def save(self, filename):
        try:
            with open(filename, "w") as f:
                f.write(f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nInventory: {self.inventory}\n")
        except Exception as e:
            print(f"Error: {e}")

    def save_in_background(self, filename):
        t = threading.Thread(target=self.save, args=(filename,))
        t.start()

test = Character("Stone Giant", 1, 780)

#Test case
# test2 = PlayerCharacter("Gandalf", 99, 1000, "Staff of Power")
# print(test2)
# test2.save("./Labwork1/player_info.txt")

test2.save_in_background("./Labwork1/player.txt")


