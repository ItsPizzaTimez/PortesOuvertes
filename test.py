print("г--೦\n|  |\n|  ^\n|__")


from operator import length_hint
import random
import re
import keyboard

## ########
## data

wordList = {
    "firstWord":"maison",
    "secondWord":"banane",
    "threeWord":"animal",
    "fourWord":"cheval",
    "fiveWord":"pomme"
}


## ########
## def spawnRandomWord

def spawnRandomWord():
    randomWord = random.choice(list(wordList.values()))
    return randomWord

randomWord = spawnRandomWord()
def verifRandomWord(word):
    userInput = str(input("Choisissez une lettre : "))

    for char in re.finditer(userInput,randomWord):
        print(char.start())
    print(randomWord)

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