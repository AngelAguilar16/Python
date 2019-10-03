def busSecuencial(v, n):
    pos = 0
    encontrado = False
    parar = False
    while pos < len(v) and not encontrado and not parar:
        if v[pos] == n:
            encontrado = True
        else:
            if v[pos] > n:
                parar = True
            else:
                pos = pos+1
    return encontrado,pos
	

v = []

x = int(input("Ingresa el total de espacios en la lista: "))

for i in range(x):
    v.append(int(input("Ingresa el valor " + str(i + 1) + " de la lista: ")))

valor = int(input("Ingresa el numero a buscar en la lista: "))
print("Tu lista es: ", v)
busSecuencial(v, valor)

valores = busSecuencial(v, valor)

if valores[0] == True:
    print("Valor encontrado en la posicion " + str(valores[1] + 1))
else:
    print("Valor no encontrado")
