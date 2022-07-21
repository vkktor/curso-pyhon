"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def soma(num, perc):
    dec = perc / 100
    perc = 1 + dec
    return num * perc


somar = soma(50, 10)
print(f'{somar:.2f}')
