import math
import random
import numpy as np

# Función para transformar los datos de una matriz con string en enteros
def convertir_matriz_int(n_filas, n_columnas, matriz):
    '''
    @param n_filas: el numero de filas de la matriz
    @param n_columnas: el numero de columnas de la matriz
    @param matriz: La matriz a convertir sus elementos
    @return nueva_matriz: una nueva matriz con valores enteros en ella
    '''
    nueva_matriz = []
    if n_filas == 1:
        for i in range(0,n_columnas):
            nueva_matriz.append(int(matriz[i]))
    else:
        for i in range(0, n_filas):
            for j in range(0, n_columnas):
                nueva_matriz.append(int(matriz[i][j]))
    return nueva_matriz


# Función para obtener cantidad de puestos, lista de tamaños de locales y matriz con asistentes a los locales
def asignacion_datos(nombre_archivo):
    '''
    @param nombre_archivo: El nombre del archivo de texto a leer
    @return: Retornara una lista que contiene el el numero de puestos, una lista con las distancias de los puestos y por ultimo una matriz con el flujo de clientes.
    '''
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

    l_tamano = convertir_matriz_int(1, len(l_tamano), l_tamano)
    matriz = convertir_matriz_int(n_puestos, n_puestos, matriz)

    archivo.close()
    return [n_puestos, l_tamano, np.array(matriz).reshape(n_puestos,n_puestos) ]


# Función para obtener la distancia entre el puesto i y el puesto j
def distancia_puestos(lista_tamanos, solucion):
    '''
    @param lista_tamanos: una lista con las distancias de los puestos
    @param solucion: es una lista que contiene valores enteros que representa el orden de la solucion
    @return distancia: es un valor entero que contiene la distancia total entre los puestos.
    '''
    suma_dist_int = 0
    largo = len(solucion)
    if largo == 2:
        distancia = (lista_tamanos[solucion[0]-1] / 2) + (lista_tamanos[solucion[largo - 1]] / 2)
    else:
        for intermedio in range(1,largo - 1):
            suma_dist_int += lista_tamanos[solucion[intermedio]]
        distancia = (lista_tamanos[solucion[0]-1] / 2) + (lista_tamanos[solucion[largo - 1]] / 2) + suma_dist_int
    return distancia

# Función que ira evaluando si la temperatura es menor a la temperatura minima
def criterio_termino(T, t_minima):
    '''
    @param T: Valor de la temperatura
    @param t_minima: El valor minimo que puede llegar la temperatura
    @return True: Se retornara Verdadero cuando la temperatura sea menor o igual a la temperatura minima.
    @return False: Retornara falso cuando la temperatura sea mayor a la temperatura minima.
    '''
    if T <= t_minima:
        return True
    return False

#Funcion que crea la solucion inicial de manera random
def solucion_inicial(numero_puestos):
    '''
    @param numero_puestos: La cantidad de puestos que se quieren evaluar
    @return solucion_inicial: Una lista con valores enteros que representan la solución 
    '''
    solucion_inicial = np.arange(numero_puestos)
    np.random.shuffle(solucion_inicial)
    return solucion_inicial

#Funcion que va disminuyendo el valor de la temperatura
def enfriamiento(t, alpha):
    '''
    @param t: Valor de la temperatura
    @param alpha: Valor que al multiplicar con la temperatura, ira reduciendo la temperatura
    @return t: La nueva temperatura despues del enfriamiento.
    '''
    t = t * alpha
    return t

#Funcion donde se aplica la metaheuristica Simulated Annealing
def simulated_annealing(numero_puestos, lista_tamanos, matriz_asistentes, t_inicial, t_minima, alpha):
    '''
    @param numero_puestos: Un valor entero que hace referencia al numero de puestos
    @param lista_tamanos: una lista que contiene la distancia de cada puesto
    @param matriz_asistentes: Una matriz de enteros que contiene el flujo de personas entre puestos
    @param t_inicial: La temperatura con la que empezara el sistema
    @param t_minima: La temperatura minima que puede llegar la temperatura
    @param alpha: El valor para el enfriamiento de la temperatura
    @return s_plus: Retorna una lista de enteros con la solucion
    '''
    s = solucion_inicial(numero_puestos)
    s_plus = s
    T = t_inicial
    while criterio_termino(T, t_minima):
        s_ast = swap(s, numero_puestos)
        delta_s = funcion_objetivo(s_ast,lista_tamanos,matriz_asistentes) - funcion_objetivo(s,lista_tamanos,matriz_asistentes)
        if delta_s < 0:
            s = s_ast
        else:
            p = math.exp(-delta_s / t_inicial)
            if random.random() < p:
                s = s_ast
        s_plus = mejor_solucion(s, s_plus,lista_tamanos,matriz_asistentes)
        T = enfriamiento(T, alpha)
    return s_plus

#Funcion que retorna la mejor solucion entre dos soluciones posibles.
def mejor_solucion(s, s_plus,l_tamano,matriz):
    '''
    @param s: una lista con la 
    @param s_plus: una lista con la solucion vecino
    @param l_tamano: una lista con las distancias de los puestos
    @param matriz: una matriz con los valores entre flujo de clientes entre puestos
    @return s: retornara s siempre que la funcion objetivo sea menor a la de s_plus
    @return s_plus: retornara s_plus siempre que la funcion objetivo sea menos a la de s
    '''
    try:
        s = funcion_objetivo(s, l_tamano, matriz)
        s_plus = funcion_objetivo(s_plus, l_tamano, matriz)
        if s < s_plus:
            return s
        elif s_plus < s:
            return s_plus
    except Exception as e:
        print(str(e))

#Funcion que va creando una nueva solucion, aplicando swap a partir de una solucion inicial
def swap(solucion_inicial, numero_puestos):
    '''
    @param solucion_inicial: es una lista que contiene valores enteros que representa el orden de la solucion
    @param numero_puestos: un valor entero con la cantidad de puestos
    @return vecino: retorna una nueva solución
    '''
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
    '''
    @param solucion: es una lista que contiene valores enteros que representa el orden de la solucion
    @param l_tamano: es una lista con contiene valores enteros que representa el largo del puesto
    @param matriz_asistentes: Una matriz con valores enteros que representan el flujo de clientes entre puestos
    @return valor_obj: Retorna un valor entero que es la funcion objetivo
    '''
    valor_obj = 0
    for i in range(len(solucion)-1):
        for j in range(i+1,len(solucion)):
            valor_obj += distancia_puestos(l_tamano,solucion[i:j+1]) + matriz_asistentes[solucion[i],solucion[j]]
    return valor_obj