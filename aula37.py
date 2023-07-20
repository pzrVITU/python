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

while contador < 100:
    contador += 2

    if contador == 6:
        print('Não vou mostrar o 6')
        continue
    
    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o' ,contador)
        continue

    print(f'{contador}')
    
    if contador == 80:
        break # Termina o laço