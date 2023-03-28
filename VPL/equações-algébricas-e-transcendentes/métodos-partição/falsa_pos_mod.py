# Fernanda Larissa Müller - 21202109

from math import cos, exp

def f(n):
    return exp(n) - (2 * cos(n))  

# intervalo dado
a = 0; b = 2

ciclos = 0
xm = 0
erro = 10**-10

# valores iniciais
fa = f(a); fb = f(b); fxm = 1

if fa * fb > 0:
    print("O intevalo dado não garante uma raiz.")
else:
    while abs(fxm) > erro:
        ciclos += 1
        xm = a - ((fa*(b-a)) / (fb -fa))
        fxm = f(xm)

        if fa*fxm > 0:
            pb = fa / (fa + fxm)
            fb *= pb
            a = xm
            fa = f(a)

        else:
            pa = fb / (fb + fxm)
            fa *= pa
            b = xm
            fb = f(b)

print("Operação de Falsa Posição Modificada finalizada!")
print("Ciclos: %d" %ciclos)
print('xm (raiz): %.16f' %xm)
print('f(xm): %.16f' %fxm)
