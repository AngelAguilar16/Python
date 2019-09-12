DISCOS = int(input("Ingrese el numero de discos que quiere en la torre: ")) 

def Espacio():
  return 2

def AnchoDisco(tamano):
  return 2 * tamano + 3

def AnchoTorre(tamano):
  return 2 * tamano + 3

def AlturaTorre(tamano):
  return tamano + 2

def PosicionTorre(tamano, i):
  return i * (AnchoTorre(tamano) + Espacio())

def CentroTorre(tamano, i):
  return AnchoTorre(tamano) // 2 + PosicionTorre(tamano, i)

def AlturaImagen(tamano):
  return AlturaTorre(tamano) + 3

def AnchuraImagen(tamano):
  return AnchoTorre(tamano) * 3 + 2 * Espacio()

def ObtMovimiento(inicio, fin, n_discos):
  if n_discos == 1:
    yield (inicio, fin)
  else:
    midObjetivo = 3 - inicio - fin
    yield from ObtMovimiento (inicio, midObjetivo, n_discos - 1)
    yield (inicio,fin )
    yield from ObtMovimiento(midObjetivo, fin, n_discos - 1)

def HacerMovimiento(mover, discos): 
  inicio, fin = mover
  discos[fin].append(discos[inicio].pop())

TRANSPARENTE = ""

def Art_vacio():
  return lambda x, y: TRANSPARENTE

def crearStringArt(string):
  def resultado(x, y):
    if x == 0 and y >= 0 and y < len(string):
      return string[y]
    else:
      return TRANSPARENTE
  return resultado
  
def TrasladarStringArt(stringArt, i, j): 
  return lambda x, y: stringArt(x - i, y - j)

def TransponerStringArt(stringArt): 
  return lambda x, y: stringArt(y, x)

def stringArtUnion(stringArts): 
  def resultado(x, y):             
    for art in stringArts:
      if art(x, y) != TRANSPARENTE:
        return art(x, y)
    return TRANSPARENTE
  return resultado

def resolverChar(char):  
  return  " " if char == TRANSPARENTE else char

def printStringArt(stringArt, sizeX, sizeY):  
  for i in range(sizeX):                      
    line = "".join([resolverChar(stringArt(i, j)) for j in range(sizeY)])
    print(line) 

#---------------------------------
#A partir de ahora tratamos los elementos que realmente queremos mostrar

def CrearTorreBaseySoporte(tamaño):  # Ésta funcion hace que se despliegue el la base y el  
  Altura = AlturaTorre(tamaño)       # soporte de la torre.
  Anchura = AnchoTorre(tamaño)
  soporte = TransponerStringArt(crearStringArt("|" * Altura))
  soporte = TrasladarStringArt(soporte, 0, Anchura // 2)
  base = crearStringArt("=" * Anchura)
  base = TrasladarStringArt(base, Altura - 1, 0)
  return stringArtUnion([base, soporte])

def crearflecha(inicio, fin):        # Ésta funcion crea un flecha que nos indica  
  izquierda_fin = min([inicio, fin]) #de que torre a que torre estamos moviendo el disco.
  derecha_fin = max([inicio, fin])
  v = crearStringArt("v")
  v = TrasladarStringArt(v, 0, fin)
  fila = crearStringArt("-" * (derecha_fin - izquierda_fin + 1))
  fila = TrasladarStringArt(fila, 0, izquierda_fin)
  return stringArtUnion([v, fila])
   
def crearDisco(tamaño, centro):          # Esta función crea un "StringArt" que va a 
  stoneString = "o" * AnchoDisco(tamaño) # representar un disco de la torre.
  return crearStringArt(stoneString.center(2 * centro + 1))

def crearTorreconDiscos(tamaño, ListaDisco):      # Esta función crea un "String Art" para 
  BaseTorreArt = CrearTorreBaseySoporte(tamaño)   # una torre, incluyendo los discos que 
  DiscoArts = []                                  
  AlturaDisco = tamaño
  center = tamaño + 1
  for stoneSize in ListaDisco:
    DiscoArt = crearDisco(stoneSize, center)
    DiscoArts.append(TrasladarStringArt(DiscoArt, AlturaDisco, 0))
    AlturaDisco -= 1
  return stringArtUnion([BaseTorreArt] + DiscoArts)

def crearImagenTorre(size, ListaDisco, i):     
  posicion = PosicionTorre(size, i)            
  TorreArt = crearTorreconDiscos(size, ListaDisco)
  return TrasladarStringArt(TorreArt, 2, posicion)
 
def crearFlechaPaso(tamaño, SiguientePaso):  
  if SiguientePaso != None:
    inicioIndice, finIndice = SiguientePaso
    inicio = CentroTorre(tamaño, inicioIndice)
    fin = CentroTorre(tamaño, finIndice)
    result = crearflecha(inicio, fin)
  else:
    result = Art_vacio()
  return result

def createFullArt(tamaño, discos, SiguientePaso):   
  flecha = crearFlechaPaso(tamaño, SiguientePaso)   
  TorreArts = [crearImagenTorre(tamaño, discos[i], i) for i in range(3)]
  TorresArt = stringArtUnion(TorreArts)
  return stringArtUnion([flecha, TorresArt]) 

def imprimirpasos(tamaño):
  discos = [list(range(DISCOS))[::-1], [], []]
  Altura_Imagen = AlturaImagen(tamaño)
  Anchura_Imagen = AnchuraImagen(tamaño)
  for mover in ObtMovimiento(0, 2, tamaño):
    print("Mueve el disco de la torre {0} a la {1}".format(*mover))
    printStringArt(createFullArt(tamaño, discos, mover), Altura_Imagen, Anchura_Imagen)
    HacerMovimiento(mover, discos)
  print("¡Y queda listo!, despues de realizar :", 2**DISCOS-1, "movimientos.")
  printStringArt(createFullArt(tamaño, discos, None), Altura_Imagen, Anchura_Imagen)  
  
imprimirpasos(DISCOS)
