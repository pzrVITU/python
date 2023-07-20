"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    if numero_int%2 == 0:
        print('O número é par')
    else:
        print('O número é impar')
except:
    print(' Você não digitou um número inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digete sua hora(s) atual: ')
minutos = input('Digite seu(s) minuto(s) atual: ')

try:
    int_hora = int(hora)
    int_minutos = int(minutos)

    bom_dia = (int_hora >=0 and int_hora <=11)
    boa_tarde = (int_hora >=12 and int_hora <=17)
    boa_noite = (int_hora >=18 and int_hora <=23)

    if int_hora > 23 or int_minutos > 59:
        print('Horas ou minutos com valor acima do esperado')
    else:
        if bom_dia:
            print(f'Bom dia, seu horario atual é {int_hora:0>2} : {int_minutos:0>2}')
        elif boa_tarde:
            print(f'Boa tarde, seu horario atual é {int_hora:0>2} : {int_minutos:0>2}')
        elif boa_noite:
            print(f'Boa noite, seu horario atual é {int_hora:0>2} : {int_minutos:0>2}')     

except:

    print('Digite um numero inteiro em horas e em minutos')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

nome = input('Digite seu primeiro nome: ')
contador = len(nome)

if contador <= 4 :
    print('Seu nome é curto')
elif contador > 4 and contador < 7 :
    print('Seu nome é normal')
else:
    print('Seu nome é muito longo')
