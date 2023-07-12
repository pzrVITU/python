"""
d - int
f - float

.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= -> Força o número a aparecer depois do 0
Sinal - + ou +
Ex.: 0>-100, .1f
Conversion flags - !r !s !a  ->!r = chama o método __repr__, !s = chama o método __str__, !a chama o método ____
"""

variavel = 'ABCD'
print(f'{variavel}')
print(f'{variavel:0^10}') # Inserindo o caractere definido após os dois, nesse caso é o "0", e o operador "^" na formatação da string, insere o valor definido no entre a string
print(f'{variavel:0>10}') # Inserindo o caractere definido após os dois, nesse caso é o "0", e o operador ">" na formatação da string, insere o valor definido à esquerda da string
print(f'{variavel:0<10}') # Inserindo o caractere definido após os dois, nesse caso é o "0", e o operador "<" na formatação da string, insere o valor definido à direita da string

print(f'{100.487979546484684:.1f}') # Definindo quantas casas decimais vai aparecer em um numero float
print(f'{100.487979546484684:,.2f}') # Definindo quantas casas decimais vai aparecer em um numero float, e a virgula que vem antes, define a separação de numeros em mil
print(f'{100.487979546484684:+.2f}') # Definindo quantas casas decimais vai aparecer em um numero float, e a virgula que vem antes, define a separação de numeros em mil, o "+" indica para o Python mostrar o sinal do numero, se negativo, vai mostrar negativo e se positivo, vai retornar o valor positivo

print(f'O hexadecimal de 1500 {1500:04x}') # Mostrando um número em forma hexadecimal

print(f'{variavel!r}') #Conversion flags