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

def merge(lista_1, lista_2):
    i=0
    j=0
    k=0
    while i < len(lista_1) and j < len(lista_2):
        if lista_1[i] < lista_2[j]:
            lista_3.insert(k,lista_1[i])
            i=i+1
        else:
            lista_3.insert(k,lista_2[j])
            j=j+1
        k=k+1

    while i < len(lista_1):
        lista_3.insert(k,lista_1[i])
        i=i+1
        k=k+1

    while j < len(lista_2):
        lista_3.insert(k,lista_2[j])
        j=j+1
        k=k+1
    print("Mezclar ",lista_3)
    lista_final = sorted(lista_3)
    print(lista_final)


merge(lista_1, lista_2)