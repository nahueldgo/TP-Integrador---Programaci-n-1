import time # Para medir el tiempo. 
import random # Para generar lsitas aleatorias.

#Algoritmo de ordenamiento Bublble sort.
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

#Algoritmo de ordenamiento Insertion Sort.
def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

# Función para medir el tiempo de ejecución
def medir_tiempo(algoritmo, datos):
    tiempos = []
    for _ in range(3):#Repite la prueba 3 veces
        lista = datos.copy() # usa una copia para que no este ordenado 
        inicio = time.time()
        algoritmo(lista)
        fin = time.time()
        tiempos.append((fin - inicio) * 1000) # Guarda el tiempo en milisegundos 
    return sum(tiempos) / len(tiempos) # Devuelve el promedio de las ejecuciones

# 🔹 Tamaños de lista que se van a probar
tamaños = [500, 1000, 2000]

# 🔹 Imprime encabezado
print("Tamaño \tBubble Sort (ms) \tInsertion Sort (ms)")

# 🔹 Ejecuta las pruebas
for n in tamaños:
    lista = [random.randint(1, 10000) for _ in range(n)]  # Genera una lista aleatoria
    t_bubble = medir_tiempo(bubble_sort, lista)           # Mide el tiempo de Bubble Sort
    t_insertion = medir_tiempo(insertion_sort, lista)     # Mide el tiempo de Insertion Sort
    print(f"{n}\t{t_bubble:.2f}\t\t\t{t_insertion:.2f}")   # Muestra resultados