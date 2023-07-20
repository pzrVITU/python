'''
Repetição while (enquanto)
Executa uma ação enquanto uma condição for verdadeira 
Loop infinito, quando um código não tem fim
Unreacheble -> Inalcançavel, todo código após um loop infinito


'''

condicao = True

while condicao:
    nome = input('Qual seu nome? ')
    print (f'Seu nome é {nome}')

    if nome == 'sair':
        break # Dentro de um laço, busca o laço mais proximo dela e interrompe a ação
