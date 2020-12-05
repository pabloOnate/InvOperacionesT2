from numpy import shape, random
from processData import numero_puestos, lista_tamanos, matriz_asistentes, alpha, t_inicial, t_minima
from functions import simulated_annealing,funcion_objetivo
from random import shuffle
import numpy as np
import statistics as stats

soluciones = []
resultados = []
ejecucion = 0

while ejecucion < 10:
    soluciones.append(simulated_annealing(numero_puestos,lista_tamanos, matriz_asistentes,t_inicial,t_minima,alpha))
    resultados.append(funcion_objetivo(soluciones[ejecucion],lista_tamanos,matriz_asistentes))
    ejecucion += 1

print("Soluciones")
print(soluciones)
print("Funciones objetivos")
print(resultados)
media = stats.mean(resultados)
print("Media: ",media)
desviacion_est = stats.pstdev(resultados)
print("Desviacion Estandar: ",desviacion_est)



    




