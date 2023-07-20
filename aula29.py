"""
try/except
try -> tenta executar o código
except -> ocorreu algum erro ao tentar executar

"""

#Exemplo de ValueErro#
print(1234)
print(456)
# int('a')

# Exemplo de conversão de dados
numero = input('Vou dobrar o numero que você digitar: ')

numero_float = float(numero)

dobro = (numero_float * 2)

print(f'O dobro do numero {numero} é {dobro:.2f}')



numero_str = input('Vou dobrar o numero: ')

# Utilizando o método do objeto numero_str exemplo de como tratar uma str com isdigit (checa se o usuario digitou apenas números)

print(numero_str.isdigit()) # Retorna um resultado booleano, ou seja, retorna se é verdadeiro ou falso

# Convertanto o valor da string para float
numero_float1 = float(numero_str)

# Realizando o calculo do dobro.
print(f'O dobro de {numero_str} é {numero_float1*2:.2f}')


# Exemplo de utilização do isdigit

# if numero_str.isdigit():
#     print('Isso é um numero')
# else:
#     print('Isso não é um número')

# O if não evita exceção, já o try evita

# Exemplo de try

try: # Não precisa colocar nenhuma condição dentro do try (Tenta executar o código que vier aqui dentro)
    ... ## Definição da elipsis
    numero = input('Vou dobrar o numero que você digitar: ')

    numero_float = float(numero)

    dobro = (numero_float * 2)

    print(f'O dobro do numero {numero} é {dobro:.2f}')
except: # Se ocorrer algum erro dentro do try, pula imediatamente para o except
    ...('Isso não é um numero')

#Fail Fast = Errar o mais rapido possivel para mandar para except (exceção)
