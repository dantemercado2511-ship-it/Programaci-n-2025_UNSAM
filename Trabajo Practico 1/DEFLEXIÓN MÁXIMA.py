import math

# Parámetros (se convierte L a centímetros para ser coherentes con E e I)
L_mm = 600.0               # L dado en mm
L = L_mm / 10.0            # pasar a cm (1 cm = 10 mm) -> L en cm = 60 cm

E = 50000.0                # kN / cm^2
I = 30000.0                # cm^4
w0 = 2.5                   # kN / cm

# Factor global de la ecuación y(x)
def y_of_x(x_cm):
    factor = w0 / (120.0 * E * I * L)
    return factor * (-x_cm**5 + 2.0 * L**2 * x_cm**3 - L**4 * x_cm)

# Derivada dy/dx
def dy_dx_polynomial(x_cm):
    return -5.0 * x_cm**4 + 6.0 * (L**2) * x_cm**2 - L**4

# Bisección para encontrar raíz de dy/dx dentro del intervalo (0, L)
def bisection_root(func, a, b, tol=1e-8, max_iter=100):
    fa = func(a)
    fb = func(b)
    if fa == 0:
        return a, 0
    if fb == 0:
        return b, 0
    if fa * fb > 0:
        raise ValueError("No hay cambio de signo en el intervalo inicial para bisección.")
    iter_count = 0
    while iter_count < max_iter:
        iter_count += 1
        m = 0.5 * (a + b)
        fm = func(m)
        # parada por tolerancia en x
        if abs(fm) == 0 or (b - a)/2.0 < tol:
            return m, iter_count
        # actualizar intervalo
        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
    # si se acabaron las iteraciones, devolvemos la mejor aproximación
    return 0.5 * (a + b), iter_count

if __name__ == "__main__":
    # Se busca la raíz interior: se sabe que hay una raíz en (0, L) at ~ L/sqrt(5)
    # Se usa un intervalo que contenga la raíz: [0.1 L, 0.9 L]
    a = 0.0 + 1e-6
    b = L - 1e-6

    x_root_cm, iters = bisection_root(dy_dx_polynomial, a, b, tol=1e-9, max_iter=200)

    y_max_cm = y_of_x(x_root_cm)

    # Se pasan resultados a mm para posición y a mm para deflexión (1 cm = 10 mm)
    x_root_mm = x_root_cm * 10.0
    y_max_mm = y_max_cm * 10.0

    print("Resultados (usando unidades consistentes):")
    print(f"L = {L_mm:.1f} mm  (usado L = {L:.3f} cm internamente)")
    print(f"Iteraciones bisección: {iters}")
    print(f"Posición de deflexión máxima: x = {x_root_mm:.6f} mm (≈ {x_root_cm:.6f} cm)")
    print(f"Deflexión máxima: y = {y_max_mm:.6e} mm (≈ {y_max_cm:.6e} cm)")
