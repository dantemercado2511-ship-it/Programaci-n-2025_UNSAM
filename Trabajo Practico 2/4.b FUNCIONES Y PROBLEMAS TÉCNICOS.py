import math

# Constantes
mu = 3.986e14     
R = 6371e3         

def transferencia_descenso(hA_km, hB_km, phi0_deg, phiB_deg):
    """
    Calcula velocidades al dejar la órbita A y al llegar al punto B
    hA_km  : altura inicial
    hB_km  : altura final
    phi0_deg : ángulo de salida en A
    phiB_deg : ángulo de llegada en B
    """
    # Convertir unidades
    rA = R + hA_km * 1000
    rB = R + hB_km * 1000
    phi0 = math.radians(phi0_deg)
    phiB = math.radians(phiB_deg)

    # 1. velocidad circular inicial en A
    vA_circ = math.sqrt(mu / rA)

    # 2. momento angular inicial en salida
    #    se desconoce V_Af, así que selo llama vAf
    #    pero debemos cumplir conservación de energía y momento angular
    #
    # Ecuación general:
    #    h = rA * vAf * cos(phi0)
    #    energía = vA_circ^2/2 - mu/rA
    #
    #    en la trayectoria balística:
    #    epsilon = vAf^2/2 - mu/rA = vBi^2/2 - mu/rB
    #
  
    # se resuelve vAf imponiendo energía total correcta
    epsilon = vA_circ**2/2 - mu/rA   # energía total de la órbita circular
    # se obtiene vBi por energía
    # vBi^2 = 2*(epsilon + mu/rB)
    # Por momento angular:
    # h = rA * vAf * cos(phi0) = rB * vBi * cos(phiB)
    #
    # ...Se Combinan ambas ecuaciones...
    #
    #   vBi = sqrt( 2*(epsilon + mu/rB) )
    #   vAf = (rB / (rA)) * (vBi * cos(phiB) / cos(phi0))

    vBi = math.sqrt(2*(epsilon + mu/rB))

    vAf = (rB * vBi * math.cos(phiB)) / (rA * math.cos(phi0))

    return vAf, vBi

# VALIDACIÓN
hA = 362.10      # km
hB = 67.37       # km
phi0 = 60        # grados
phiB = 0         # en el dibujo B es radial

vAf, vBi = transferencia_descenso(hA, hB, phi0, phiB)

print("Velocidad de salida en A (m/s):", round(vAf, 1))
print("Velocidad de llegada en B (m/s):", round(vBi, 1))
