from __future__ import annotations
import numpy as np

# Constantes globales (SI)
MU = 3.986e14       
R_EARTH = 6371e3    
# Funciones auxiliares internas
def _v_circ(r_m: float) -> float:
    """Velocidad circular [m/s] para radio r [m]."""
    return np.sqrt(MU / r_m)

def _hohmann_delta_v(r1_m: float, r2_m: float):
    """Devuelve dv1, dv2, dv_total, factor_f usando fórmula de Hohmann."""
    a_t = 0.5 * (r1_m + r2_m)

    v1 = _v_circ(r1_m)
    v2 = _v_circ(r2_m)

    # Velocidades en la órbita de transferencia
    v_per = np.sqrt(MU * (2 / r1_m - 1 / a_t))
    v_apo = np.sqrt(MU * (2 / r2_m - 1 / a_t))

    dv1 = v_per - v1
    dv2 = v2 - v_apo
    dv_total = dv1 + dv2
    factor_f = v2 / v1

    return dv1, dv2, dv_total, factor_f

#       CLASS Vehiculo_e (API requerida)
class Vehiculo_e:
    _contador = 0    # contador para nombres automáticos
    def __init__(self, masa_kg: float, h_km: float, nombre: str | None = None):
        """
        Crea una instancia de vehículo espacial en órbita circular.
        nombre: nombre opcional
        """
        Vehiculo_e._contador += 1
        if nombre is None:
            self.nombre = str(Vehiculo_e._contador).zfill(4)
        else:
            self.nombre = nombre

        # Estado físico
        self.masa_kg = float(masa_kg)
        self.h_km = float(h_km)

        # Parámetros orbitales
        self.r_m = R_EARTH + self.h_km * 1e3      # radio orbital [m]
        self.excentricidad = 0.0
        self.semieje_mayor = self.r_m
        self.semieje_menor = self.r_m
        self.v_nominal = _v_circ(self.r_m)

        # Datos de maniobra
        self.delta_v = 0.0
        self.factor_f = 1.0

    #   Cambiar órbita circular → circular (Hohmann)
    def cambiar_orbita(self, nueva_h_km: float) -> float:
        """
        Realiza la maniobra de Hohmann a la nueva órbita circular
        nueva_h_km: altura destino en km
        Devuelve:
            delta_v_total [m/s]
        """
        r1 = self.r_m
        r2 = R_EARTH + nueva_h_km * 1e3

        dv1, dv2, dv_total, f = _hohmann_delta_v(r1, r2)

        # Guardar resultados
        self.delta_v = dv_total
        self.factor_f = f

        # Actualizar parámetros orbitales
        self.h_km = nueva_h_km
        self.r_m = r2
        self.excentricidad = 0.0
        self.semieje_mayor = r2
        self.semieje_menor = r2
        self.v_nominal = _v_circ(r2)

        return dv_total
    # Representación legible
    def __repr__(self):
        return (f"VE({self.nombre}) – masa={self.masa_kg:.1f} kg, "
                f"h={self.h_km:.1f} km, e={self.excentricidad}, "
                f"a={self.semieje_mayor:.1f} m")
    # Comparación por órbita
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehiculo_e):
            return False
        return np.isclose(self.h_km, other.h_km)
    # Ordenamiento por masa
    def __lt__(self, other: "Vehiculo_e") -> bool:
        return self.masa_kg < other.masa_kg
    # Representación cuando está dentro de contenedores
    def __str__(self):
        return f"{self.nombre} (masa={self.masa_kg:.1f} kg)"

# Test unitario dentro de __main__
if __name__ == "__main__":

    sat1 = Vehiculo_e(1100, 400)
    sat2 = Vehiculo_e(950, 600)
    # Test de __repr__
    print(sat1)
    print(sat2)
    # Test cambio de órbita
    dv = sat1.cambiar_orbita(700)
    print("ΔV aplicado:", dv)
    print("Factor f:", sat1.factor_f)
    # Test ordenamiento por masa
    lista = [sat1, sat2]
    lista.sort()
    print("Ordenados:", lista)
