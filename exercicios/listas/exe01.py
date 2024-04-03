## Construa um programa para incluir uma lista de nomes (inclusão no final da lista).

import collections as cl

class Lista:
    ## Atributos
    __lista = None

    def __init__(self) -> None:
        '''Construtor'''
        self.__lista = cl.deque()
        self.menu()

    ## Menu
    def menu(self):
        '''Menu de opções'''
        OPTIONS = {
            1: self.apresentar_dados,
            2: self.incluir_final,

            0: exit
        }
        while True:
            print('========MENU========\n1. Apresentar dados\n2. Incluir no final\n0. Sair\n====================')
            opcao = int(input('Escolha uma opção: '))
            if opcao in OPTIONS:
                OPTIONS[opcao]()
            else:
                print('Opção inválida')
                
    ## Métodos
    def apresentar_dados(self):
        '''Apresenta os dados da lista'''
        fila_auxiliar = cl.deque()

        while self.__lista:
            print(self.__lista[0])
            fila_auxiliar.append(self.__lista.popleft())
    
        while fila_auxiliar:
            self.__lista.append(fila_auxiliar.popleft())

    def incluir_final(self) -> None:
        '''Inclui um valor no final da lista'''
        valor = input('Digite o valor: ')

        if valor:
            self.__lista.append(valor)

if __name__ == "__main__":
    Lista()