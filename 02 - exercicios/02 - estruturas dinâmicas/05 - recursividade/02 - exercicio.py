## 02) Sabe-se que a sequência de Fibonacci é a sequência de inteiros:
## 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... Se permitirmos que fib(0) = 0, fib(l) = 1,
## fib(2) = 1, fib(6) = 8, e assim por diante, então construa uma função recursiva
## para determinar o valor Fibonacci.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def main():
    n = int(input('Digite um número inteiro: '))
    print(f'O valor de Fibonacci de {n} é {fib(n)}')
    
if __name__ == '__main__':
    main()