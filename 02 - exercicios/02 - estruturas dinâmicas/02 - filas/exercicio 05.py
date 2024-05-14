## Faça um programa que cadastre em uma pilha encadeada vários números. A entrada deles será finalizada com a digitação de um número menor ou igual a zero.
## Posteriormente, o programa deve gerar duas filas encadeadas, a primeira com os números pares e a segunda com os números ímpares.
## A saída do programa deve apresentar a pilha digitada e as filas geradas. Caso alguma das filas seja vazia, deve-se imprimir “Fila vazia”.

class Node:
    def __init__ (self):
        self.__value = None
        self.__next = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value
    
    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next
    
class Stack:
    pass