"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se estre número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num1 = input('Digite um número inteiro: ')

if num1.isdigit():
    num2 = int(num1)
    if num2 % 2 == 0:
        print(f'{num2} é um número par.')
    else:
        print(f'{num2} é um número ímpar.')
else:
    print(f'{num1} não é um número inteiro.')
