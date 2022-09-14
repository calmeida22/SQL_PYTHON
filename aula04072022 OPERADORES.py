nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:_^20}!'.format(nome))  # alinhamento centralizado, 20 é qtd caracteres
print('Prazer em te conhecer {:_<20}!'.format(nome))  # alinhamento a esquerda
print('Prazer em te conhecer {:_>20}!'.format(nome))  # alinhamento a direita

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print('Divisão inteira é {} e potência é {}'.format(di, e))
