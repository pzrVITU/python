"""
Aula 3 -> Tipos de dados

Tipo de tipagem = Dinâmica / Forte (Tipagem dinamica -> O Python já sabe oque você está passando para ele)

str -> string -> texto
Strings são textos que estão dentro de aspas
"""

print(1234) # Exemplo, em outras linguagens que não tenha a tipagem dinamica, você deveria dizer qual é o tipo de dado que você está passando, porém, como no Python a tipagem é dinamica, o interpretador já reconhece qual o tipo de dado que você está passando

# Strings pode ser definido por:
# Aspas simple
print('Victor Henrique') 
print('Victor "Henrique"') # Aspas duplas dentro de aspas simples, pode!

# Aspas Duplas
print("Victor 'Henrique'") 
print("Victor 'Henrique'") # Aspas simples dentro de aspas duplas, pode!

# Escape
print('Victor \"Henrique\"') # Caracter de escape será utilizado quando eu quiser que o interpretador não interprete o proximo caracter, ele vai ser utilizado com o "\", conforme o exemplo

# r
print(r'Victor \"Henrique\"') # Usado normalmente para expressões regulares, vai ser trabalhado mais para a frente do curso.
