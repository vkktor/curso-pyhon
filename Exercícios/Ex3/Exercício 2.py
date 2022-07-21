"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre
eles.
"""


def numeros(n1, n2, n3):
    return n1 + n2 + n3


n1 = int(input('Insira um número: '))
n2 = int(input('Insira um número: '))
n3 = int(input('Insira um número: '))

somar = numeros(n1, n2, n3)
print(somar)
