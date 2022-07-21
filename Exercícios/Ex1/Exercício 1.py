"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Victor'
idade = 20
altura = float(1.68)
peso = float(72)
ano = 2021
ano_nasc = ano - idade
imc = peso / altura ** 2

print(f"""{nome} tem {idade} anos, {altura} de altura e pesa {peso}.
O IMC de {nome} é {imc:.2f}.
{nome} nasceu em {ano_nasc}.""")
