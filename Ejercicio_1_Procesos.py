import multiprocessing
import time
import numpy as np

def suma_parcial(datos):
    return sum(datos)

def ejecutar_paralelo(datos, num_procesos):
    inicio = time.time()

    tamaño = len(datos) // num_procesos
    partes = [datos[i*tamaño:(i+1)*tamaño] for i in range(num_procesos)]

    if len(datos) % num_procesos != 0:
        partes[-1] = np.concatenate((partes[-1], datos[num_procesos*tamaño:]))

    with multiprocessing.Pool(processes=num_procesos) as pool:
        resultados = pool.map(suma_parcial, partes)

    resultado_final = sum(resultados)
    fin = time.time()

    return resultado_final, fin - inicio

if __name__ == "__main__":

    N = 100_000_000
    datos = np.random.randint(0, 10, N)

    # Secuencial 
    inicio = time.time()
    resultado_sec = sum(datos)
    fin = time.time()

    tiempo_sec = fin - inicio

    print("Secuencial:")
    print("Tiempo:", tiempo_sec, "segundos\n")

    # Paralelo

    for procesos in [2, 4, 8]:
        resultado_par, tiempo_par = ejecutar_paralelo(datos, procesos)

        speedup = tiempo_sec / tiempo_par

        print(f"Paralelo ({procesos} procesos):")
        print("Tiempo:", tiempo_par, "segundos")
        print("Speedup:", speedup)
        print("Eficiencia: ", speedup/procesos)
        print()