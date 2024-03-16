## De acordo com o exemplo 1,
## implemente uma função para imprimir
## todos os itens da pilha; e outra função
## para imprimir o topo da pilha. Lembrese, o acesso se dá somente ao
## elemento topo da pilha.

class Stack:
    __stack = []

    def __topStack(self):
        if len(self.__stack) > 0:
            return(self.__stack[-1])

    def __wholeStack(self):
        auxiliary_stack = []
        while self.__stack:
            print(self.__topStack())
            auxiliary_stack.append(self.__stack.pop())
        else:
            while auxiliary_stack:
                self.__stack.append(auxiliary_stack.pop())

    def __setStack(self):
        while True:
            value = input("Valor para pilha(stop para parar):")
            if value == 'stop':
                self.__wholeStack()
                exit()
            else:
                self.__stack.append(value)

    def __init__(self):
        self.__setStack()

example = Stack()