import json
from random import choice

theletterto = "*"

def GuessTheLetter():
    while True:
        letter = input("Enter A Letter: ")
        if len(letter) != 1:
            print("Please Input a SINGLE LETTER!")
            continue
        else:
            return letter

def ChangeLetter(indices, lettertochangeto, wordtobechanged, word):
    wordtobechanged = list(wordtobechanged)
    word = list(word)
    for index in indices:
        word[index] = wordtobechanged[index]
    wordtobechanged = ''.join(wordtobechanged)
    word= ''.join(word)
    print(word)
    return word



def Encrypt(word):
    word = list(word)
    for i in range(len(word)):
        word[i] = '_'
    word = ''.join(word)
    return word

def TheGame(letter):
    with open("words.json", "r") as f:
            words_data = json.load(f)
            the_hidden_word = choice(words_data["data"])
    word = Encrypt(the_hidden_word)
    print(word)        
    #print(the_hidden_word)   #Remove "#" in order to cheat
    while(not any(char == "_" for char in the_hidden_word)):
        
        letter = GuessTheLetter()
        positions = []
        for i, char in enumerate(the_hidden_word):
            if char == letter:
                positions.append(i)
            
        if letter in the_hidden_word:
            print("it is valid")
            print(f"the letter is the {positions}. character")
      
            word = ChangeLetter(positions, theletterto, the_hidden_word, word)
            
            if not any(char == "_" for char in word):
                print("congrulations!")
                TheGame(None)
            continue
            
        else:
            print("No")
            print(word)
            continue




def Main():
    TheGame(None)    


if __name__ == "__main__":
    Main()


'''

def TheGame(letter):
    with open("words.json", "r") as f:
            words_data = json.load(f)
            the_hidden_word = choice(words_data["data"])
    print(the_hidden_word)
    while(not all(char == "*" for char in the_hidden_word)):
        
        letter = GuessTheLetter()
        positions = []
        for i, char in enumerate(the_hidden_word):
            if char == letter:
                positions.append(i)
            
        if letter in the_hidden_word:
            print("it is valid")
            print(f"the letter is the {positions}. character")
      
            the_hidden_word = ChangeLetter(positions, theletterto, the_hidden_word)
            print(the_hidden_word)
            if all(char == "*" for char in the_hidden_word):
                print("congrulations!")
                TheGame(None)
            continue
            
        else:
            print("No")
            break




def Main():
    TheGame(None)    


if __name__ == "__main__":
    Main()

    '''