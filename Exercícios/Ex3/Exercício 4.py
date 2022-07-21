"""
4 - Fizz Buzz - Se o parâmetro da função for divisivel por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro
da função for divisível por 5 e por 2, retorne FizzBuzz, caso contrário,
retorne o número enviado.
"""


def FizzBuzz(par):
    if par % 3 == 0 and par % 5 == 0:
        return 'FizzBuzz'
    elif par % 3 == 0:
        return 'Fizz'
    elif par % 5 == 0:
        return 'Buzz'
    else:
        return par


divisao = FizzBuzz(15)
print(divisao)
