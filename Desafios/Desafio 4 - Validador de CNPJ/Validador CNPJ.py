import re


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def executa(cnpj):
    cnpj_novo = segundo_digito(primeiro_digito(cnpj))
    return cnpj_novo


def primeiro_digito(cnpj):
    try:
        cnpj_novo = cnpj[:-2]
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


def sequencia(cnpj):
    sequencia = cnpj_novo == (cnpj_novo[0]) * len(cnpj)
    return sequencia


cnpj = input('Digite os números do CNPJ: ')
cnpj = remover_caracteres(cnpj)

if len(cnpj) != 14:
    print('Valores Inválidos.')

else:
    try:
        cnpj_novo = executa(cnpj)
        repete = sequencia(cnpj)

        if cnpj == cnpj_novo and not repete:
            print('CNPJ Válido.')
        else:
            print('CNPJ Inválido.')

    except (IndexError, IndentationError, TypeError):
        print('Valores Inválidos.')
