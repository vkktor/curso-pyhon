"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest
lst1 = [1, 2, 3, 4, 5, 6, 7]
lst2 = [1, 2, 3, 4]

lst_soma = [x + y for x, y in zip(lst1, lst2)]
lst_soma_grande = [x + y for x, y in zip_longest(lst1, lst2, fillvalue=0)]
print(lst_soma)
print(lst_soma_grande)

# lst_soma = []
# for i in range(len(lst2)):
#     lst_soma.append(lst1[i] + lst2[i])
# print(lst_soma)

# lst_soma = []
# for i, _ in enumerate(lst2):
#     lst_soma.append(lst1[i] + lst2[i])
# print(lst_soma)
