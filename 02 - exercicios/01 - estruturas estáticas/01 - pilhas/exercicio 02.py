## Construa um programa com as
## seguintes opções no menu:
## 1 – Incluir novo nome na pilha
## 2 – Excluir o nome do topo da pilha
## 3 – Imprimir o nome do topo da pilha
## 4 – Imprimir todos os nomes da pilha
## 5 – Excluir todos os nomes da pilha
import os
class Stack:
    __stack = []

    def validStack(self):
        if len(self.__stack) > 0:
            return True
        else:
            print('\nATENÇÃO, pilha vazia!')

    def insertValueStack(self):
        value = input('\nPor favor, informe um valor:')
        self.__stack.append(value)

    def deleteValueStack(self):
        if self.validStack():
            self.__stack.pop()

    def getTopValueStack(self):
        if self.validStack():
            print(self.__stack[-1])

    def getWholeStack(self):
        if self.validStack():
            auxiliary_stack = []
            while self.__stack:
                self.getTopValueStack()
                auxiliary_stack.append(self.__stack.pop())
            else:
                while auxiliary_stack:
                    self.__stack.append(auxiliary_stack.pop())

    def deleteWholeStack(self):
        if self.validStack():
            while self.__stack:
                self.__stack.pop()

    def menuStack(self):
        OPTIONS = {
            '1':self.insertValueStack,
            '2':self.deleteValueStack,
            '3':self.getTopValueStack,
            '4':self.getWholeStack,
            '5':self.deleteWholeStack,
            '6':exit
        }
        print('\n1 - Inserir valor\n2 - Deletar topo\n3 - Valor topo\n4 - Toda a pilha\n5 - Deletar pilha\n6 - Sair')
        option = input('\nSelecione uma opção: ')
        function = OPTIONS.get(option)
        if function:
            function()
            self.menuStack()
        else:
            self.menuStack()

    def __init__(self):
        self.menuStack()

example = Stack()