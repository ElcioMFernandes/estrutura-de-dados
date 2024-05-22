# Exemplo Fila Circular

import sys

class no_fila:
    def __init__(self):
        self.__nome = None
        self.__prox = None

    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome
    def getprox(self):
        return self.__prox
    def setprox(self, prox):
        self.__prox = prox

class Fila:
    def __init__(self):
        self.__fim = None

    def __del__(self):
        self.__fim = None

    def push(self):
        temp_no = no_fila()
        if temp_no:
            temp_no.setnome(input("Entre com um nome: "))
            if self.__fim:
                temp_no.setprox(self.__fim.getprox())
                self.__fim.setprox(temp_no)
            else:
                temp_no.setprox(temp_no)
            self.__fim = temp_no
        Fila.printall(self)

    def pop(self):
        if self.__fim:
            print("\nNome a remover: ", self.__fim.getprox().getnome())
            resp = input("Confirma? [S/N] ").upper()
            if resp == 'S':
                if self.__fim.getprox() is not self.__fim:
                    self.__fim.setprox(self.__fim.getprox().getprox())
                else:
                    self.__fim = None
        Fila.printall(self)

    def printall(self):
        if not self.__fim:
            print("Fila vazia...")
            return
        temp_no = self.__fim.getprox()
        saida = "Fila:\n"
        while True:
            saida += temp_no.getnome() + "  Endereço: " + str(temp_no) + \
                   "  " + "  Próximo: " + str(temp_no.getprox()) + "\n"
            temp_no = temp_no.getprox()
            if temp_no is self.__fim.getprox():
                break
        print(saida)

#############################################################################


f = Fila()
while True:
    op = int(input("\n1 - Inserir\n2 – Remover\n3 - Imprime a fila\n"
                   "4 - Sair\n\nOpcao: "))
    if op == 1:
        f.push()
    elif op == 2:
        f.pop()
    elif op == 3:
        f.printall()
    else:
        del f
        sys.exit()