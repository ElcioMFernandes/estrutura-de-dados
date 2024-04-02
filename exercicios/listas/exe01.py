## Construa um programa para incluir uma lista de nomes (inclusão no final da lista).

import collections as cl

class Lista:
    __lista = None

    def __init__(self) -> None:
        self.__lista = cl.deque()
    
if __name__ == "__main__":
    Lista()