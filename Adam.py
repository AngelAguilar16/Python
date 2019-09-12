# YiP = Yi + h/24 (55fi - 59fi-1 + 37fi-2 - 9fi-3)
# YiC = Yi + h/24 (9fi+1 + 19fi - 5fi-1 + fi-2)
# f(x, y) = 2y - 2x - 1

h = 0
x = 7
xi = 0
listaDatosX = [0 for i in range(x + 1)]
listaDatosYiP = [0 for i in range(x + 1)]
listaDatosFiP = [0 for i in range(x + 1)]
listaDatosYiC = [0 for i in range(x + 1)]
listaDatosFiC = [0 for i in range(x + 1)]

def f(x, y):
    res = (2 * y) - (2 * x) - 1
    return res

def yP(i):
    res = listaDatosYiC[i] + (h / 24) * ((55 * listaDatosFiC[i]) - (59 * listaDatosFiC[i]) + (37 * listaDatosFiC[i]) - (9 * listaDatosFiC[i])) 
    return res

def yC(i):
    res = listaDatosYiC[i] + (h / 24) * ((9 * listaDatosFiP[i]) + (19 * listaDatosFiC[i]) - (5 * listaDatosFiC[i]) + (listaDatosFiC[i])) 
    return res


def main():
    listaDatosYiC.append(input("y(0) = "))
    listaDatosYiC.append(input("y(1) = "))
    listaDatosYiC.append(input("y(2) = "))
    listaDatosYiC.append(input("y(3) = "))
    print("|x|\t|y|\n")
    for i in range(j+1):
        listaDatosX.append(str(x)) 
        x += h
        listaDatosYiP[i] = yP(i-1),
        listaDatosFiP[i]= f(listaDatosX[i], listaDatosYiP[i]),10
        listaDatosYiC[i]= yC(i-1)
        listaDatosFiC[i]= f(listaDatosX[i], listaDatosYiC[i])
        print("|" + listaDatosX[i] + "|\t|" + listaDatosYiC[i] + "|")

main()