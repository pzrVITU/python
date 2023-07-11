#Precedencia de operadores

#1. (n + n)
#2. **
#3. * / // %
#4. + -

conta_1 = 1 + 1 ** 5 + 5 #7    <--- Sem a utilização do parentese, primeiro ele vai realizar a conta 1**5 = 1 e posteriormente vai ficar 1 + 1 + 5
print(conta_1)

conta_1 = (1 + 1) ** (5 + 5) #1024    <- Correta
print(conta_1)
