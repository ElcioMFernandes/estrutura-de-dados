class Node:
    def __init__(self):
        self.__valor = 0
        self.__prox = None

    def setValor(self, valor):
        self.__valor = valor

    def getValor(self):
        return self.__valor
    
    def setProx(self, p):
        self.__prox = p
        
    def getProx(self):
        return self.__prox

class Fila:
    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push(self):
        novo = Node()
        if novo:
            novo.setValor(int(input('Valor para inserir: ')))
            if self.__fim:
                self.__fim.setProx(novo)
                self.__fim = novo
            else:
                self.__ini = self.__fim = novo

    def pop(self):
        if self.__ini:
            self.__ini = self.__ini.getProx()
            if not self.__ini:
                self.__fim = None
        else:
            print('Fila vazia...')

    def printall(self):
        if self.__fim:
            saida = '\nFila:\n'
            temp = self.__ini
            while temp:
                saida += str(temp.getValor()) + '\t'
                temp = temp.getProx()
            print(saida)
        else:
            print('\nFila vazia...')

    def media(self):
        if self.__fim:
            soma = qtde = 0
            temp = self.__ini
            while temp:
                soma += temp.getValor()
                qtde += 1
                temp = temp.getProx()
            print('Média: %.2f' % (soma/qtde))
        else:
            print('\nFila vazia...')

f = Fila()
while True:
    op = int(input('\nMenu\n1-Ler\n2-Excluir\n3-Imprimir\n4-Média\n5-Sair\nOpção: '))
    if op == 1:
        f.push()
    elif op == 2:
        f.pop()
    elif op == 3:
        f.printall()
    elif op == 4:
        f.media()
    elif op == 5:
        break
    else:
        print('Opção inválida...')