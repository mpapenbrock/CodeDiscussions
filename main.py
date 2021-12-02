import random

class Tamagotchi:
    hunger = 3
    happiness = 3
    discipline = 3
    cleanliness = 3
    def __init__(self, my_name):
        self.name = my_name

    def update_status(self, action):
        if action == "Feed":
            self.hunger +=1
        elif action == "Play":
            self.happiness +=1
        elif action == "Scold":
            self.discipline +=1
        elif action == "Clean":
            self.cleanliness +=1
        else:
            new_action = input("Sorry I did not understand, please write 'Feed', 'Play', 'Scold' or 'Clean'.")
            self.update_status(new_action)

    def print_status(self):
        string = "Hunger: {}\nHappiness: {}\nDiscipline: {}\nCleanliness: {}\n".format(self.hunger,
                                                                                       self.happiness,
                                                                                       self.discipline,
                                                                                       self.cleanliness)
        print(string)

    def generate_mood(self):
        mood = random.randint(0,3)
        if mood == 0:
            self.hunger -= 1
        elif mood == 1:
            self.happiness -= 1
        elif mood == 2:
            self.discipline -= 1
        elif mood == 3:
            self.cleanliness -= 1

    def check_alive(self):
        if (self.hunger <= 0 or self.happiness <= 0 or self.discipline <= 0 or self.cleanliness <= 0):
            print("Oh no! {} died! Create a new Tamagotchi!\n".format(self.name))
            return False
        else:
            return True

def create_new_tamagotchi():
    my_name = input("Hello! What would you like to name your Tamagotchi?\n")
    my_tama = Tamagotchi(my_name)

    alive = True
    while alive:
        my_tama.generate_mood()
        my_tama.print_status()
        action = input("What would you like to do?\n 'Feed', 'Play', 'Scold' or 'Clean'?")
        my_tama.update_status(action)
        alive = my_tama.check_alive()

def main():
    while True:
        create_new_tamagotchi()

main()