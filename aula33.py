'''
Documentação Python: https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis (não pode mudar esse tipo ao decorrer do programa) que vimos : str, int, float, bool

'''

string = 'Victor Henrique'


# string[3] = 'ABC' # Com dados mutáveis essa condição seria lida, trocaraia meu indice 3 por ABC conforme descrito, porém, como é um tipo de dado imutavel essa alteração não é possível. Uma possivel solução seria criar uma nova variavel para adicionar esse valor eX:

outra_variavel = f'{string[:3]}ABC{string[4:]}'

print(f'{outra_variavel}')

print(string.zfill(50)) # Adiciona zeros a esquerda trazendo um total de 50 caracteres conforme informando no valor do método

