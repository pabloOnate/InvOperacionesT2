import numpy as np

#------------------------------------Funciones----------------------------------
def convertir_matriz_int(n_filas,n_columnas,matriz):
    for i in range(0,n_filas-1):
        for j in range(0,n_columnas-1):
            matriz[i][j] = int(matriz[i][j])
    return matriz  

def asignacion_datos(nombre_archivo):
    archivo = open(nombre_archivo,"r")

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
             
    l_tamano = convertir_matriz_int(0,len(l_tamano),l_tamano)
    matriz = convertir_matriz_int(n_puestos,n_puestos,matriz)
    
    archivo.close()
    return [n_puestos, l_tamano, matriz]

def distancia_puestos(pos_i,pos_j,dist_puestos):
    for intermedio in range(pos_i-1,pos_j-1):
        suma_dist_int += dist_puestos[intermedio]
    distancia = (dist_puestos[pos_i]/2) + (dist_puestos[pos_j]/2) + suma_dist_int 
    return distancia

def funcion_objetivo(pos_i,pos_j,dist_puestos,datos):
    
    return 0


#-------------------------------------PROCEDIMIENTO-----------------------------------
#Nombre del archivo de datos
nombre_archivo = "QAP_sko56_04_n.txt"

#Asignamos los valores sacados desde el archivo
datos = asignacion_datos(nombre_archivo)

n_puestos = datos[0]
l_tamano = datos[1]
matriz = datos[2]

print(n_puestos)
print(l_tamano)
print(matriz)



    




