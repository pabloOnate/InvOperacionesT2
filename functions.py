import math
import random
from processData import t_minima

# Función para transformar los datos de la matriz en enteros
import numpy as np
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
def distancia_puestos(lista_tamanos,solucion):
    suma_dist_int = 0
    largo = len(solucion)
    for intermedio in range(1, largo-2):
        suma_dist_int += lista_tamanos[intermedio]
    distancia = (lista_tamanos[solucion[0]]/2) + (lista_tamanos[solucion[largo-1]]/2) + suma_dist_int 
    return distancia

#Función objetivo para minimizar los tiempos según la distancia entre puestos y cantidad de clientes que asisten a los puesto i y j
def distancia_intermedia(l_tamano, i, j)
    d = (l_tamano[i] + l_tamano[j]) / 2
    for k = i + 1 in range(j-1):
        d += lista_tamanos[k]
    return d

def funcion_objetivo(l_tamano, matriz):
    largo = len(l_tamano)
    for i = 1 in largo-1
        for j = i+1 in largo
            w = matriz[i,j]
            d = distancia_intermedia(l_tamano, i, j)
            objetivo = w * d
    return objetivo

def criterio_termino(T, t_minima):
    if T <= t_minima:
        return True
    return False


def solucion_inicial(numero_puestos):
    solucion_inicial = np.arange(numero_puestos)
    np.random.shuffle(solucion_inicial)
    return solucion_inicial

def criterio_aceptacion(s_ast,s,t_inicial):
    delta_s = funcion_objetivo(s_ast) - funcion_objetivo(s)
    if delta_s < 0:
        return True
    if t_inicial == 0.2:
        return False
    p = math.exp(-delta_s/t_inicial)
    if random.random() < p:
        return True
    return False
