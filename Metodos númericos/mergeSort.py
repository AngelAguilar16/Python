def merge(v):
    print("Dividir ",v)
    if len(v)>1:
        mitad = len(v)//2
        Izquierda = v[:mitad]
        Derecha = v[mitad:]
        merge(Izquierda)
        merge(Derecha)
        i=0
        j=0
        k=0
        while i < len(Izquierda) and j < len(Derecha):
            if Izquierda[i] < Derecha[j]:
                v[k]=Izquierda[i]
                i=i+1
            else:
                v[k]=Derecha[j]
                j=j+1
            k=k+1

        while i < len(Izquierda):
            v[k]=Izquierda[i]
            i=i+1
            k=k+1

        while j < len(Derecha):
            v[k]=Derecha[j]
            j=j+1
            k=k+1
    print("Mezclar ",v)

    
v = []
n = int(input("Cuantos valores deseas en la lista: "))
for i in range(n):
    dato = int(input("Valor " + str(i + 1) + ": "))
    v.append(dato)

merge(v)
print(v)