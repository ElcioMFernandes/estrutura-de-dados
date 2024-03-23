## Construa um programa que insere nomes em uma fila, imprimindo a
## fila completa a cada inserção.

class Fila:
    __fila = []

    def __get_fila(self):
        fila_aux = []
        while self.__fila:
            print(self.__fila[0])
            fila_aux.append(self.__fila.pop(0))
        else:
            while fila_aux:
                self.__fila.append(fila_aux.pop(0))

    def __set_fila(self):
        while True:
            value = input('Valor(stop para parar): ')
            if value != 'stop':
                self.__fila.append(value)
                self.__get_fila()
            else:
                exit()

    def __init__(self):
        self.__set_fila()

example = Fila()
