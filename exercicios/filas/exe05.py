## Faça um programa que cadastre em uma pilha vários
## números. A entrada deles será finalizada com a digitação de
## um número menor ou igual a zero.
## Posteriormente, o programa deve gerar duas filas, a primeira
## com os números pares e a segunda com os números ímpares.
## A saída do programa deve apresentar a pilha digitada e as
## filas geradas. Caso alguma das filas seja vazia, deve-se
## imprimir “Fila vazia”.

class Row:
    __stack = None
    __row_pair = None
    __row_odd = None

    def __validate(self, argument_to_validate):
        if argument_to_validate:
            return True
        else:
            return False

    def __to_string(self, attribute, index=0):
        string = ''
        if self.__validate(attribute):
            while attribute:
                string += f"{self.__stack.pop(index)}, "
            else:
                return string

    def __present_attributes(self):
        stack = self.__to_string(self.__stack, -1)
        print(f"Stack = {stack}")
        odd = self.__to_string(self.__row_odd)
        print(f"Odd row = {odd}")
        pair = self.__to_string(self.__row_pair)
        print(f"Even  queue = {pair}")
        exit(0)

    def __set_odd_pair(self):
        if self.__validate(self.__stack):
            auxiliary_battery = []
            while self.__stack:
                auxiliary_battery.append(self.__stack.pop())
                if auxiliary_battery[-1] % 2 == 0:
                    self.__row_pair.append(auxiliary_battery[-1])
                else:
                     self.__row_odd.append(auxiliary_battery[-1])
            else:
                while auxiliary_battery:
                    self.__stack.append(auxiliary_battery.pop())
        else:
            print('Empty stack')
            exit(0)

    def __set_stack(self):
        flag = True
        while flag:
            value = input("Enter a value: ")
            try:
                value = int(value)
                if value > 0:
                    self.__stack.append(value)
                else:
                    flag = False
            except ValueError:
                print("Value invalid :(, but don't worry, try again... =D")
                self.__set_stack()

    def __main(self):
        try:
            self.__set_stack()
            self.__set_odd_pair()
            self.__present_attributes()
        except Exception as e:
            print(e)

    def __init__(self):
        self.__stack = []
        self.__row_pair = []
        self.__row_odd = []
        self.__main()
        
teste = Row()
