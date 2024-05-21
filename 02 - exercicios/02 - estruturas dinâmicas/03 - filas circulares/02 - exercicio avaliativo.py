import sys, random

class no_fila:
    def __init__(self):
        self.__nome = None
        self.__maos = 2
        self.__prox = None

    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome
    def getprox(self):
        return self.__prox
    def setprox(self, prox):
        self.__prox = prox
    def getmaos(self):
        return self.__maos
    def setmaos(self, maos):
        self.__maos = maos
    def submao(self):
        if self.__maos > 0:
            self.__maos -= 1

class Fila:
    def __init__(self):
        self.__fim = None
        self.__cancao = "lá-vem-a-car-ro-ci-nha-de-pi-co-le-que-sa-bor-vo-ce-quer"

    def __del__(self):
        self.__fim = None
        
    def contar_silabas(self):
        num_silabas = self.__cancao.count("-") + 1
        return num_silabas

    def push(self):
        temp_no = no_fila()
        if temp_no:
            temp_no.setnome(input("Entre com um nome: "))
            if self.__fim:
                temp_no.setprox(self.__fim.getprox())
                self.__fim.setprox(temp_no)
            else:
                temp_no.setprox(temp_no)
            self.__fim = temp_no
        Fila.printall(self)

    def pop(self, no):
        if no == self.__fim:
            temp_no = self.__fim
            if temp_no.getprox() == temp_no:
                self.__fim = None
            else:
                temp_no = self.__fim.getprox()
                while temp_no.getprox() != self.__fim:
                    temp_no = temp_no.getprox()
                temp_no.setprox(self.__fim.getprox())
                self.__fim = temp_no
        else:
            temp_no = self.__fim.getprox()
            while temp_no.getprox() != no:
                temp_no = temp_no.getprox()
            temp_no.setprox(no.getprox())
        del no

    def printall(self):
        if not self.__fim:
            print("Fila vazia...")
            return
        temp_no = self.__fim.getprox()
        saida = "Fila:\n"
        while True:
            saida += temp_no.getnome() + " - " + str(temp_no.getmaos()) + " maos\n"
            temp_no = temp_no.getprox()
            if temp_no is self.__fim.getprox():
                break
        print(saida)

    def verificar_vencedor(self):
        temp_no = self.__fim.getprox()
        if temp_no.getprox() == temp_no:
            return True
        return False

    def main(self):
        a = self.contar_silabas()
        temp_no = self.__fim.getprox()
        for i in range(a-1):
            temp_no = temp_no.getprox()
        print("\nNome sorteado: ", temp_no.getnome())
        numero = random.randint(1, 6)
        print("Número sorteado: ", numero)
        for j in range(numero):
            temp_no = temp_no.getprox()
        print("Nome que perdeu a mão: ", temp_no.getnome())
        temp_no.submao()
        self.printall()
        if temp_no.getmaos() == 0:
            print("Jogador sem mãos: ", temp_no.getnome())
            self.pop(temp_no)
            
        if self.verificar_vencedor():
            print("Vencedor: ", temp_no.getnome())
            return

f = Fila()
while True:
    op = int(input("\n1 - Inserir participante\n2 - Iniciar\n"))
    if op == 1:
        f.push()
    elif op == 2:
        f.main()
    else:
        del f
        sys.exit()