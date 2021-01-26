# # Ejercicio _colabirativo_

#cambios introducidos 25/01
import numpy as np


# **Ejercicio 1**: Escribir un arreglo con 100 números equiespaciados del 0 al 9. Pista: `linspace`

np.linspace(0,9,100)


# **Ejercicio 2:** crear un arreglo 1D de 20 ceros. 
# Reemplazar los primeros 15 elementos por unos.

arr = np.zeros(20)
nuevo = np.ones(15)
arr[:15] = nuevo
arr


# **Ejercicio 3:** crear un arreglo 1D de 50 ceros. 
# Reemplazar los primeros 25 elementos por los números naturales del 0 al 24.

arr = np.zeros(50)
new = np.arange(25)
arr[:25] = new
arr


# **Ejercicio 4:** crear un arreglo 2D de 3 filas y 3 columnas, lleno de ceros. 
# Reemplazar los elemento de la segunda columna por los números 1, 2 y 3 respectivamente. 
# Es decir, crear la siguiente matriz:
# 
# ```
# 0 1 0 
# 0 2 0
# 0 3 0
# ```

arr = np.zeros((3,3))
arr[:,1] = [1,2,3]
arr


# **Ejercicio 5:** crear un arreglo 2D de 3 filas y 3 columnas, lleno de ceros. 
# Reemplazar los elemento de la diagonal por unos. Es decir, crear la siguiente matriz:
# 
# ```
# 1 0 0 
# 0 1 0
# 0 0 1
# ```

arr = np.zeros((3,3))
for i in range(3):
    arr[i,i] = 1

# **Ejercicio 6:** crear un arreglo 2D de 100 filas y 100 columnas, lleno de ceros. 
# Reemplazar los elemento de la diagonal por unos. Es decir, crear la siguiente matriz:
# 
# ```
# 1 0 0 ... 0 0 0 
# 0 1 0 ... 0 0 0
# 0 0 1 ... 0 0 0
# ...  
# 0 0 0 ... 1 0 0
# 0 0 0 ... 0 1 0
# 0 0 0 ... 0 0 1
# ```

arr = np.zeros((100,100))
arr = np.eye(100)
arr
