'''
Repetição while (enquanto)
Executa uma ação enquanto uma condição for verdadeira 
Loop infinito, quando um código não tem fim
Unreacheble -> Inalcançavel, todo código após um loop infinito

'''

while False:
    print('Não vai entrar no while, é unreacheble')

print('Acabou')

contador = 0

while contador < 10:
    contador = contador + 1
    print(f'{contador}')