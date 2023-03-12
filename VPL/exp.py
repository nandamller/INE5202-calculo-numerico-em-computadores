# Fernanda Larissa Müller - 21202109

from math import *
x = 2
exato = exp(x)
erro_permitido = 10**(-6)

print("Valor exato:", exato)

# Implementação simples (calculando com 5 termos da série)
soma = 1

for i in range(1, 5):
    soma += (x**i)/(factorial(i))

print("Valor aproximado com 5 termos da série:", soma)


#Implementação com base no erro permitido
erro = abs(exato - soma)
soma = potencia = termos = fatorial = 1

while erro > erro_permitido:
    potencia *= x
    fatorial *= termos
    soma += potencia / fatorial
    erro = abs(exato - soma)
    termos += 1

print("Valor com base no erro permitido:", soma, "-", termos, "termos foram utilizados.")