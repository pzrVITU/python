"""
Operadores lógicos and (e) or (ou) not (não) and - Todas as condições precisam ser verdadeiras.

Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor são consideradas falsy(que você já viu) 
0 0.0 '' False

Também existe o tipo None que é usado para representar um não valor

"""

#------------------------------------Exemplo 1 
# entrada=input('[E]ntrar [S]air\n')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else: 
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)

# Avaliação de curto circuito para de ler o codigo no momento que a condição não é mais verdadeira
print(True and 0 and True)

