from HangmanStages import stages 
from Words import word_list
import random

word = random.choice(word_list).upper()

def Play(word):
    word_was_guessed = False 
    remaining_tries = 6
    hidden_letter_symbol = '_'
    word_completion = hidden_letter_symbol * len(word)
    verlauf = []

    print('............................|Galgenmännchen|......................................')
    print('                              Von Laurin                                          ')
    print('                                                                                  ')
    print('----------------------------------------------------------------------------------')
    name = input('Wie heißt du denn?')
    print('Du hast 6 Versuche, um ein Wort zu erraten. Ratest du falsch, hängt sich langsam eine Person auf.')
    start = input('Möchtest du starten? [j/n]') 
    print('----------------------------------------------------------------------------------')
    if start == 'j':
        keyStart = True
    elif start == 'n':
        print('Du hast doch keine Ahnung! Ich starte trotzdem.')
        keyStart = True
    else:
        return

    PrintHangmanStage(remaining_tries)
    print(word_completion)
    gameIsRunning = True

    while gameIsRunning:
        while not word_was_guessed and remaining_tries > 0 and keyStart == True:
            while True:
                print('--------------------------------------------------')
                guess = (input('Buchstabe eingeben: ')).upper() 
                try:
                    val = int(guess)
                    return
                except ValueError:
                    print(f'Du hast noch {remaining_tries} Versuche')
                    if guess in verlauf:
                        print('Der Buchstabe wurde schon einmal genannt!')
                        continue
                    verlauf.append(guess)
                    break
            if guess not in word:
                print(f'Enthält den Buchstaben {guess} nicht')

                remaining_tries -= 1
            elif guess in word:
                print(f'Enthält Buchstaben {guess} .')

                word_completion = FillLettersInWord(word, guess,word_completion)

                word_was_guessed = hidden_letter_symbol not in word_completion
                print('--------------------------------------------------')
            PrintHangmanStage(remaining_tries)  
            print(word_completion)
                                                                   
        if word_was_guessed:
            print(f'Du hast gewonnen {name}!')
        else:
            print(f'Du hast verloren {name}!')
            print(f'Das Wort war {word}')
        neustart = input('Neustart? [j/n]') 

        if neustart == 'n':
            print('Danke fürs spielen!')
            return
        elif neustart == 'j':
            word = random.choice(word_list).upper()
            word_was_guessed = False
            remaining_tries = 6
            keyStart = True
            word_completion = hidden_letter_symbol * len(word)
            verlauf = []
        else:
            print('Gebe mir eine richtige Angabe!')
            neustart = input('Neustart? [j/n]') 
        if neustart == 'j':
            print('Dann noch eine Runde!')
            word = random.choice(word_list).upper()
            word_was_guessed = False
            remaining_tries = 6
            keyStart = True
            word_completion = hidden_letter_symbol * len(word)
            verlauf = []
            
def PrintHangmanStage(stage):
    print(stages[stage])


def GetWordIndices(word, guess):
    indices = []
    for index, letter in enumerate(word):
        if letter == guess:
            indices.append(index)
    return indices

def FillLettersInWord(word, guess, word_completion):
    word_as_list = list(word_completion)
    
    indices = GetWordIndices(word, guess)
    for index in indices:
        word_as_list[index] = word_as_list[index].replace('_', guess)
    word_completion = "".join(word_as_list)
    return word_completion

Play(word)