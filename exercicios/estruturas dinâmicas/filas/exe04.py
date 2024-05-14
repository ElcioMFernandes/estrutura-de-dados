## Construa um programa para manipular elementos inteiros na fila, com as seguintes opções no menu:
## 1 – Incluir inteiro na fila
## 2 – Excluir inteiro da fila
## 3 – Imprimir o primeiro inteiro da fila
## 4 – Imprimir todos os inteiros da fila
## 5 – Excluir todos os inteiros da fila
## 6 – Inverter os inteiros da fila
## 7 – Imprimir os inteiros pares e depois os inteiros ímpares

## Classe para o nó
class Node:
    def __init__ (self):
        self.__value = None ## Valor do nó
        self.__next = None ## Próximo nó

    def set_value(self, value): ## Função para definir o valor do nó
        self.__value = value

    def get_value(self): ## Função para obter o valor do nó
        return self.__value
    
    def set_next(self, next): ## Função para definir o próximo nó
        self.__next = next

    def get_next(self): ## Função para obter o próximo nó
        return self.__next

## Classe para a fila
class Queue:
    def __init__(self) -> None:
        self.__start = None ## Início da fila
        self.__end = None ## Fim da fila

    def push(self) -> None: ## Função para inserir um novo inteiro na fila
        new = Node() ## Instancia um novo nó
        if new:
            new.set_value(int(input('Valor para inserir: ')))
            if self.__end: ## Se a fila não estiver vazia
                self.__end.set_next(new) ## O último nó aponta para o novo nó
                self.__end = new ## O novo nó é o último nó
            else: ## Se a fila estiver vazia
                self.__start = self.__end = new ## O novo nó é o primeiro e o último nó

    def pop(self) -> None: ## Função para remover o primeiro inteiro da fila
        if self.__start: ## Se a fila não estiver vazia
            self.__start = self.__start.get_next() ## O primeiro nó é o próximo nó
            if not self.__start: ## Se a fila estiver vazia
                self.__end = None ## O último nó é nulo
        else:
            print('Fila vazia...')

    def get(self) -> None: ## Função para imprimir o primeiro inteiro da fila
        if self.__start: ## Se a fila não estiver vazia
            print('Primeiro da fila:', self.__start.get_value()) ## Imprime o valor do primeiro nó
        
    def pop_all(self) -> None: ## Função para remover todos os inteiros da fila
        self.__start = self.__end = None ## O início e o fim da fila são nulos

    def get_all(self) -> None: ## Função para imprimir todos os inteiros da fila
        if self.__end: ## Se a fila não estiver vazia
            output = '\nFila:\n' 
            temp = self.__start ## Nó temporário
            while temp: ## Enquanto houver um nó
                output += str(temp.get_value()) + '\t'
                temp = temp.get_next() ## O nó temporário recebe o próximo nó
            print(output)
        else:
            print('\nFila vazia...')

    def invert(self) -> None: ## Função para inverter os inteiros da fila
        if self.__end: ## Se a fila não estiver vazia
            temp = self.__start ## Nó temporário
            prev = None ## Nó anterior
            while temp: ## Enquanto houver um nó
                next = temp.get_next() ## Próximo nó
                temp.set_next(prev) ## O próximo nó é o nó anterior
                prev = temp ## O nó anterior é o nó atual
                temp = next ## O nó atual é o próximo nó
            self.__start = prev ## O início da fila é o nó anterior
        else:
            print('\nFila vazia...')
    
    def get_even_odd(self) -> None: ## Função para imprimir os inteiros pares e depois os ímpares
        if self.__end: ## Se a fila não estiver vazia
            even = odd = '' ## Variáveis para os inteiros pares e ímpares
            temp = self.__start ## Nó temporário
            while temp: ## Enquanto houver um nó
                if temp.get_value() % 2 == 0: ## Se o valor do nó for par
                    even += str(temp.get_value()) + '\t'
                else: ## Se o valor do nó for ímpar
                    odd += str(temp.get_value()) + '\t'
                temp = temp.get_next() ## O nó temporário recebe o próximo nó
            print('Pares:', even)
            print('Ímpares:', odd)
        else:
            print('\nFila vazia...')

queue = Queue()

## Menu
while True:
    print('\n1 – Incluir inteiro na fila')
    print('2 – Excluir inteiro da fila')
    print('3 – Imprimir o primeiro inteiro da fila')
    print('4 – Imprimir todos os inteiros da fila')
    print('5 – Excluir todos os inteiros da fila')
    print('6 – Inverter os inteiros da fila')
    print('7 – Imprimir os inteiros pares e depois os inteiros ímpares')
    print('0 - Sair')
    op = input('Opção: ')
    if op == '1':
        queue.push()
    elif op == '2':
        queue.pop()
    elif op == '3':
        queue.get()
    elif op == '4':
        queue.get_all()
    elif op == '5':
        queue.pop_all()
    elif op == '6':
        queue.invert()
    elif op == '7':
        queue.get_even_odd()
    elif op == '0':
        break
    else:
        print('Opção inválida...')