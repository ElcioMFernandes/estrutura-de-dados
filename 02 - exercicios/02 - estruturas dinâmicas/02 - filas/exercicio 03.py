## Inclua no programa anterior a opção de imprimir o primeiro elemento da fila.

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
    def __init__(self):
        self.__start = None
        self.__end = None

    ## Função para inserir um novo nome na fila
    def push(self):
        new = Node() ## Instancia um novo nó
        if new:
            new.set_value(input('Nome para inserir: ')) ## Valor do nó
            if self.__end: ## Se a fila não estiver vazia
                self.__end.set_next(new) ## O próximo do último nó é o novo nó
                self.__end = new ## O novo nó é o último nó
            else: ## Se a fila estiver vazia
                self.__start = self.__end = new ## O novo nó é o primeiro e o último nó

    ## Função para remover o primeiro nome da fila
    def pop(self):
        if self.__start: ## Se a fila não estiver vazia
            self.__start = self.__start.get_next() ## O primeiro nó é o próximo do primeiro nó
            if not self.__start: ## Se a fila ficar vazia
                self.__end = None
        else: ## Se a fila estiver vazia
            print('Fila vazia...')

    ## Função para imprimir todos os nomes da fila
    def print_all(self):
        if self.__end: ## Se a fila não estiver vazia
            output = '\nFila:\n' 
            temp = self.__start ## Nó temporário
            while temp: ## Enquanto houver um nó
                output += temp.get_value() + '\t' ## Adiciona o valor do nó na saída
                temp = temp.get_next() ## O nó temporário recebe o próximo nó
            print(output)
        else: ## Se a fila estiver vazia
            print('\nFila vazia...')

    ## Função para imprimir o primeiro nome da fila
    def print_first(self):
        if self.__start: ## Se a fila não estiver vazia
            print('Primeiro da fila:', self.__start.get_value())

## Menu
queue = Queue() ## Instancia a fila
while True:
    print('\n1 - Inserir\n2 - Remover\n3 - Imprimir\n0 - Sair')
    op = input('Opção: ')
    if op == '1': ## Inserir
        queue.push()   
        queue.print_all()
    elif op == '2': ## Remover
        queue.pop()
        queue.print_all()
    elif op == '3': ## Imprimir
        queue.print_all()
    elif op == '0': ## Sair
        break
    else:
        print('Opção inválida...')