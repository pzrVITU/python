# Introdução sobre f-string (formatação de string)

nome = 'Victor Henrique Fernandes Silva'
altura= 1.750001
peso= 98.34
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso:.2f} quilos e seu IMC é '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)