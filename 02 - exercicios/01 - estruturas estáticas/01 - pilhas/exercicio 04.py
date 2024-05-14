## Escreva um programa usando
## pilhas para determinar se uma
## string é um palíndromo.

class Palindromo():
    __word = ''

    def __reversedWord(self):
        vectorWord = []
        reversedWord = ''
        for letter in self.__word:
            vectorWord.append(letter)
        else:
            while vectorWord:
                reversedWord += vectorWord.pop()
            else:
                print(reversedWord)
                print(self.__word)
                print(reversedWord == self.__word)

    def __inputWord(self):
        self.__word = input("Insira a palavra: ")
        self.__reversedWord()

    def __init__(self):
        self.__inputWord()

example = Palindromo()