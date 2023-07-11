"""
Operadores lógicos and (e) or (ou) not (não) and - Todas as condições precisam ser verdadeiras.

Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor são consideradas falsy(que você já viu) 
0 0.0 '' False

Também existe o tipo None que é usado para representar um não valor

"""

entrada=input('[E]ntrar [S]air\n')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e' ) and senha_digitada == senha_permitida: # Sempre que tiver duas ou mais condições seu if pode ficar ambiguo, para solucionar isso pode ser utilizado parenteses 
    print('Entrar')
else: 
    print('Sair')


#Avaliação de curto circuito

print(0 or False or '' or 'abc' or 1)