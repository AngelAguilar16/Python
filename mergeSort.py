def merge(v):
    print("Dividir ",v)
    if len(v)>1:
        mitad = len(v)//2
        mitadIzquierda = v[:mitad]
        mitadDerecha = v[mitad:]

        merge(mitadIzquierda)
        merge(mitadDerecha)

        i=0
        j=0
        k=0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                v[k]=mitadIzquierda[i]
                i=i+1
            else:
                v[k]=mitadDerecha[j]
                j=j+1
            k=k+1

        while i < len(mitadIzquierda):
            v[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            v[k]=mitadDerecha[j]
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