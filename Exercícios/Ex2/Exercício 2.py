"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite um horário (0-23): ')

if hora.isdigit():
    hora_int = int(hora)

    if hora_int < 0 or hora_int > 23:
        print('O horário deve estar entre 0 e 23.')

    else:
        if hora_int <= 11:
            print(f'São {hora_int}h, bom dia!')

        elif hora_int <= 17:
            print(f'São {hora_int}h, boa tarde!')

        else:
            print(f'São {hora_int}h, boa noite!')

else:
    print(f'{hora} não está dentro do padrão pedido.')
