"""
for/while
contador
0   10
1   9
2   8
3   7
4   6
5   5
6   4
7   3
8   2
"""
from time import sleep
# contador_1 = list(range(0, 11))
# contador_2 = list(range(10, -1, -1))

# for valor in range(0, 11):
#     sleep(1)
#     print(contador_1[valor], contador_2[valor])

for p, r in enumerate(range(10, -1, -1)):
    sleep(1)
    print(p, r)
