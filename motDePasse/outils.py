import os 

## ###################
## Nettoyer la console
def clearConsole(): 
    os.system('cls') # Pour Windows uniquement

## ###################
## Vérifie si valeur reçue == valeur donnée
## Renvoie un booléen
def checkInput(userInput, comparedValue):
    return True if userInput == comparedValue else False