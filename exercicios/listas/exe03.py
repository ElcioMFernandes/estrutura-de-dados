## Altere o programa anterior, para permitir a inclusão de um nome no meio da lista, ou após uma “chave”

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
            3: self.incluir_inicio,
            4: self.incluir_meio,
            0: exit
        }
        while True:
            print('========MENU========\n1. Apresentar dados\n2. Incluir no final\n3. Incluir no início\n4. Incluir no meio\n0. Sair\n====================')
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

    def incluir_final(self):
        '''Inclui um valor no final da lista'''
        valor = input('Digite o valor: ')

        if valor:
            self.__lista.append(valor)

    def incluir_inicio(self):
        '''Inclui um valor no início da lista'''
        valor = input('Digite o valor: ')

        if valor:
            self.__lista.appendleft(valor)

    def incluir_meio(self):
        '''Inclui um valor no meio da lista'''
        valor = input('Digite o valor: ')
        chave = input('Digite a chave: ')

        if valor and chave:
            try:
                pos = self.__lista.index(chave)
                self.__lista.insert(pos+1, valor)
            except ValueError:
                print('Chave não encontrada')

if __name__ == "__main__":
    Lista()