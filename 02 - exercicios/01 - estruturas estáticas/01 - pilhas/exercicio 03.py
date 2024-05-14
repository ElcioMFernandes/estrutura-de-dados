## Construa um programa para ler
## uma palavra, imprimindo-a em
## ordem inversa. Uma pilha de letras
## será usada para inverter a palavra.
## Primeiro, os caracteres são
## extraídos um por um da cadeia de
## entrada e empilhados. Então eles
## são desempilhados e exibidos. Por
## causa da característica LIFO, a pilha
## inverte a ordem dos caracteres.

class Stack:
    __word = None

    def concatStack(self, stack):
        string = ''
        for letter in stack:
            string += letter
        else:
            print(string)

    def __reversedVector(self, stack):
        auxiliary_stack = []
        while stack:
            auxiliary_stack.append(stack.pop())
        else:
            self.concatStack(auxiliary_stack)

    def __stringToVector(self):
        wordStack = []
        for letter in self.__word:
            wordStack.append(letter) 
        else:
            self.__reversedVector(wordStack)

    def __inputWord(self):
        self.__word = input("Insira a palavra: ")
        self.__stringToVector()

    def __init__(self):
        self.__inputWord()

example = Stack()