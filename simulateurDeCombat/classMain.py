import keyboard
from time import sleep

class Player:

    def __init__(self, pseudo, health, attack):

        self.pseudo = pseudo
        self.health = health
        self.attack = attack

    def get_pseudo(self):
        
        return self.pseudo

    def get_health(self):

        return self.health

    def get_attack_value(self):

        return self.attack

    def damage(self, damage):

        self.health -= damage

    def attack_player(self, target):

        target.damage(self.attack)

Knight = Player("Knight", 20, 5)
Ogre = Player("Ogre", 25, 4)
Fairy = Player("Fairy", 40,2)
Wizzard = Player("Wizzard", 15, 6)

print("Appuie sur ESPACE pour commencer à jouer !")

game = True 

while game:
    
    if keyboard.is_pressed('SPACE'):
        
        for i in range(1,4):
            print(i)
            sleep(1)

        print("C'est partit !")

        sleep(0.5)
        print("\n\nKnight")
        sleep(0.5)
        print("\n\nOgre")
        sleep(0.5)
        print("\n\nFairy")
        sleep(0.5)
        print("\n\nWizzard")
        sleep(0.5)

        character = str(input("\nChoisissez votre heros !"))

        print("Bon choix ! Bienvenue dans l'équipe : ",character, " !")
