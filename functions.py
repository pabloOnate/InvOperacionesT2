import math
import random

# Función para transformar los datos de la matriz en enteros
import numpy as np


def convertir_matriz_int(n_filas, n_columnas, matriz):
    for i in range(0, n_filas - 1):
        for j in range(0, n_columnas - 1):
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


# Función para obtener la distancia entre el puesto i y el puesto j
def distancia_puestos(lista_tamanos, solucion):
    suma_dist_int = 0
    largo = len(solucion)
    for intermedio in range(1, largo - 2):
        suma_dist_int += lista_tamanos[intermedio]
    distancia = (lista_tamanos[solucion[0]] / 2) + (lista_tamanos[solucion[largo - 1]] / 2) + suma_dist_int
    return distancia

def criterio_termino(T, t_minima):
    if T <= t_minima:
        return True
    return False


def solucion_inicial(numero_puestos):
    solucion_inicial = np.arange(numero_puestos)
    np.random.shuffle(solucion_inicial)
    return solucion_inicial


def criterio_aceptacion(s_ast, s, t_inicial):
    delta_s = funcion_objetivo(s_ast) - funcion_objetivo(s)
    if delta_s < 0:
        return True
    if t_inicial == 0.2:
        return False
    p = math.exp(-delta_s / t_inicial)
    if random.random() < p:
        return True
    return False


def mejor_solucion(s, s_plus):
    return 0


def enfriamiento(t, alpha):
    t = t * alpha
    return t


def simulated_annealing(numero_puestos, lista_tamanos, matriz_asistentes, t_inicial, t_minima, alpha):
    s = solucion_inicial(numero_puestos)
    s_plus = s
    T = t_inicial
    while not criterio_termino(T, t_minima):
        s_ast = siguiente_vecino()
        delta_s = funcion_objetivo(s_ast) - funcion_objetivo(s)
        if delta_s < 0:
            s = s_ast
        else:
            p = math.exp(-delta_s / t_inicial)
            if random.random() < p:
                s = s_ast
        s_plus = mejor_solucion(s, s_plus)
        T = enfriamiento(T, alpha)
    return s_plus


def swap(solucion_inicial, numero_puestos):
    porcentaje_casillas = np.zeros((1, numero_puestos))
    casilla_seleccionada_r1 = 0
    casilla_seleccionada_r2 = 0
    #misma_casilla = casilla_seleccionada_r1 == casilla_seleccionada_r2
    porcentaje = 1 / numero_puestos
    suma_porcentajes = 0

    #while misma_casilla:
    random_1 = random.random()
    random_2 = random.random()
    for iter in range(numero_puestos):
        porcentaje_casillas[0][iter] = (iter + 1) * porcentaje

    for casilla in range(numero_puestos):
        suma_porcentajes += porcentaje_casillas[0][casilla]
        if ((porcentaje_casillas[0][casilla] - porcentaje) <= random_1 <= porcentaje_casillas[0][casilla]):
            casilla_seleccionada_r1 = casilla
        elif ((porcentaje_casillas[0][casilla] - porcentaje) <= random_2 <= porcentaje_casillas[0][casilla]):
            casilla_seleccionada_r2 = casilla

    casilla_a = solucion_inicial[casilla_seleccionada_r1]
    casilla_b = solucion_inicial[casilla_seleccionada_r2]
    solucion_inicial[casilla_a], solucion_inicial[casilla_b] = solucion_inicial[casilla_b], solucion_inicial[casilla_a]
    vecino = solucion_inicial
    return vecino

#Función objetivo para minimizar los tiempos según la distancia entre puestos y cantidad de clientes que asisten a los puesto i y j
def funcion_objetivo(solucion, l_tamano, matriz_asistentes):
   objetivo = 0
   d = distancia_puestos(l_tamano, solucion)
   for i in matriz_asistentes
        w = matriz_asistentes[i]
        objetivo += w * d

return objetivo