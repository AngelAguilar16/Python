def busquedaBinaria(unaLista, item):
	    primero = 0
	    ultimo = len(unaLista)-1
	    encontrado = False
	
	    while primero<=ultimo and not encontrado:
	        puntoMedio = (primero + ultimo)//2
	        if unaLista[puntoMedio] == item:
	            encontrado = True
	        else:
	            if item < unaLista[puntoMedio]:
	                ultimo = puntoMedio-1
	            else:
	                primero = puntoMedio+1
	
	    return encontrado
	
v = []

x = int(input("Ingresa el total de espacios en la lista: "))

for i in range(x):
    v.append(int(input("Ingresa el valor " + str(i + 1) + " de la lista: ")))

valor = int(input("Ingresa el numero a buscar en la lista: "))
print("Tu lista es: ", v)
busquedaBinaria(v, valor)

valores = busquedaBinaria(v,valor)

if valores == True:
    print("Valor encontrado")
else:
    print("Valor no encontrado")