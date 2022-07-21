# 168 995 350 09
cpf = input('Digite os números do CPF: ')

if cpf.isnumeric():
    if len(cpf) != 11:
        print('Valores Inválidos. Insira os 11 digitos do CPF.')

    else:
        cpf_novo = cpf[:-2]
        reverso = 10
        total = 0

        for index in range(19):
            if index > 8:
                index -= 9

            total += int(cpf_novo[index]) * reverso

            reverso -= 1
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                cpf_novo += str(d)

                sequencia = cpf_novo == (cpf_novo[0]) * len(cpf)

                if cpf == cpf_novo and not sequencia:
                    print('CPF valido.')

                else:
                    print('CPF inválido.')

else:
    print('Valores Inválidos. Insira apenas números inteiros.')
