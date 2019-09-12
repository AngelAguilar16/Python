# Y Predictora
#   yi+1 = yi-3 + 4h/3 * (2fi-2 -fi-1 + 2fi) 

#Y Correctora
#   yi+1 = yi-1 + h/3 * (fi-1 + 4fi + fi+1)
 
#Funcion de x
#   x + y -1


h = 0.1
x = 0
y = 0
fiC = 0
fiP = 0
yiC = 0
yiP = 0

# datafic = [[1],[1.0052],[1.0214],[1.0499],[0],[0]]

datafic = [["fiC"],[0.5],[0.612638452],[0.757480116],[0.949242786],[1.211972484],[1.586749828],[2.149838248],[3.054124498]]
datafip = [["fiP"],[0],[0],[0],[0],[1.211386113],[1.585322779],[2.146327402],[3.044240619]]
datayic = [["yiC"],[1],[1.055468971],[1.123545506],[1.208459215],[1.315790085],[1.454533065],[1.634297961],[1.895544155]]
datayip = [["yiP"],[0],[0],[0],[0],[1.31550431],[1.453874263],[1.637958868],[1.892479452]]
datai = [["i"],[0],[1],[2],[3],[4],[5],[6],[7]]
datax = [["X"],[0],[0.1],[0.2],[0.3],[0.4],[0.5],[0.6],[0.7]] 

def f(x, y):
    return x + y - 1

def fiC(x, y):
    pass

def fiP(x,y):
    pass

def yiC(yi_1, h, fi_1, fi, fi_2):
    return yi_1 + h / 3 * (fi_1 + 4*fi + fi_2)

def yiP(yi_3, h, fi_2, fi_1, fi):
    return yi_3 + 4*h/3 * (2*fi_2 - fi_1 + 2*fi)

for i in range(9):
    print(str(datai[i]) + "\t" + str(datax[i]) + "\t" + str(datayip[i]) + "\t" + str(datafip[i]) + "\t" + str(datayic[i]) + "\t" + str(datafic[i]))
