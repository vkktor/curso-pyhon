import random
import re


def primeiro_digito(cnpj):
    try:
        cnpj_novo = cnpj
        reverso = 5
        total = 0
        for index in range(13):
            if reverso < 2:
                reverso = 9

            total += int(cnpj_novo[index]) * reverso
            reverso -= 1

            if index == 11:
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                cnpj_novo += str(d)
                return cnpj_novo
    except (IndexError, TypeError):
        pass


def segundo_digito(cnpj_novo):
    try:
        cnpj_novo_2 = cnpj_novo
        reverso = 6
        total = 0
        for index in range(14):
            if reverso < 2:
                reverso = 9

            total += int(cnpj_novo_2[index]) * reverso
            reverso -= 1

            if index == 12:
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                cnpj_novo_2 += str(d)
                return cnpj_novo_2
    except (IndexError, TypeError):
        return print('Valores Inválidos.')


def gera():
    dg1 = random.randint(0, 9)
    dg2 = random.randint(0, 9)
    bloco1 = random.randint(100, 999)
    bloco2 = random.randint(100, 999)
    bloco3 = '0001'

    inicio_cnpj = f'{dg1}{dg2}{bloco1}{bloco2}{bloco3}'
    novo_cnpj = segundo_digito(primeiro_digito(inicio_cnpj))
    novo_cnpj = formata(novo_cnpj)

    return novo_cnpj


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def formata(cnpj):
    cnpj = remover_caracteres(cnpj)
    formato = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'

    return formato


print(gera())
