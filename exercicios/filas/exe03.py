## Inclua no programa anterior(filas/exe02.py) a opção de imprimir o primeiro elemento
## da fila.

class Fila:
    __fila = []

    def __valid_fila(self):
        if len(self.__fila) > 0:
            return True

        else:
            return False

    def __setFila(self):

        value = input('Insira um valor:')
        self.__fila.append(value)

    def __delFila(self):

        if self.__valid_fila:
            self.__fila.pop(0)

    def __getFila(self):
        if self.__valid_fila:
            print(self.__fila[0])

    def __allFila(self):

        if self.__valid_fila:
            fila_aux = []
            string = ''

            while self.__fila:
                string += f"{self.__fila[0]}, "
                fila_aux.append(self.__fila.pop(0))

            else:
                print(string)
                
                while fila_aux:
                    self.__fila.append(fila_aux.pop(0))

    def __extFila(self):
        self.__fila = []
        exit()

    def __menu(self):
        OPTIONS = {
            '1':self.__setFila,
            '2':self.__delFila,
            '3':self.__getFila,
            '4':self.__allFila,
            '5':self.__extFila
        }

        option = input('\n1. Inserir\n2. Deletar\n3. Primeiro\n4. Valores\n5. Sair\n\nOpção: ')
        
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
