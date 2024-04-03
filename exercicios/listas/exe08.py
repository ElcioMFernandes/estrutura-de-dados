## Refaça o exercício 07, mas agora, que permita manipular inteiros.

import collections as cl

class Lista:
    ## Atributos
    __lista = None

    ## Construtor
    def __init__(self) -> None:
        '''Construtor'''
        self.__lista = cl.deque()
        self.menu()

    ## Menu
    def menu(self):
        '''Menu de opções'''
        OPTIONS = {
            1: self.apresentar_dados,
            2: self.incluir_final,
            3: self.incluir_inicio,
            4: self.incluir_meio,
            5: self.excluir_primeiro,
            6: self.excluir_ultimo,
            7: self.excluir_meio,
            8: self.excluir_todos,
            0: exit
        }
        while True:
            print('========MENU========\n1. Apresentar dados\n2. Incluir no final\n3. Incluir no início\n4. Incluir no meio\n5. Excluir primeiro\n6. Excluir último\n7. Excluir meio\n8. Excluir todos\n0. Sair\n====================')
            opcao = int(input('Escolha uma opção: '))
            if opcao in OPTIONS:
                OPTIONS[opcao]()
            else:
                print('Opção inválida')

    ## Métodos
    def apresentar_dados(self):
        '''Apresenta os dados da lista'''
        fila_auxiliar = cl.deque()
        if self.__lista:
            while self.__lista:
                print(self.__lista[0])
                fila_auxiliar.append(self.__lista.popleft())
        
            while fila_auxiliar:
                self.__lista.append(fila_auxiliar.popleft())
        else:
            print('Lista vazia')

    def incluir_final(self):
        '''Inclui um valor no final da lista'''
        valor = input('Digite o valor: ')
        if valor:
            try:
                valor = int(valor)
                self.__lista.append(valor)
            except ValueError:
                print(f"Valor '{valor}' é inválido")
                return

    def incluir_inicio(self):
        '''Inclui um valor no início da lista'''
        valor = input('Digite o valor: ')
        if valor:
            try:
                valor = int(valor)
                self.__lista.appendleft(valor)
            except ValueError:
                print(f"Valor '{valor}' é inválido")
                return

    def incluir_meio(self):
        '''Inclui um valor no meio da lista'''
        valor = input('Digite o valor: ')
        chave = input('Digite a chave: ')

        if valor and chave:
            try:
                valor = int(valor)
                chave = int(chave)
                pos = self.__lista.index(chave)
                self.__lista.insert(pos+1, valor)
            except ValueError:
                print('Chave não encontrada')
            except IndexError:
                print('Chave inválida')
            except Exception as e:
                print(f'Erro: {e}')

    def excluir_primeiro(self):
        '''Exclui o primeiro valor da lista'''
        if self.__lista:
            self.__lista.popleft()
        else:
            print('Lista vazia')

    def excluir_ultimo(self):
        '''Exclui o último valor da lista'''
        if self.__lista:
            self.__lista.pop()
        else:
            print('Lista vazia')

    def excluir_meio(self):
        '''Exclui um valor no meio da lista'''
        valor = input('Digite o valor: ')

        if valor:
            try:
                self.__lista.remove(valor)
            except ValueError:
                print('Valor não encontrado')
            
    def excluir_todos(self):
        '''Exclui todos os valores da lista'''
        if self.__lista:
            self.__lista.clear()
        else:
            print('Lista vazia')

if __name__ == "__main__":
    Lista()