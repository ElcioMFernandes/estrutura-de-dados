## Construa um programa que, a partir de lista encadeada L desordenada,
## tenha uma função que cria uma nova lista K ordenada, com os
## mesmos nós da lista L.
## A função remove os elementos da lista L, e insere-os na lista K,
## que dessa forma torna-se uma lista ordenada (em ordem crescente).
## Observações:
## • Não devem ser criados nós extras, deve-se utilizar os mesmos nós
## alocados para a lista L.
## • No final do processo, a lista L estará vazia e a lista K conterá os nós
## anteriormente alocados para a lista L.

class Node:
    def __init__(self) -> None:
        self.__data = None
        self.__next = None

    def set_data(self, data: int) -> None:
        self.__data = data

    def get_data(self) -> int:
        return self.__data

    def set_next(self, next: 'Node') -> None:
        self.__next = next

    def get_next(self) -> 'Node':
        return self.__next

class LinkedList:
    def __init__(self) -> None:
        self.__initial = None
        self.__end = None

    def push(self, value=None) -> None:
        node = Node() ## Instancia um novo nó
        if node: ## Se o nó foi instanciado
            if value:
                node.set_data(value)
            else:
                node.set_data(int(input('Digite um número: '))) ## Setando o valor do nó
                
            if not self.__initial: ## Se a lista estiver vazia
                self.__initial = self.__end = node ## O nó assume o início e o fim da lista
            elif node.get_data() <= self.__initial.get_data(): ## Se não, se o valor do nó for menor ou igual ao valor do início da lista
                node.set_next(self.__initial) ## Seta o próximo nó como o início da lista
                self.__initial = node ## O nó assume o início da lista
            elif node.get_data() >= self.__end.get_data(): ## Se não, se o valor do nó for maior ou igual ao valor do fim da lista
                self.__end.set_next(node) ## Seta o próximo nó como o fim da lista
                self.__end = node ## O nó assume o fim da lista
            else: ## Se não
                current = self.__initial ## Cria um nó auxiliar que começa no início da lista
                while current.get_next().get_data() < node.get_data(): ## Enquanto o valor do próximo nó for menor que o valor do nó
                    current = current.get_next() ## O nó auxiliar assume o próximo nó
                node.set_next(current.get_next()) ## Seta o próximo nó como o próximo nó do nó auxiliar
                current.set_next(node) ## O nó auxiliar assume o nó
        else: ## Se o nó não foi instanciado
            print('Memória insuficiente')

    def pop(self) -> None:
        if self.__initial: ## Se a lista não estiver vazia
            data = int(input('Digite um número para excluir: '))
            node = self.__initial ## Cria um nó auxiliar que começa no início da lista
            if data == node.get_data(): ## Se o valor do nó for igual ao valor a ser excluído
                self.__initial = node.get_next() ## O início da lista assume o próximo nó
                if not self.__initial: ## Se a lista estiver vazia
                    self.__end = None ## O fim da lista é nulo
                return
            while node.get_next(): ## Enquanto houver um próximo nó
                if data == node.get_next().get_data(): ## Se o valor do próximo nó for igual ao valor a ser excluído
                    node.set_next(node.get_next().get_next()) ## O próximo nó do nó assume o próximo nó do próximo nó
                    if not node.get_next(): ## Se o próximo nó for nulo -> Caso o nó excluído seja o último
                        self.__end = node ## O nó auxiliar assume o fim da lista
                    break ## Encerra o loop
                node = node.get_next() ## O nó auxiliar assume o próximo nó
        else: ## Se a lista estiver vazia
            print('Lista vazia') ## Exibe uma mensagem

    def show(self) -> None: 
        if self.__initial: ## Se a lista não estiver vazia
            current = self.__initial ## Cria um nó auxiliar que começa no início da lista
            while current: ## Enquanto houver um nó
                print(current.get_data()) ## Exibe o valor do nó
                current = current.get_next() ## current assume o próximo nó
        else: ## Se a lista estiver vazia
            print('Lista vazia') ## Exibe uma mensagem

    def empty(self) -> None:
        self.__initial = self.__end = None ## O início e o fim da lista são nulos, esvaziando a lista

    def order(self) -> None:
        K = LinkedList()
        while self.__initial:
            current = self.__initial
            K.push(current.get_data())

linked_list = LinkedList()
while True:
    print('1 - Inserir um número')
    print('2 - Excluir um número')
    print('3 - Consultar a lista')
    print('4 - Esvaziar a lista')
    print('5 - Sair')
    option = int(input('Digite uma opção: '))
    if option == 1:
        linked_list.push()
    elif option == 2:
        linked_list.pop()
    elif option == 3:
        linked_list.show()
    elif option == 4:
        linked_list.empty()
    elif option == 5:
        break
    else:
        print('Opção inválida')