class Node:
    def __init__(self):
        self.__valor = None
        self.__prox = None

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def get_prox(self):
        return self.__prox

    def set_prox(self, prox):
        self.__prox = prox

class Lista:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def push_inicio(self):
        novo = Node()
        valor = input('Digite um valor: ')
        novo.set_valor(valor)
        if self.__inicio == None:
            self.__inicio = novo
            self.__fim = novo
        else:
            novo.set_prox(self.__inicio)
            self.__inicio = novo

    def push_fim(self):
        novo = Node()
        valor = input('Digite um valor: ')
        novo.set_valor(valor)
        if self.__inicio == None:
            self.__inicio = novo
            self.__fim = novo
        else:
            self.__fim.set_prox(novo)
            self.__fim = novo

    def pop(self):
        valor = input('Digite o valor a ser removido: ')
        if self.__inicio == None:
            print('Lista vazia')
        elif self.__inicio.get_valor() == valor:
            self.__inicio = self.__inicio.get_prox()
        else:
            atual = self.__inicio
            prox = atual.get_prox()
        while prox != None:
            if prox.get_valor() == valor:
                atual.set_prox(prox.get_prox())
                break
            atual = prox
            prox = prox.get_prox()

    def print_lista(self):
        if self.__inicio == None:
            print('Lista vazia')
        else:
            atual = self.__inicio
            while atual != None:
                print(atual.get_valor())
                atual = atual.get_prox()

    def pop_todos(self):
        self.__inicio = None
        self.__fim = None
        
lista = Lista()
while True:
    print('1 - Inserir no início')
    print('2 - Inserir no fim')
    print('3 - Remover')
    print('4 - Imprimir')
    print('5 - Remover todos')
    print('6 - Sair')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        lista.push_inicio()
    elif opcao == 2:
        lista.push_fim()
    elif opcao == 3:
        lista.pop()
    elif opcao == 4:
        lista.print_lista()
    elif opcao == 5:
        lista.pop_todos()
    elif opcao == 6:
        break
    else:
        print('Opção inválida')