import os
import numpy as np
import time

# Numero de hilos para la ejecución de operaciones vectorizadas

base = 2

N = 100_000_000

A = np.random.rand(N)
B = np.random.rand(N)

# Bucle for para sumar los elementos de A y B y almacenar el resultado en C
print("Ejecucion con for...")
inicio = time.time()

C = [0]*N

for i in range(N):
    C[i] = A[i] + B[i]

fin = time.time()
print("Tiempo con for:", fin - inicio)

# Vectorización con NumPy para sumar los elementos de A y B y almacenar el resultado en C, 
# utilizando diferentes números de hilos y midiendo el tiempo de ejecución para cada caso.
tiempo_base = 0
print("\nEjecucion con NumPy utilizando diferentes números de hilos:")
for i in range(4):
    NUM_HILOS = base**i

    print("\nEjecutando con ", NUM_HILOS, " hilos, iteracion...")
    os.environ["OMP_NUM_THREADS"] = str(NUM_HILOS)
    os.environ["OPENBLAS_NUM_THREADS"] = str(NUM_HILOS)
    os.environ["MKL_NUM_THREADS"] = str(NUM_HILOS)
    tiempos = []

    for j in range(5):
        inicio = time.time()
        C = A + B
        fin = time.time()
        tiempos.append(fin - inicio)
        print("Ejecucion", j+1, ":", fin - inicio)

    tiempos.sort()
    tiempos_filtrados = tiempos[1:-1]  # Elimina menor y mayor tiempo
    promedio = sum(tiempos_filtrados) / len(tiempos_filtrados)
    
    if NUM_HILOS == 1:
        tiempo_base = promedio       
    speedup = tiempo_base / promedio

    print("Tiempo con NumPy ", NUM_HILOS, " hilos: ", promedio)
    print("Speedup:", speedup)
    print("Eficiencia: ", speedup/NUM_HILOS)




