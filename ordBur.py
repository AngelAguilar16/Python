
def llenarV():
    v = []
    n = int(input("Valores a ingresar: "))
 
    for i in range(0, n):
        cont = i + 1
        v.append(int(input("Ingrese valor %d : " % cont)))
    return v

def ordBurbuja(lista,tam):
    print("Lista desordenada: ")
    for i in range(0,tam):
        print("[" + str(v[i]) + "]")
    print("")

    numMov = 0
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lista[j] > lista[j+1]):
                numMov = numMov + 1
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k;

    print("Lista ordenada: ")
    for i in range(0,tam):
        print("[" + str(v[i]) + "]")
    print("")
    print("Numero de movimientos: " + str(numMov))
  
print("")
v = llenarV()
ordBurbuja(v,len(v))