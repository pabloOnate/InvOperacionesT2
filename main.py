from numpy import shape, random
from processData import numero_puestos, lista_tamanos, matriz_asistentes, alpha, t_inicial, t_minima
from functions import simulated_annealing,funcion_objetivo
from random import shuffle
import numpy as np
import statistics as stats

#solucion_inicial = solucion_inicial(numero_puestos)
#print(solucion_inicial)
# vecindario = [None] * numeroPuestos
# solucion = solucion_inicial()
# while (criterio_termino() != True):
#     nuevaSolucion = siguiente_vecino(vecindario)
#
#     if(criterio_aceptacion(nuevaSolucion, solucion) == True):
#         solucion = nuevaSolucion
#
#     mejorSolucion = mejorSolucion(solucion, mejorSolucion)
#a = swap(solucion_inicial, numero_puestos)
#print(a)

resultados = []
ejecucion = 0

while ejecucion < 10:
    resultados[ejecucion] = funcion_objetivo(simulated_annealing(numero_puestos,lista_tamanos, matriz_asistentes,t_inicial,t_minima,alpha),lista_tamanos,matriz_asistentes)
    ejecucion += 1
media = stats.mean(resultados)
print(media)
desviacion_est = stats.pstdev(resultados)
print(desviacion_est)



    




