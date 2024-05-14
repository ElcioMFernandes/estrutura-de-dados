class Node: ## Classe para o nó

    def __init__(self) -> None: ## Método construtor do nó
        self.__value = None ## Valor do nó
        self.__next = None ## Endereço do próximo nó

    def get_value(self): ## Método para obter o valor do nó
        return self.__value ## Retorna o valor do nó

    def set_value(self, value): ## Método para definir o valor do nó
        self.__value = value ## Define o valor do nó

    def get_next(self): ## Método para obter o endereço do próximo nó
        return self.__next ## Retorna o endereço do próximo nó

    def set_next(self, __next): ## Método para definir o endereço do próximo nó
        self.__next = __next ## Define o endereço do próximo nó

class Stack: ## Classe para a pilha

    def __init__(self): ## Método construtor da pilha
        self.__top = None ## Topo da pilha
        
    def push(self): ## Método para inserir um novo valor na pilha
        new = Node() ## Instancia um novo nó
        if new: ## Se o nó foi instanciado
            new.set_value(int(input("value: "))) ## Define o valor do nó
            new.set_next(self.__top) ## O próximo do novo nó é o topo da pilha
            self.__top = new ## O novo nó é o topo da pilha

    def pop(self): ## Método para remover o valor do topo da pilha
        if self.__top: ## Se a pilha não estiver vazia
            print("value to remove: ", self.__top.get_value()) ## Exibe o valor do topo
            self.__top = self.__top.get_next() ## O topo da pilha é o próximo do topo
        else: ## Se a pilha estiver vazia
            print("empty stack...") ## Exibe mensagem de pilha vazia

    def get_all(self): ## Método para exibir todos os valores da pilha
        if not self.__top: ## Se a pilha estiver vazia
            print("empty stack...") ## Exibe mensagem de pilha vazia
            return ## Encerra o método
        new = self.__top ## Nó temporário
        output = "stack:\n" ## Saída
        while new: ## Enquanto houver um nó
            output += f"{str(new.get_value())}\n" ## Adiciona o valor do nó na saída
            new = new.get_next() ## O nó temporário recebe o próximo nó
        print(output) ## Exibe a saída

## Menu
app = Stack()
while True:
    op = int(input("\n1. stack up\n2. unstack\n3. get stack\n4. quit\n\nentry: "))
    if op == 1:
        app.push()
    elif op == 2:
        app.pop()
    elif op == 3:
        app.get_all()
    else:
        break