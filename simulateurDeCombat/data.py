
from weapon import Weapon

# boite principale

class Player:

    # constructeur

    def __init__(self, pseudo, health, attack):

        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None

    # méthodes

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health
    
    def get_attack_value(self):
        return self.attack

    def set_weapon(self, weapon):
        self.weapon = weapon

    if self.has_weapon():
        damage += self.weapon.get_damage_amount()

    target_player.damage(damage)

    def has_weapon(self):
        return self.weapon is not None

    # interactions

    # on crée l'action d'attaque, qui permet de soustraire a la vie du joueur concerné
    def damage(self, damage):
        self.health -= damage
        print("Aie... tu viens de te prendre ", damage, " !")

    # on crée l'action attaque player, qui permet de soustraire a la vie du joueur concerné les degats de l'ennemie

    def attack_player(self, target_player):
        target_player.damage(self.attack)
