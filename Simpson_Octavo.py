import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy

def f(x):
    return numpy.exp(x) * numpy.sin(x)

def simpson38(f, a, b):
    m1 = (2 * a + b) / 3
    m2 = (a + 2 * b) / 3
    integral = (b - a) / 8 * (f(a) + 3 * f(m1) + 3 * f(m2) + f(b))
    return integral

a = 0
b = numpy.pi
n = 10
h = (b - a) / n
suma = 0

for i in range(n):
    b = a + h
    area = simpson38(f, a, b)
    suma = suma + area
    a = b


print(suma)
vt = numpy.exp(numpy.pi) / 2 + 1 / 2
errorporcent = abs((vt - suma) / vt) * 100
print('Error % = ',errorporcent)