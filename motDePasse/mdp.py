import random # Importe la librairie random pour proposer des évènement au hasard
import smtplib
import string # Importe la librairie string qui va nous donner tous les carcatères
from time import sleep # Importe la librairie time pour gérer le temps

from outils import *

bot = smtplib.SMTP_SSL("smtp.gmail.com",465)
bot.login("jpocondorcet@gmail.com","1fR     a$0     w!")
reinitialized = True

## ########################
## Créer son mot de passe
def createPassword():

    while True:
        passwordInput = input("Choisissez votre mot de passe : ")
        confirmInput = input("Afin de confirmer, appuyez sur la touche Y pour le confirmer, appuyez sur la touche N pour le retaper\n ->").lower()
        if checkInput(confirmInput, "y"):
            createdPassword = passwordInput
            break
        else:
            continue
    return createdPassword

## #######################
## Générer un mot de passe
def generatePassword():
    characters = string.printable
    mdp = ""

    while True:
        sizeOfMdp = input("Veuillez choisir la taille du mot de passe : ")
        if sizeOfMdp.isdigit():
            size=int(sizeOfMdp)
            i = 0
            while i < size: 
                num = random.randint(0,99)
                mdp = mdp + characters[num] 
                i += 1
            return mdp
        else: 
            print("La valeur entrée n'est pas un nombre valide")
            continue

## ##################
## Mot de passe oublié
def passwordForgotten(mdp):

    while True:
        passwordForgottenMenuInput = input("Souhaitez-vous:\n1- Recevoir un code de vérification par mail\n2- Tenter de rentrer le mot de passe\n ->")
        if checkInput(passwordForgottenMenuInput, "1"):
            userMailInput = input("Veuillez entrer votre adresse mail\n ->")
            digits = string.digits
            verify = ""
            i=0
            while i < 4:
                num = random.randint(0,4)
                verify = verify + digits[num]
                i += 1
            bot.sendmail("jpocondorcet@gmail.com", userMailInput, verify)
            print("Mail de vérification envoyé a :", userMailInput)
            while True:
                verifyUserMail = input("Mettez le code de vérification : ")
                if checkInput(verifyUserMail, verify):
                    print('Système déverrouillé avec succès !')
                    break
                else:
                    print('Code incorrect !\n')
                    continue
            break
        elif checkInput(passwordForgottenMenuInput, "2"):
            connexion(mdp)
            break
        else: continue

## #####################
## Système de connection
def connexion(mdp):
    chances = 3
    waitingTime = 0

    while True:
        if chances == 0:
            chances = 3
            waitingTime += 5
            print('Le système est bloqué, réessayer dans', waitingTime ,'secondes :')
            sleep(waitingTime)
            clearConsole()

        passwordInput = input("Entrez votre MDP (\"R\": mot de passe oublié): ")
        
        if checkInput(passwordInput, mdp): break
        elif checkInput(passwordInput.upper(), "R"):
            passwordForgotten(mdp)
            break
        else:
            chances -= 1
            print(chances," chances restantes\n")


## #############
## Début du main
def main():

    clearConsole()

    print("Bienvenue dans notre application !")
    
    while(True):
        inputMenu = input("Voulez-vous :\n1- Choisir votre mot de passe\n2- Générer un nouveau mot de passe\n3- Quitter l'application\n -> ")
        if checkInput(inputMenu, "1"):
            clearConsole()
            mdp = createPassword()
            break
        elif checkInput(inputMenu, "2"):
            clearConsole()
            mdp = generatePassword()
            break
        elif checkInput(inputMenu, "3"):
            clearConsole()
            print("Au revoir !")
            quit()
        else: 
            clearConsole()
            print("Choix incorrect\n")
            continue

    clearConsole()

    print("Votre mot de passe est {}".format(mdp))

    while(True):
        inputMenu = input("Que souhaitez-vous faire ? :\n1- Se connecter\n2- Mot de passe oublié\n3- Quitter l'application\n -> ")
        if checkInput(inputMenu, "1"):
            clearConsole()
            connexion(mdp)
            break
        elif checkInput(inputMenu, "2"):
            clearConsole()
            passwordForgotten(mdp)
            break
        elif checkInput(inputMenu, "3"):
            clearConsole()
            print("Au revoir !")
            quit()
        else: 
            print("Choix incorrect\n")
            continue

    clearConsole()
    print('Système déverrouillé avec succès !')



## ##############
##  Appel du main
main()