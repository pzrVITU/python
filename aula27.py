"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento[i"nicio":f"im":p"asso" = incremento][::]
Obs.: a função len retorna a qtd de caracteres da str
"""

# fatiramento, pega uma fatia de sua string

variavel = 'Olá mundo'
print(variavel[7]) # Exemplo de buscar um caracter de acordo com sua posição na string

print(variavel[4:]) # Exemplo de fatiamento da string, definimos o inicio de onde vai começar a pegar os caracteres da str, mas não colocando o final, ele entende que deve pegar até o final, não preciso definir se for para pegar todo o "resto" da str

print(variavel[4:7]) # Exemplo de fatiamento da string, definimos o inicio de onde vai começar a pegar os caracteres da str e definindo o final, ele pega até uma posição antes do valor que defini, no caso o meu caracter que está na posição 7 é o d, porém , como a maioria das coisas em Python, o ultimo elemento da posição normalmente não é considerado, e ele acaba pegando até o "n"

print(variavel[:7]) # Exemplo de fatiamento da string, omitindo o inicio, ele saber que terá que começar da posição 0 e ir até o final definido no fatiamento

print(variavel[:7]) # Exemplo de fatiamento da string, omitindo o inicio, ele saber que terá que começar da posição 0 e ir até o final definido no fatiamento

print(variavel[-5: -1]) # Exemplo de fatiamento de string utilizando outro método de validação dos caracteres da string "números negativos"

# OBS: Prestar atenção nos espaços, um espaço, é um caracter
# função len retorna a quantidade de caracteres de uma string, Exemplo:

print(len(variavel[2:7])) # Exemplo da função len, contando quantos caracteres tem na fatia 2:7

print(variavel[0:len(variavel):2]) # Exemplo de uma incrementação de 2 em 2

print(variavel[-1:-10:-1]) # Exemplo de uma inversão de string com a incrementação negativa
print(variavel[::-1]) # O memso exemplo de uma inversão de string com a incrementação negativa

