## 03) Faça um programa para a multiplicação de números naturais. O produto
## a * b, em que a e b são inteiros positivos, pode ser definido como a somado a si
## mesmo b vezes. Essa é uma definição iterativa. Por exemplo, para avaliar 6*3,
## avalia-se primeiro 6*2 e depois soma-se 6. Para avaliar 6*2, avalia-se primeiro
## 6*1 e soma-se 6. Mas 6*1 é igual a 6. Sendo assim: 6*3=6*2+6=6*1+6+6=6+6+6=18.

def multiplicacao(a, b):
    if b == 1:
        return a
    else:
        return a + multiplicacao(a, b-1)
    
def main():
    a = int(input('Digite um número inteiro positivo: '))
    b = int(input('Digite outro número inteiro positivo: '))
    if a > 0 and b > 0:
        print(f'{a} * {b} = {multiplicacao(a, b)}')
    else:
        main()

if __name__ == '__main__':
    main()