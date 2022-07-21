"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor
da função2 executada. Faça a função1 executar duas funções que recebam um
número diferente de argumentos.
"""


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}.'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}.'


executando = mestre(fala_oi, 'Victor')
executando2 = mestre(saudacao, 'Victor', saudacao='Bom dia,')
print(executando)
print(executando2)
