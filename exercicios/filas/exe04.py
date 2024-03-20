class Fila:
    __fila = []

    def __validFila(self):
        if self.__fila:
            return True
        else:
            print('Fila vazia!')
            return False

    def __insertNew(self):
        value = input('Informe um valor.\n>> ')
        try:
            value = int(value)
            self.__fila.append(value)
        except:
            print('O valor informado precisa ser númerico!\n')
            self.__insertNew()

    def __delFirst(self):
        if self.__validFila:
            self.__fila.pop(0)

    def __strFirst(self):
        if self.__validFila:
            print(self.__fila[0])

    def __strAll(self):
        if self.__validFila:
            fila_aux = []
            string = ''
            while self.__fila:
                string += f"{self.__fila[0]}, "
                fila_aux.append(self.__fila.pop(0))
            else:
                print(string)
                while fila_aux:
                    self.__fila.append(fila_aux.pop(0))
                else:
                    string = ''

    def __delAll(self):
        if self.__validFila:
            while self.__fila:
                self.__fila.pop(0)

    def __reversed(self):
        if self.__validFila:
            pilha = []
            while self.__fila:
                pilha.append(self.__fila.pop(0))
            else:
                while pilha:
                    self.__fila.append(pilha.pop())

    def __str(self):
        if self.__validFila:
            pares = ''
            impares = ''
            for num in self.__fila:
                if num % 2 == 0:
                    pares += f"{num},"
                else:
                    impares += f"{num}, "
            else:
                print(f"Pares: {pares}\nImpares: {impares}")

    def __exit(self):
        self.__fila = []
        exit()

    def __menu(self):
        OPTIONS = {
            '1':self.__insertNew,
            '2':self.__delFirst,
            '3':self.__strFirst,
            '4':self.__strAll,
            '5':self.__delAll,
            '6':self.__reversed,
            '7':self.__str,
            '8':self.__exit,
        }

        option = input('1 - Incluir inteiro na fila\n2 - Excluir inteiro da fila\n3 - Imprimir o primeiro inteiro da fila\n4 - Imprimir todos os inteiros da fila\n5 - Excluir todos os inteiros da fila\n6 - Inverter os inteiros da fila\n7 - Imprimir os inteiros pares e depois os inteiros ímpares da fila\n8 - Sair\n\n>> ')
        
        function = OPTIONS.get(option)

        if function:
            function()
            self.__menu()

        else:
            print('Opção inválida, tente novamente!')
            self.__menu()

    def __init__(self):
        self.__menu()

example = Fila()