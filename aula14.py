# Outra forma de formatar strings

a = 'AAAAA'
b = 'BBBBB'
c = 1.1

#Primeira forma de usar o método .format, com chaves vazias, nesse caso você deve seguir rigorosamente a posição de cada variavel dentro do método format. Nessa forma de utilizar o format, não pode haver chaves a mais do que variaveis dentro do método.
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

print(formato)

#Segunda forma de usar o método .format, com chaves informando a posição da variavel dentro do método format. Nesse modo você pode colocar chaves a mais do que você tem de variaveis dentro do metodo format, porém deve referencia a posição em cada chamada.
a = "AAAAA"
b = "BBBBB"
c = 1.1
formato = 'a={0} b={1} c={2:.2f} b={1}'
print(formato.format(a, b, c))

#Terceira forma de usar o método .format, com parametro nomeados, é quando damos um nome para as variaveis dentro do método format, obs: tudo que vem apos o primeiro parametro nomeado, deve ser nomeado.

a = "AAAAA"
b = "BBBBB"
c = 1.1
formato = 'a={0} b={nome1} c={nome2:.2f} b={nome1}' #Nesse exemplo, usamos uma junção do segundo caso, com o terceiro caso. Dentro da chamada a variavel a indica a variavel da posição 0 dentro do método, enquanto a variável b e c são nomeadas e são chamadas pelos seus respectivos nomes.
print(formato.format(a, nome1=b, nome2=c))