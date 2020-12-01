# Función para transformar los datos de la matriz en enteros
def convertir_matriz_int(n_filas, n_columnas, matriz):
    for i in range(0, n_filas-1):
        for j in range(0, n_columnas-1):
            matriz[i][j] = int(matriz[i][j])
    return matriz  
# Función para obtener cantidad de puestos, lista de tamaños de locales y matriz con asistentes a los locales
def asignacion_datos(nombre_archivo):
    archivo = open('data/' + nombre_archivo, "r")

    cont = 0
    matriz = []

    for linea in archivo:
        cont += 1
        
        if cont == 1:
            n_puestos = int(linea)
        elif cont == 2:
            l_tamano = linea.rstrip().split(",")
            
        else:
             matriz.append(linea.rstrip().split(","))
             
    l_tamano = convertir_matriz_int(0, len(l_tamano), l_tamano)
    matriz = convertir_matriz_int(n_puestos, n_puestos, matriz)
    
    archivo.close()
    return [n_puestos, l_tamano, matriz]

#Función para obtener la distancia entre el puesto i y el puesto j
def distancia_puestos(puesto_i, puesto_j, lista_tamanos):
    suma_dist_int = 0
    for intermedio in range(puesto_i-1, puesto_j-1):
        suma_dist_int += lista_tamanos[intermedio]
    distancia = (lista_tamanos[puesto_i]/2) + (lista_tamanos[puesto_j]/2) + suma_dist_int 
    return distancia

#Función objetivo para minimizar los tiempos según la distancia entre puestos y cantidad de clientes que asisten a los puesto i y j
def funcion_objetivo(pos_i,pos_j,dist_puestos,datos):
    
    return 0

def criterio_termino():
    return 0


def solucion_inicial():
    return 0
