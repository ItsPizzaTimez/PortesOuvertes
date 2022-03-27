import os 
import keyboard # importe la librairie keyboard qui va permettre de coder des commandes avec des touches, on pourra les detecter
import string # importe la librairie string qui va nous donner tous les carcateres
import random # importe la librairie random pour proposer des évènement au hasard
from time import sleep # importe la librairie time pour gérer le temps
from http import server
import smtplib

bot = smtplib.SMTP_SSL("smtp.gmail.com",465)
bot.login("jpocondorcet@gmail.com","1fR     a$0     w!")
reinitialized = True

## #####################
## Clear the console
def clearConsole(): 
    os.system('cls') # pour Windows uniquement

def choosePwd():
    # creer son propre mot de passe
            mdp_register = str(input("Choisissez votre mot de passe : ")) # on stock le mot de passe dans la variable "mdp_register"
            user_mail = str(input("Mettez votre adresse mail pour : "))
            print("Afin de confirmer, appuyez sur la touche Y pour le confirmer, appuyez sur la touche N pour le retapper") # on écrit juste une phrase pour informer
            sure_or_no = True # on crée une variable de type Booléan. Cette dernière sera soit vraie ou fausse

            while sure_or_no: # tant que "sure_or_no" est vraie, alors, si on appuie sur la touche Y sa coupe la boucle et ne change rien au mot de passe
                if keyboard.is_pressed('y'):
                    mdp = mdp_register
                    sure_or_no = False
                elif keyboard.is_pressed("n"): # si on appuie sur la touche N la boucle "sure_or_no" le code va retourner à la ligne 11 donc redemander
                    mdp_register = str(input("Choisissez votre mot de passe : "))
                    print("Afin de confirmer, appuyez sur la touche Y pour le confirmer, appuyez sur la touche N pour le retapper")
                    sure_or_no = True
            return mdp
    
def generatePwd():
        # systeme pour generer un mot de passe aléatoire
            characters = string.printable
            mdp = ""
            mdp_size = int(input("Veuillez choisir la taille du mot de passe : "))

            for i in range(mdp_size): # pour tous les nombres (i est un exemple) présents dans "mdp_size" alors
                num = random.randint(0,99) # on crée une variable "num" qui va choisir au hasard entre 0 et 99
                mdp = mdp + characters[num] # on initialise la variable mdp qui est l'incrémentation des caracteres égaux a la longueur choisie dans le mot de passe de base vide
            return mdp

## #####################
## Password verification
def verifPwd(mdp):
    chances = 3
    time_check = 0
    verified = False
    
    while not verified:   
        verif = str(input("Entrez votre MDP :"))
        
        if verif == mdp:
            return print('Système dévérouillé avec succès !')
        else:
            chances -= 1
            print(chances," chances restantes")

        if chances == 0:
            chances = 3
            time_check += 10
            print('Le système est bloqué, réessayé dans', time_check ,'secondes :')
            sleep(time_check)

## #############
## Start of main
def main():
    print("Voulez-vous choisir votre mot de passe(1) ou le générer(2) ?")
    choice = True

    while choice:
        if keyboard.is_pressed('1'):
            mdp = choosePwd()
            choice = False    
        elif keyboard.is_pressed('2'):
            mdp = generatePwd()
            choice = False

    print("Votre mot de passe est : ",mdp)

    verifPwd(mdp)
    
main()

""" 
    # systeme de verification
    print("Pour réinitialiser le mot de passe, appuyez sur Y sinon pour ignorer appuyez sur N")



    if keyboard.is_pressed('y'):
        digits = string.digits
    verify = ""
    for i in range(4):
        num = random.randint(0,4)
        verify = verify + digits[num]
    bot.sendmail("jpocondorcet@gmail.com", user_mail, verify)
    print("Mail de vérification envoyé a : ",user_mail)
    verify_user_mail = input("Mettez le code de vérification : ")
    if verify_user_mail == verify:
        print('Système dévérouillé avec succès !')
        check = False
        verification = False
        reinitialized = False
    else:
        print("Code incorrect. Voulez-vous renvoyer un code de vérification (Y) ou rettaper votre mot de passe (N)")
        if keyboard.is_pressed('Y'):
            mail_send()
        elif keyboard.is_pressed('n'):
            print("")

    verificationt()

 """