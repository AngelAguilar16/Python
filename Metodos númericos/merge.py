n1 = int(input("Cuantos numeros desea en la lista 1: "))
n2 = int(input("Cuantos numeros desea en la lista 2: "))

lista_1 = []
lista_2 = []
lista_3 = []

for i in range(n1):
    dato_1 = int(input("Ingresa el valor " + str(i + 1) + " de la lista 1: "))
    lista_1.append(dato_1)


for i in range(n2):
    dato_2 = int(input("Ingresa el valor " + str(i + 1) + " de la lista 2: "))
    lista_2.append(dato_2)

lista_3 = sorted(sorted(lista_1) + sorted(lista_2))
print(lista_3)