# IMPORTAR UM CONJUNTO DE FUNÇÕES (precisa de math.sqrt)
# import math
# num = int(input('Digite um número '))
# raiz = math.sqrt(num)
# print('A raiz de {} é igual a {}'.format(num, raiz))

# IMPORTAR UMA FUNÇÃO ESPECÍFICA (não precisa de math.sqrt
# from math import sqrt

# num = int(input('Digite um número '))
# # raiz = sqrt(num)
# # print('A raiz de {} é igual a {}'.format(num, raiz))
#
# import random
#
# num = random.randint(1, 10)
# print(num)

# import emoji

# TRATAR FRASE OU PARTE DE FRASE COMO VETOR
print('')  # Pular linha
frase = 'Curso em Vídeo Python'
print(frase)  # MOSTRA A FRASE
print(frase[9:21:2])  # MOSTRA DO CARACTER 9 ATE 21 EXCLUINDO 2 EM 2 LETRA
print(frase[:5])  # MOSTRA ANTERIOR ATÉ CARACTER 5
print(frase[15:])  # MOSTRA ATÉ FINAL A PARTIR DO CARACTER 15
print(frase[9::3])
print(frase.count('o'))  # CONTA QUANTAS LES 'O' TEM NA FRASE
print(frase.count('o', 0, 13))  # CONTA QUANTAS LES 'O' TEM NA FRASE NO INTERVALO DE 0 A 13
print(len(frase))  # CONTA QUANTOS CARACTERES TEM A STRING
print(frase.find('Vídeo'))  # PROCURA UM PALAVRA/LETRA ESPECÍFICA
print(frase.replace('Python', 'Android'))  # ALTERA A PALAVRA'PYTHON' PARA 'ANDROID'
print(frase.upper())  # TODAS A LETRAS MAIÚSCULAS
print(frase.lower())  # TODAS A LETRAS MINÚSCULAS
print(frase.capitalize())  # PRIMEIRA LETRA DA FRASE MAIÚSCULA
print(frase.title())  # PRIMEIRA LETRA DE CADA PALAVRA MAIÚSCULA

print('')
frase2 = '   Aprenda Python   '
print(frase2)
print(frase2.strip())  # EXCLUI OS ESPAÇOS SOBRANDO NO INÍCIO E FIM DA FRASE
print(frase2.lstrip())  # EXCLUI OS ESPAÇOS SOBRANDO A ESQUERDA
print(frase2.rstrip())  # EXCLUI OS ESPAÇOS SOBRANDO A DIREITA
print(frase2.split())  # SEPARA CADA ELEMENTO PELO ESPAÇO (é uma lista que seria a evolução do vetor)
print(frase.split())  # SEPARA CADA ELEMENTO PELO ESPAÇO (é uma lista)
