import numpy as np

# Constantes orbitales
MU = 3.986e14        
R_EARTH = 6371e3    

# Funciones de dinámica orbital
def v_circ(r):
    return np.sqrt(MU / r)

def hohmann_delta_v(h1_km, h2_km):
    """Devuelve (ΔV1, ΔV2, ΔV_total, factor_f)."""
    r1 = R_EARTH + h1_km * 1e3
    r2 = R_EARTH + h2_km * 1e3
    a_t = 0.5 * (r1 + r2)

    # Velocidades circulares
    v1 = v_circ(r1)
    v2 = v_circ(r2)

    # Transferencia
    v_per = np.sqrt(MU * (2/r1 - 1/a_t))
    v_apo = np.sqrt(MU * (2/r2 - 1/a_t))

    dv1 = v_per - v1
    dv2 = v2 - v_apo
    dv_total = dv1 + dv2

    factor_f = v2 / v1  # v_final / v_inicial

    return dv1, dv2, dv_total, factor_f

#         CLASS Vehiculo_e()
class Vehiculo_e:

    # Contador global de instancias
    contador = 0

    def __init__(self, altura_km: float, masa_kg: float, nombre: str = None):
        
        # Contador para nombre automático
        Vehiculo_e.contador += 1
        if nombre is None:
            self.nombre = str(Vehiculo_e.contador).zfill(4)
        else:
            self.nombre = nombre

        # Estado inicial
        self.altura_km = float(altura_km)
        self.masa_kg = float(masa_kg)

        # Radio orbital
        self.r_orbita = R_EARTH + self.altura_km * 1e3

        # Órbita circular → e = 0
        self.excentricidad = 0.0
        self.semieje_mayor = self.r_orbita
        self.semieje_menor = self.r_orbita

        # Velocidad nominal circular
        self.v_nominal = v_circ(self.r_orbita)

        # Atributos de maniobras
        self.delta_v = 0.0
        self.factor_f = 1.0

    # Cambio de órbita circular → circular (Hohmann)
    def cambiar_orbita(self, nueva_altura_km: float):
        dv1, dv2, dv_total, f = hohmann_delta_v(self.altura_km, nueva_altura_km)

        # Guardar resultados
        self.delta_v = dv_total
        self.factor_f = f

        # Actualizar parámetros orbitales
        self.altura_km = nueva_altura_km
        self.r_orbita = R_EARTH + self.altura_km * 1e3

        self.excentricidad = 0.0
        self.semieje_mayor = self.r_orbita
        self.semieje_menor = self.r_orbita
        self.v_nominal = v_circ(self.r_orbita)

    # Representación en terminal
    def __repr__(self):
        return (f"VE [{self.nombre}] – masa={self.masa_kg:.1f} kg, "
                f"h={self.altura_km:.1f} km, e={self.excentricidad}, "
                f"a={self.semieje_mayor:.1f} m")

    # Comparación → están en la misma órbita
    def __eq__(self, other):
        if not isinstance(other, Vehiculo_e):
            return False
        return np.isclose(self.altura_km, other.altura_km)

    # Para permitir ordenar por masa
    def __lt__(self, other):
        return self.masa_kg < other.masa_kg

    # Cómo aparece dentro de listas, tuplas, sets
    def __str__(self):
        return f"{self.nombre} (masa={self.masa_kg:.1f} kg)"
