print("г--೦\n|  |\n|  ^\n|__")


from operator import length_hint
import random
import re
import keyboard

## ########
## data

wordList = {
    "firstWord":"cacan",
    "secondWord":"banane"
}


## ########
## def spawnRandomWord

def spawnRandomWord():
    randomWord = random.choice(list(wordList.values()))
    return randomWord

def verifRandomWord(word):
    userInput = str(input("Choisissez une lettre : "))

    for char in re.finditer(userInput):
        print(char.start())

def main():
    print("Bienvenue sur le jeu du pendu !\n\nAppuie sur ESPACE pour commencer à jouer :)\n")
    choice = True
    while choice:
        if keyboard.is_pressed('SPACE'):
            word = spawnRandomWord()
            verifRandomWord(word)
            choice = False
        elif keyboard.is_pressed(not 'SPACE'):
            print("Appuie sur ESPACE pour commencer à jouer :)\n")
main()