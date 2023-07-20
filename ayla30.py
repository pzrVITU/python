"""
CONSTANTE = "VARIAVEIS" que não vão mudar
Muitas condições no mesmo if(ruim)
    <-  Contagem de complexidade(ruim)
"""

velocidade = 62 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada


# Para definir uma variavel constante em Python, como a linguagem não tem essa restrição, uma boa prática é utilizar os nomes das variaveis em maiuscula Ex:

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
multar_carro = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1:
    print('Carro acima da velocidade do radar')

if multar_carro and velocidade_carro_passou_radar_1:
    print('Carro multado') 
else:
    print('Carro não foi multado')