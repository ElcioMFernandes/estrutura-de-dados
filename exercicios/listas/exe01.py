## Construa um programa para incluir uma lista de nomes (inclusão no final da lista).
import collections

class List:
    __list = None 

    def __init__(self) -> None:
        self.__list = collections.deque()
        self.insert()

    def insert(self) -> None:
        flag = True
        while flag:
            value = input(">> ")
            if value:
                self.__list.append(value)
            else:
                flag = False
        else:
            print(self)

    def __str__(self) -> str:
        return f'{self.__list}'

if __name__ == '__main__':
    List()