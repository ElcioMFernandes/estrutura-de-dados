## Altere o programa anterior, para permitir a exclusão de um nome na lista (na primeira ocorrência que encontrar).

import collections as cl

class Lista:
    ## Atributos
    __list = cl.deque()

    ## Construtor
    def __init__(self) -> None:
        '''Construtor'''
        self.inserir_nomes()

    ## Métodos
    def inserir_nomes(self):
        '''Insere nomes na lista'''
        flag = True
        while flag:
            value = input('>> ')
            if value:
                if not self.__list:
                    self.__list.append(value)
                else:
                    index = 0
                    while index < len(self.__list) and value > self.__list[index]:
                        index += 1
                    self.__list.insert(index, value)
            else:
                flag = False
                while self.__list:
                    print(self.__list.popleft())
                    return

if __name__ == '__main__':
    Lista()