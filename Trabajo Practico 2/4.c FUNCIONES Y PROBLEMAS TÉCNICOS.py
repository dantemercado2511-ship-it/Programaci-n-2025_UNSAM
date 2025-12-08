import numpy as np
import matplotlib.pyplot as plt

# Constantes
mu = 3.986e14           # m^3/s^2  (GM de la Tierra)
R  = 6371e3             # m       (radio terrestre)
# Datos
hA = 362.10e3
hB =  67.37e3
phi0_deg = 60           # ángulo de salida nominal del punto b
phi0 = np.radians(phi0_deg)
rA = R + hA
rB = R + hB

# Velocidad circular en A
vA_circ = np.sqrt(mu / rA)

# --- Punto b para obtener el ΔV nominal original ---
# Energía orbital inicial
epsilon = vA_circ**2 / 2 - mu / rA
vB_nom = np.sqrt(2 * (epsilon + mu/rB))
# Momento angular conservado
h_nom = rA * vA_circ * np.cos(phi0)
# Velocidad nominal en A (tras ΔV en tangencial inverso)
vA_nom = 3450.3   # m/s dado en el enunciado (debug real)
DV_b = vA_nom - vA_circ   # ΔV original de punto (b), negativo

# NUEVA ESTRATEGIA
percent_list = np.linspace(0.05, 1.00, 20)

phiB_list = []
vB_list   = []

for p in percent_list:
    DV = p * abs(DV_b)       # valor positivo
    # Vector velocidad en A
    vA_t = vA_circ                # tangencial
    vA_r = DV                     # radial hacia afuera
    vA = np.sqrt(vA_t**2 + vA_r**2)
    # Nuev energía
    epsilon_c = vA**2/2 - mu / rA
    # Conservación del momento angular
    h_c = rA * vA_t               # sólo la componente tangencial produce h
    # Velocidad de llegada a rB
    vB = np.sqrt(2*(epsilon_c + mu/rB))
    # Ángulo de llegada (por momento angular)
    phiB = np.arccos( h_c / (rB * vB) )
    phiB_deg = np.degrees(phiB)
    phiB_list.append(phiB_deg)
    vB_list.append(vB)

#     GRAFICAR  V_B  vs   φ_B
plt.figure(figsize=(8,6))
plt.plot(phiB_list, vB_list, 'o-', color='blue')

for i, p in enumerate(percent_list):
    plt.text(phiB_list[i], vB_list[i], f"{int(p*100)}%", fontsize=8)

plt.xlabel("Ángulo de llegada φ_B (grados)")
plt.ylabel("Velocidad en B   V_B (m/s)")
plt.title("Velocidad en B vs Ángulo de llegada φ_B \n(porcentajes de energía aplicada en A)")
plt.grid(True)
plt.show()
