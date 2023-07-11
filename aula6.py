# Conversão de tipos, coerção, type convertion, typecasting, coercion é o ato de converter um tipo de dados em outro.
# Tipos imutaveis e primitivos -> Tipos que trabalhando antes, são tipos imutaveis, pois quando criamos eles não é permitido mudar seu tipo.

# str, int, float, bool
print('--Exemplo 1--')
print (1 + 1) # Numeros com o operador de "+" o Python retorna a soma desses números.
print ('a' + 'b') # str com o operador de "+" o Python concatena as duas strings.
#print (1 + 'a')  No caso de utilizar o operador logico de + para somar/concatenar dois tipos de dados diferentes o Pyton apresenta um erro informando que não é possivel utilizar o operador logico diretamento convertendo os dados.
# Existe algumas funções para converter um tipo de dado em outro.
print('-------------', end='\n\n\n')


print('--Exemplo 2--')
print(int('1'), type (int('1')))
print(int('1') + 1) # Para realizar a coerção, eu tenho que definir o tipo de dado que estou utilizando para o Python saber qual o tipo ele deve converter
print('-------------', end='\n\n\n')


print('--Exemplo 3--')
print (float('1') + 1) # Alguns tipos de dados pode ser somados entre sí, como é o caso do float e int, porém, nesse caso o resultado sempre será em float, conforme o exemplo
print (type(float('1') + 1)) # Função/Classe para saber qual o tipo de dado do exemplo acima

print('-------------', end='\n\n\n')

print('--Exemplo 4--')

print(bool('')) # str vazia, retorna um valor falso
print(bool(' ')) # str preenchida, retorna um valor verdadeiro, mesmo que o valor preenchido seja um espaço

print('-------------', end='\n\n\n')

print('--Exemplo 5--')

print(str('11') + 'b') # Nesse exemplo estamos convertendo o numero 11, que poderia ser um inteiro ou um float, para string. 

print('-------------')

