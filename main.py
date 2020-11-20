from processData import numeroPuestos, listaTamanos, matriz
from functions import criterio_termino, solucion_inicial, siguiente_vecino, criterio_aceptacion

 
vecindario = [None]*numeroPuestos
print(matriz)
solucion = solucion_inicial()
while (criterio_termino() != True):
    nuevaSolucion = siguiente_vecino(vecindario)
    
    if(criterio_aceptacion(nuevaSolucion, solucion) == True):
        solucion = nuevaSolucion

    mejorSolucion = mejorSolucion(solucion, mejorSolucion)

print(mejorSolucion)




    




