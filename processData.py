from numpy import matrix
from functions import asignacion_datos
#-------------------------------------PROCEDIMIENTO-----------------------------------
#Nombre del archivo de datos
nombre_archivo = "QAP_sko56_04_n.txt"

#Asignamos los valores sacados desde el archivo
datosIniciales = asignacion_datos(nombre_archivo)

numeroPuestos = datosIniciales[0]
listaTamanos = datosIniciales[1]
matriz = matrix(datosIniciales[2])
