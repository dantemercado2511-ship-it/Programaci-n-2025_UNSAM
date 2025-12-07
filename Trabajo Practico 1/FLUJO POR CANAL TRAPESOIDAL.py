import math

#canal trapezoidal
Q = 20         # m3/s
g = 9.81       # m/s2

def B(y):
    return 3 + y

def A_c(y):
    return 3*y + (y**2)/2

def f(y):
    """Ecuación del canal trapezoidal."""
    return 1 - (Q**2) / (g * (A_c(y)**3) * B(y))

# función de bisección,
def biseccion_f(func, xi, xu, tol=0.01, max_iter=10):
    pasos = 0
    while pasos < max_iter:
        pasos += 1
        xm = (xi + xu) / 2
        f_xm = func(xm)

        # error aproximado
        if pasos > 1:
            ea = abs((xm - xm_prev) / xm) * 100
            if ea < tol:
                return xm, pasos
        xm_prev = xm

        # bisección clásica
        if func(xi) * f_xm < 0:
            xu = xm
        else:
            xi = xm

    return xm, pasos

if __name__ == "__main__":
    print("Calculando profundidad crítica del canal...")

    raiz, pasos = biseccion_f(f, 0.5, 2.5)

    print(f"\nProfundidad crítica (y): {raiz:.6f} m")
    print(f"Iteraciones: {pasos}")
