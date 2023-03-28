# Fernanda Larissa Müller - 21202109

from math import cos, exp, sin

def f(n):
    return exp(n) - (2 * cos(n))

def f_der(n):
    return exp(n) + (2 * sin(n))

# intervalo dado
a = 0; b = 2

ciclos = 0
x0 = 0
erro = 10**-10

# valores iniciais
fx0 = f(x0)

while abs(fx0) > erro:
    ciclos += 1
    xk = x0 - (f(x0) / f_der(x0))

    x0 = xk
    fx0 = f(x0)

print("Operação de Método de Newton finalizada!")
print("Ciclos: %d" %ciclos)
print('x0 (raiz): %.16f' %x0)
print('f(x0): %.16f' %fx0)