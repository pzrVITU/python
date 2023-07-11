# função input é para o usuário preencher dados, somente vai funcionar no terminal, o output do Python é somente leitura
# input("Qual o seu nome? ")

# exemplo

# nome = input('Qual o seu nome? ')
# print (f'O seu nome é {nome=}') # O igual seria para ele trazer o nome da variavel antes, e depois, o valor que essa variavel armazena

# numero_1 = input('Digite um numero ')
# numero_2 = input('Digite um numero ')

# print(f'A soma dos numeros é: {numero_1 + numero_2}') # input é somente para str, ou seja, quando usamos o sinal de "+" realizamos uma concatenação

# numero_3 = int(input('Digite um numero ')) #Um dos métodos de realizar contas com o input, é realizando a converção dos dados, dentro do momento de solicitar ao usuário os dados. Porém se o usuário informar o tipo de dado errado, nosso programa ele morre, sem saber qual foi o dado que o usuário digitou.
# numero_4 = int(input('Digite um numero '))

# print(f'A soma dos numeros é: {numero_3 + numero_4}')

# O ideal é criar uma variavel para converter e checar o tipo de dado que meu usuário digitou

numero_5 = input('Digite um numero ')
numero_6 = input('Digite um numero ')

int_numero_5 = int(numero_5)
int_numero_6 = int(numero_5)

print(f'A soma dos números são {int_numero_5 + int_numero_6}')