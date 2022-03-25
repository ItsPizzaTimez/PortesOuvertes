
from data import Player
from weapon import Weapon

# armes

knife = Weapon("Couteau", 2)
pistol = Weapon("Pistolet", 5)

# joueurs

player1 = Player("Hugo", 20, 3)
player1.set_weapon(knife)
player2 = Player("Simon", 20, 5)

# actions sur les joueurs

