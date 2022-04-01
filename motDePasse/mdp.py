import random # Importe la librairie random pour proposer des évènement au hasard
import smtplib
import string # Importe la librairie string qui va nous donner tous les carcatères
from time import sleep # Importe la librairie time pour gérer le temps

# Importe checkInput et clearConsole des outils
from outils import *

bot = smtplib.SMTP_SSL("smtp.gmail.com",465)
bot.login("jpocondorcet@gmail.com","1fR     a$0     w!")
reinitialized = True

# -----------------------------------------------------------------------------

## ########################
## Créer son mot de passe
def createPassword():
    # Boucle demandant le mot de passe
    while True:
        passwordInput = input("Choisissez votre mot de passe : ")
        # "lower" sert à formatter l'input afin de vérifier sans se soucier de la casse 
        confirmInput = input("Afin de confirmer, appuyez sur la touche Y pour le confirmer, appuyez sur la touche N pour le retaper\n ->").lower() 

        if checkInput(confirmInput, "y"):
            createdPassword = passwordInput
            # "break" permet de sortir de la boucle while
            break        
        # "continue" permet de revenir au début de la boucle while
        else: continue 

    # "return" nous retourne le string du mot de passe
    return createdPassword 

# -----------------------------------------------------------------------------

## #################################
## Générer un mot de passe aléatoire
def generatePassword():
    # Initialisation d'une liste de tout les caractères 
    characters = string.printable
    # Initialisation de la variable mdp pour la boucle while i < size
    mdp = ""

    # Boucle de choix de la taille de mot de passe
    # (dans le cas ou la valeur est incorrecte)
    while True:
        pwdSize = input("Veuillez choisir la taille du mot de passe : ")
        
        # On vérifie que pwdSize est un nombre et qu'il soit positif
        if pwdSize.isdigit():
            # Si il s'agit d'un nombre valide, on transforme le string en int
            pwdSizeInt = int(pwdSize)

            i = 0
            # On fait la boucle le nombre de fois donné par pwdSizeInt
            while i < pwdSizeInt:
                # On prend un nombre aléatoire entre 0 et 99
                num = random.randint(0,99)
                # Le nombre aléatoire va "piocher" 
                # dans la liste de caractères initialisés plus haut
                mdp = mdp + characters[num] 
                i += 1
            return mdp

        else: 
            print("La valeur entrée n'est pas un nombre valide")
            continue

# -----------------------------------------------------------------------------

## ###################
## Mot de passe oublié
def passwordForgotten(mdp):

    # Boucle du menu de mot de passe oublié
    while True:
        passwordForgottenMenuInput = input("Souhaitez-vous:\n1- Recevoir un code de vérification par mail\n2- Tenter de rentrer le mot de passe\n ->")

        if checkInput(passwordForgottenMenuInput, "1"):
            # digits reçoit "0123456789"
            digits = string.digits
            verify = ""
            i=0
            while i < 4:
                num = random.randint(0,4)
                verify = verify + digits[num]
                i += 1

            userMailInput = input("Veuillez entrer votre adresse mail\n ->")
            # Envoi d'e-mail à "userMailInput" de "jpocondorcet@gmail.com"
            # avec "verify" en contenu
            bot.sendmail("jpocondorcet@gmail.com", userMailInput, verify)
            print("Mail de vérification envoyé a :", userMailInput)
            
            # Boucle de vérification du code
            while True:
                verifyUserMail = input("Mettez le code de vérification : ")
                if checkInput(verifyUserMail, verify):
                    print('Système déverrouillé avec succès !')
                    break # On sort de la boucle while True
                else:
                    print('Code incorrect !\n')
                    continue
            # On sort de cette boucle uniquement 
            # quand on est aussi sorti de la boucle précédente
            break 
        elif checkInput(passwordForgottenMenuInput, "2"):
            connexion(mdp)
            break
        else: continue

# -----------------------------------------------------------------------------

## #####################
## Système de connection
def connexion(mdp):
    # On initialise les chances à 3
    chances = 3
    # On initialise le temps de blocage
    waitingTime = 0

    # Boucle de connection
    while True:
        # Si les chances sont à 0, on bloque l'utilisateur
        if chances == 0:
            # On réinitialise les chances à 3
            chances = 3
            # On ajoute 5 secondes au temps total de blocage
            waitingTime += 5

            print('Le système est bloqué, réessayer dans', waitingTime ,'secondes :')
            sleep(waitingTime) # Attente
            clearConsole()

        passwordInput = input("Entrez votre MDP (\"R\": mot de passe oublié): ")
        
        # Si le mot de passe correspond à l'input, 
        # on sort de cette fonction pour afficher le message final dans le main
        if checkInput(passwordInput, mdp): break
        # Si l'utilisateur appuie sur "R" (ou "r", graçe au .upper()),
        # La fonction mot de passe oublié est appelée
        elif checkInput(passwordInput.upper(), "R"):
            passwordForgotten(mdp)
            break
        # Si l'utilisateur ne donne pas le bon mot de passe 
        # et n'appuie pas sur "R", il perds une chance
        else:
            chances -= 1
            print(chances," chances restantes\n")

# -----------------------------------------------------------------------------

## #############
## Début du main
def main():

    clearConsole()

    print("Bienvenue dans notre application !")
    
    # Boucle de menu initial
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
            # Termine l'application
            quit()
        else: 
            clearConsole()
            print("Choix incorrect\n")
            continue

    clearConsole()

    # ".format(mdp)" petmet de remplacer la valur {} par mdp dans le string
    print("Votre mot de passe est {}".format(mdp))

    # Boucle de second menu après création / génération de mot de passe
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

    # L'utilisateur s'est connecté, fin du programme
    print('Système déverrouillé avec succès !')

# -----------------------------------------------------------------------------

## ##############
##  Appel du main
main()
