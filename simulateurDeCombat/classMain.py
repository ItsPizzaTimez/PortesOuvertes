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




Ogre = Player("Ogre", 25, 4)
Fairy = Player("Fairy", 40,2)
Wizzard = Player("Wizzard", 15, 6)


game = True 

print("Appuie sur ESPACE pour commencer à jouer !")

while game:

    if keyboard.is_pressed('SPACE'):
        
        for i in range(1,4):
            print(i)
            sleep(1)

        print("C'est partit !")

        user = str(input('Mettez votre pseudo : '))

        player_Knight = Player(user, 20, 5)
        print("Bienvenue dans l'équipe : ",player_Knight.get_pseudo()," !")

        print("Prêt pour les combats ? Si oui, appuyer sur ESPACE sinon, sur ALT")

        if keyboard.is_pressed('1'):

            print("\n\nPremier level : ennemie : Ogre\n\n")
        
        elif keyboard.is_pressed('2'):
            game = False