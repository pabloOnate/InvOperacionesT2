from numpy import matrix
from functions import asignacion_datos
#-------------------------------------PROCEDIMIENTO-----------------------------------
#Nombre del archivo de datos
nombre_archivo = "QAP_sko56_04_n.txt"

#Asignamos los valores sacados desde el archivo
datos_iniciales = asignacion_datos(nombre_archivo)

numero_puestos = datos_iniciales[0]
lista_tamanos = datos_iniciales[1]
matriz_asistentes = matrix(datos_iniciales[2])
