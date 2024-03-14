class Pilha:
    __pilha_principal = []
    
    def get_last(self, pilha=None):
        """Retorna o elemento no topo da pilha"""
        if pilha is None:
            pilha = self.__pilha_principal
        return pilha[-1]
    
    def get_all(self):
        pilha_auxiliar = []
        """Desempilha todos os elementos da pilha e os retorna"""
        for i in range(0, len(self.__pilha_principal), 1):
            print(f"Elemento {i+1}: {self.get_last()}")
            pilha_auxiliar.append(self.__pilha_principal.pop())
        else:
            for i in range(0, len(pilha_auxiliar), 1):
                self.__pilha_principal.append(pilha_auxiliar.pop())

    def __set_pilha(self):
        """Define valores para aleatorios para a pilha principal"""
        import random
        for i in range(5):
            self.__pilha_principal.append(random.randint(1, 100))

    def __init__(self, pilha=None):
        if pilha is not None:
            self.__pilha_principal = pilha
        else:
            self.__set_pilha()

pl = Pilha()
pl.get_all()