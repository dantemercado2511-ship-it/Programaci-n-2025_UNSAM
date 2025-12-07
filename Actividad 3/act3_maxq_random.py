# -*- coding: utf-8 -*-

"""Actividad 3 — Simulaciones aleatorias para max(q)"""

import random
import statistics
from act3_max import max_y_pos  

def generar_q(n):
  
"""Genera una lista de n números aleatorios uniformes en [0,1]."""
    return [random.random() for _ in range(n)]

def simulacion(n, repeticiones=300):

"""Genera un vector q de tamaño n
Obtiene el máximo y su posición combinando max_y_pos(q)
Devuelve:
máximos
posiciones"""

    maximos = []
    posiciones = []

    for _ in range(repeticiones):
        q = generar_q(n)
        m, p = max_y_pos(q)
        maximos.append(m)
        posiciones.append(p)

    return maximos, posiciones

def imprimir_estadisticas(maximos, posiciones):
   
"""Imprime media y desvío estándar para máximos y posiciones"""
    print("\nRESULTADOS DE 300 SIMULACIONES")
    print(f"Media del valor máximo:          {statistics.mean(maximos):.4f}")
    print(f"Desvío estándar del máximo:      {statistics.stdev(maximos):.4f}")
    print(f"Media de la posición del máximo: {statistics.mean(posiciones):.2f}")
    print(f"Desvío estándar de posición:     {statistics.stdev(posiciones):.2f}")

if __name__ == "__main__":
    n = 50
    
    maximos, posiciones = simulacion(n)
    imprimir_estadisticas(maximos, posiciones)

    print("\nPrimeros 10 valores máximos (solo referencia):")
    print(maximos[:10])
