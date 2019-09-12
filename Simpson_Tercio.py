import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy

def f(x):
    return numpy.exp(x) * numpy.sin(x)

def simpson13(f, a, b):
    m = (a + b) / 2
    integral = (b - a) / 6 * (f(a) + 4 * f(m) + f(b))
    return integral

a = 0
b = numpy.pi
n = 40
h = (b - a) / n
suma = 0

for i in range(n):
    b = a + h
    area = simpson13(f, a, b)
    suma = suma + area
    a = b

print(suma)
vt = numpy.exp(numpy.pi) / 2 + 1 / 2
errorporcent = abs((vt - suma) / vt) * 100
print('Error % = ',errorporcent)