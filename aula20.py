# Exercicio operadores de comparação

primeiro_valor = input('Digite um valo: ')
segundo_valor = input('Digite um valo: ')

# int_primeiro_valor = int(primeiro_valor)
# int_segundo_valor = int(segundo_valor)


if primeiro_valor > segundo_valor:
    print(f'O primeiro valor digitado "{primeiro_valor}" é maior que o segundo valor digitado"{segundo_valor}"')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor digitado "{segundo_valor}" é maior que o primeiro valor digitado "{primeiro_valor}"')
else:
    print(f'Os numeros digitados : {primeiro_valor} e {segundo_valor}, são iguais')