"""
Flag(Bandeira) - Marca um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

# Identidade é o ponteiro em Python

v1='1'
v2=int('1')
print(id(v1))
print(id(v2))

condicao = False

if condicao:
    passou_no_if = True # Podemos declarar a variavel dentro de um bloco da comandos, no exemplo, dentro do if, porém não é uma boa prática fazer isso, o ideal é o ciclo contrário, declarara a variavel fora do if e posteriormente utiliza-la dentro do if
    print('Faça algo')
else:
    passou_no_if = None
    print('Não faça algo')

print(passou_no_if) # Nesse exemplo, caso a condição seja falsa a variavel "passou_no_if" não foi criada, e como estamos chamando ela fora do if, irá apresentar problemas no momento de chamar essa variavel

# Para corrigir esse problema, deve ser declarada a variavel fora do if, da seguinte forma: 

passou_no_if1 = None # Definindo a variavel dessa forma, ela tem o valor de None atribuido a ela e so muda de valor, caso entre na condição True

if condicao:
    passou_no_if1 = True # Mudando o valor da variavel dentro do if
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if1, passou_no_if1 is None) # passou _no_if1 -> informa o valor dessa variavel, o passou_no_if1 "é" none ou não, irá retornar uma saida em booleano
print(passou_no_if1, passou_no_if1 is not None)
