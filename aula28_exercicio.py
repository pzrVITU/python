"""
Exercício

Peça para o usuário digitar seu nome
Peça para o usuário digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém ou nao espaçoes
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
exiba: "Desculpe, você deixou campos varios"
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

#int_idade = int(idade)

if nome != '' and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'O nome contém espaço?',' ' in nome)
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos varios')