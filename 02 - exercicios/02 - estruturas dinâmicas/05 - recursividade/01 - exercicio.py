## 01) Construa um programa para calcular a soma sucessiva de um inteiro positivo qualquer, mediante uma função recursiva.
import sys

def soma_sucessiva(n):
    if n != 1:
        return n + soma_sucessiva(n-1)
    else:
        return 1
        
def main():
    n = int(input('Digite um número inteiro positivo: '))
    if n > 0:
        print(f'A soma sucessiva de {n} é {soma_sucessiva(n)}')
        sys.exit(0)
    else:
        main()
        
if __name__ == '__main__':
    main()