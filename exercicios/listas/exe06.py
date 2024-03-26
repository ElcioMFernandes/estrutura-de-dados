## Altere o programa anterior, para permitir a exclusão de um nome no meio da lista, na primeira ocorrência que encontrar.

import collections, sys

class List:
    __list = None 

    def __init__(self) -> None:
        '''Método construtor'''
        self.__list = collections.deque()
        self.menu()

    def menu(self) -> None:
        '''Método de menu'''
        OPTIONS = {
            '0': sys.exit,
            '1': self.insert_last,
            '2': self.insert_first,
            '3': self.insert_middle,
            '4': self.del_first,
            '5': self.del_last,
            '6': self.del_middle,
            '7': self.__str__
        }
        op = input('1. Inserir último\n2. Inserir primeiro\n3. Inserir no meio\n4. Deletar primeiro\n5. Deletar último\n6. Deletar meio\n7. Apresentar\n0. Sair\n>> ')
        
        if op in OPTIONS.keys():
            OPTIONS[op]()
            self.menu()

        else:
            print('Opção inválida, tente novamente.')
            self.menu()

    def __str__(self) -> None:
        '''Printa a lista'''
        print(f'{self.__list}')

    def insert_last(self) -> None:
        '''Método que insere um valor no último índice'''
        value = input("\nInserir valor >> ")
        if value:
            self.__list.append(value)

    def insert_first(self) -> None:
        '''Método que insere um valor no primeiro índice'''
        value = input("\nInserir valor >> ")
        if value:
            self.__list.appendleft(value)

    def insert_middle(self):
        '''Método para inserir no meio da lista'''
        index = input('\nInsira o índice de alocação >> ')
        if index:
            index = int(index)
            value = input('\nInserir valor >> ')
            if value: 
                self.__list.insert(index, value)
        else:
            if len(self.__list) % 2 == 0:
                value = input('\nInserir valor >> ')
                if value:
                    self.__list.insert(len(self.__list) / 2, value)
            else:
                value = input('\nInserir valor >> ')
                self.__list.insert((int(len(self.__list) / 2 + 0.5)), value)

    def del_first(self):
        '''Método para deletar o primeiro elemento da lista'''
        self.__list.popleft()

    def del_last(self):
        '''Método para deletar o primeiro elemento da lista'''
        self.__list.pop()

    def del_middle(self):
        '''Método para deletar um elemento no meio da lista'''
        

if __name__ == '__main__':
    List()