import keyboard # importe la librairie keyboard qui va permettre de coder des commandes avec des touches, on pourra les detecter
import string # importe la librairie string qui va nous donner tous les carcateres
import random # importe la librairie random pour proposer des évènement au hasard
from time import sleep

print("Voulez-vous choisir votre mot de passe(1) ou le générer(2) ?")
choice = True
while choice:
    if keyboard.is_pressed('1'):
        # creer son propre mot de passe

        mdp_register = str(input("Choisissez votre mot de passe : ")) # on stock le mot de passe dans la variable "mdp_register"

        print("Afin de confirmer, appuyez sur la touche Y pour le confirmer, appuyez sur la touche N pour le rettaper") # on écrit juste une phrase pour informer

        sure_or_no = True # on crée une variable de type Booléan. Cette dernière sera soit vraie ou fausse

        while sure_or_no: # tant que "sure_or_no" est vraie, alors, si on appuie sur la touche Y sa coupe la boucle et ne change rien au mot de passe
            if keyboard.is_pressed('y'):
                mdp=mdp_register
                sure_or_no = False

            elif keyboard.is_pressed("n"): # si on appuie sur la touche N la boucle "sure_or_no" le code va retourner à la ligne 11 donc redemander
                mdp_register = str(input("Choisissez votre mot de passe : "))
                print("Afin de confirmer, appuyez sur la touche Y pour le confirmer, appuyez sur la touche N pour le rettaper")
                sure_or_no = True
        choice = False
    elif keyboard.is_pressed('2'):
        # systeme pour generer un mot de passe aléatoire
        choice = False
        characters = string.printable
        mdp = ""
        mdp_size = int(input("Veuillez choisir la taille du mot de passe : "))



        for i in range(mdp_size): # pour tous les nombres (i est un exemple) présents dans "mdp_size" alors
            num = random.randint(0,99) # on crée une variable "num" qui va choisir au hasard entre 0 et 99
            mdp = mdp + characters[num] # on initialise la variable mdp qui est l'incrémentation des caracteres égaux a la longueur choisie dans le mot de passe de base vide
print("Votre mot de passe est ", mdp)

# systeme de verification

verification = True
check = True
reinitialized = True
chances = 3

while check:

    while verification:
        user_input = ''
        user_input = str(input('Mot de pass : '))


        if user_input == mdp:
            print('Système dévérouillé avec succès !')
            verification = False


        elif user_input != mdp:
            chances = chances -1
            print(chances," chances restantes")
            if chances == 0:
                print('Le système est bloqué, réessayé dans 10 secondes : ')
                sleep(10)
                verification = False
                print("Voulez-vous réinitialiser le mot de passe ? (Y pour oui et N pour non ou A pour abandonner)")


    while reinitialized:

        if keyboard.is_pressed('y'):
            mdp = str(input("Choisissez votre mot de passe : ")) # on stock le mot de passe dans la variable "mdp_register"
            chances = 3
            verification = True
            reinitialized = False

        elif keyboard.is_pressed('n'):
            mdp = mdp
            chances = 3
            verification = True
            reinitialized = False

        elif keyboard.is_pressed('a'):
            ckeck = False