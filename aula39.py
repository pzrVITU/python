"""
Iterando strings com while

"""

# #      'Indices'
# nome = 'Victor Henrique' # Iteráveis
# #       'Indices negativos'

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# print(nome[11])

# nova_string += '*V*i*c*t*o*r* *H*e*n*r*i*q*u*e*'


nome = input('Digite seu nome: ')
indice = 0
novo_nome = ''


while indice < len(nome):

    letra = nome[indice]
    novo_nome +=f'*{letra}'
    indice += 1

print(novo_nome)