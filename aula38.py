'''
Repetição while (enquanto)
Executa uma ação enquanto uma condição for verdadeira 
Loop infinito, quando um código não tem fim
Unreacheble -> Inalcançavel, todo código após um loop infinito

While dentro de while

'''

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1 
    while coluna <= qtd_colunas:
          print(f'{linha=}{coluna=}')
          coluna += 1
    linha += 1

print('Acabou')