import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy

def f(x):
    return numpy.sqrt(9 - x ** 2)

n = 24
a = -3
b = 3
dx = (b - a) / n
suma = 0

for i in range(n):
    Area = (f(a) + f(a + dx)) * dx / 2
    suma = suma + Area
    a = a + dx


print("El área es aproximadamente: ", suma)
vt = 9*numpy.pi / 2
print("Error: ", abs(vt - suma) / vt * 100)

x = numpy.linspace(a, b, 100)

plt.plot(a, label='a')
plt.plot(dx,label='dx')

plt.xlabel('a')
plt.ylabel('dx')

plt.title("Metodo de Trapecio")

plt.legend()

plt.show()
