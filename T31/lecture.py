# Object-Oriented Programming: Inheritance

class Games:
    def __init__(self, name, type, developer):
        self.name = name
        self.type = type
        self.developer = developer

    def pirate_game(self):
        return f"You got the {self.name} for free!"


class ConsoleGame(Games):
    def __init__(self, console, name, type, developer):
        super().__init__(name, type, developer)
        self.console = console
    
    def is_too_old(self):
        print("The console is too old to run this game.")

game = Games("Sims 3", " Life Simulation", "EA")
console_game = ConsoleGame("Nintendo Switch", input("Please enter the game name: "), "RPG", "Niantic")
console_game.is_too_old()
print(game.pirate_game())