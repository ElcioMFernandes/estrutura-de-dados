## Faça um programa que cadastre em uma pilha vários
## números. A entrada deles será finalizada com a digitação de
## um número menor ou igual a zero.
## Posteriormente, o programa deve gerar duas filas, a primeira
## com os números pares e a segunda com os números ímpares.
## A saída do programa deve apresentar a pilha digitada e as
## filas geradas. Caso alguma das filas seja vazia, deve-se
## imprimir “Fila vazia”.

class Queue:
    __stack = None
    __pair = None
    __odd = None

    def __init__(self) -> None:
        self.__stack = []
        self.__pair = []
        self.__odd = []
        self.entry_stack() 
        print(self.__str__())

    def __str__(self) -> str:
        string = 'Pilha:\n\n'
        while self.__stack:
            string += f"[{self.__stack.pop()}]\n"
        
        string += ' ^ Fim da pilha\n\nÍmpares: '

        if self.__odd:
            while self.__odd:
                string += f"{self.__odd.pop(0)}, "
        else:
            string += 'Fila vazia'
        
        string += '\nPares: '
        if self.__pair:    
            while self.__pair:
                string += f"{self.__pair.pop(0)}, "
        else:
            string += 'Fila vazia'

        return string

    def entry_stack(self) -> None:
        flag = True
        while flag:
            value = input('Entre com um valor: ')
            try:
                value = int(value)
                if value > 0:
                    self.__stack.append(value)
                else:
                    flag = False
                    self.separate()

            except ValueError:
                print(f'Valor {value} inválido.')

    def separate(self):
        if self.__stack:
            aux = []
            while self.__stack:
                aux.append(self.__stack[-1])

                if self.__stack[-1] % 2 == 0:
                    self.__pair.append(self.__stack.pop())
                else:
                    self.__odd.append(self.__stack.pop())

            else:
                while aux:
                    self.__stack.append(aux.pop())

if __name__ == '__main__':
    Queue()