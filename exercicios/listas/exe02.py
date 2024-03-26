## Altere o programa anterior, para permitir a inclusão de um nome no início da lista.

import collections

class List:
    __list = None 

    def __init__(self) -> None:
        '''Método construtor'''
        self.__list = collections.deque()
        self.menu()

    def menu(self) -> None:
        '''Método de menu'''
        OPTIONS = {
            '1': self.insert_last,
            '2': self.insert_first,
            '3': self.__str__
        }
        op = input('1. Inserir último\n2. Inserir primeiro\n3. Apresentar\n>> ')
        
        if op in OPTIONS.keys():
            OPTIONS[op]()
            self.menu()

        else:
            print('Opção inválida, tente novamente.')
            self.menu()

    def insert_last(self) -> None:
        '''Método que insere um valor no último índice'''
        value = input("\nInserir valor >> ")
        if value:
            self.__list.append(value)

    def insert_first(self) -> None:
        '''Método que insere um valor no primeiro índice'''
        value = input("\nInserir valor>> ")
        if value:
            self.__list.appendleft(value)

    def __str__(self) -> None:
        '''Printa a lista'''
        print(f'{self.__list}')

if __name__ == '__main__':
    List()