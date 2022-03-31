import os 
import keyboard # importe la librairie keyboard qui va permettre de coder des commandes avec des touches, on pourra les détecter
import string # importe la librairie string qui va nous donner tous les carcateres
import random # importe la librairie random pour proposer des évènement au hasard
from time import sleep # importe la librairie time pour gérer le temps
from http import server
import smtplib

bot = smtplib.SMTP_SSL("smtp.gmail.com",465)
bot.login("jpocondorcet@gmail.com","1fR     a$0     w!")
reinitialized = True

## ###################
## Nettoyer la console
def clearConsole(): 
    os.system('cls') # Pour Windows uniquement

## ########################
## Choisir son mot de passe
def choosePwd():
            # Créer son propre mot de passe
            pwdRegister = str(input("Choisissez votre mot de passe : "))
            print("Afin de confirmer, appuyez sur la touche Y pour le confirmer, appuyez sur la touche N pour le retaper")
            sureOrNo = True # On crée une variable de type Booléen.

            while sureOrNo: # Tant que "sureOrNo" est vraie, alors, si on appuie sur la touche Y sa coupe la boucle et ne change rien au mot de passe
                if keyboard.is_pressed('y'):
                    mdp = pwdRegister
                    sureOrNo = False
                elif keyboard.is_pressed("n"): # si on appuie sur la touche N la boucle "sureOrNo" le code va redemander
                    pwdRegister = str(input("Choisissez votre mot de passe : "))
                    print("Afin de confirmer, appuyez sur la touche Y pour le confirmer, appuyez sur la touche N pour le retaper")
                    sureOrNo = True
            return mdp

## #######################
## Générer un mot de passe
def generatePwd():
            # système pour generer un mot de passe aléatoire
            characters = string.printable
            mdp = ""
            sizeOfMdp = int(input("Veuillez choisir la taille du mot de passe : ")) # TODO CAMEL CASE
            i = 0
            while i < sizeOfMdp: # pour tous les nombres (i est un exemple) présents dans "sizeOfMdp" alors
                num = random.randint(0,99) # on crée une variable "num" qui va choisir au hasard entre 0 et 99
                mdp = mdp + characters[num] # on initialise la variable mdp qui est l'incrémentation des caracteres égaux a la longueur choisie dans le mot de passe de base vide
                i += 1
            return mdp
            
## ##################
## Email verification
def verifEmail(userMail):
    
    codeInput = input("Code incorrect. Voulez-vous renvoyer un code de vérification (Y) ou rettaper votre mot de passe (N)")
    
    def checkInput(codeInput, letter):
        input(codeInput)
        return True if codeInput.lower() == letter else False

    if checkInput(codeInput, "y"):

        digits = string.digits
        verify = ""
        i=0
        while i < 4:
            num = random.randint(0,4)
            verify = verify + digits[num]
            
            i += 1
        bot.sendmail("jpocondorcet@gmail.com", userMail, verify)
        print("Mail de vérification envoyé a : ",userMail)
        verifyUserMail = input("Mettez le code de vérification : ")
        if verifyUserMail == verify:
            print('Système déverrouillé avec succès !')
        else:
            print("Code incorrect. Voulez-vous renvoyer un code de vérification (Y) ou rettaper votre mot de passe (N)\n")
            if checkInput(codeInput, "y"):
                verifEmail()
            elif checkInput(codeInput, "n"):
                verifPwd()
    elif checkInput(codeInput, "n"):
        verifPwd()
    else:
        print(codeInput, "Inexistant")
        verifEmail()
    
## #####################
## Système de vérification
def verifPwd(mdp):
    chances = 3
    checkTime = 0
    verified = False
    
    while not verified:   
        verif = str(input("Entrez votre MDP :"))
        
        if verif == mdp:
            return print('Système déverrouillé avec succès !')
        else:
            chances -= 1
            print(chances," chances restantes")

        if chances == 0:
            chances = 3
            ''' checkTime += 10 TODO UNCOMMENT '''
            print('Le système est bloqué, réessayé dans', checkTime ,'secondes :')
            sleep(checkTime)
            verifEmail()
            verified = False
            
## #############
## Début du main
def main():
    userMail = str(input("Mettez votre adresse mail pour : "))
    print("Voulez-vous choisir votre mot de passe(1) ou le générer(2) ?")
    choice = True

    while choice:
        if keyboard.is_pressed('1'):
            mdp = choosePwd(userMail)
            choice = False    
        elif keyboard.is_pressed('2'):
            mdp = generatePwd()
            choice = False

    print("Votre mot de passe est : ",mdp)

    verifPwd(mdp)
    
main()