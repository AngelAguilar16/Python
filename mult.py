def mult(a, b):
    if(b == 1):
        return a
    else:
        return a + mult(a, b - 1)

a = int(input("Ingresa el valor de a: "))
b = int(input("ingresa el valor de b: "))
print("La multiplicacion de " + str(a) + " * " + str(b) + " es: " + str(mult(a, b)))