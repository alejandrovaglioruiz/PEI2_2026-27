import numpy as np
import mathematics
import gui

# 1. Matriz de calibracion del anemometro 3D (Voltajes) 
# y vector de velocidades de viento de referencia (m/s)
voltajes_anemometro = np.array([[1.2, 0.3, 0.1], [0.2, 1.5, 0.4], [0.1, 0.2, 1.1]])
viento_referencia = np.array([15.5, -5.2, 3.1])

# 2. Datos de calibracion del altimetro barometrico: Voltaje (V) vs Presion log (ln(Pa))
v_sensor = np.array([0.5, 1.2, 2.0, 2.8, 3.5, 4.1, 5.0])
ln_presion = np.array([11.5, 10.8, 9.9, 9.1, 8.2, 7.5, 6.4])

# 3. Telemetria irregular: Tiempos de recepcion (s) y Altitud registrada (m)
t_telemetria = np.array([0, 12, 25, 43, 58, 71, 89, 105, 120, 145])
altitud_cruda = np.array([500, 650, 820, 1050, 1280, 1500, 1790, 2100, 2350, 2800])

# 4. Perfil de temperatura atmosferica en funcion del tiempo T(t) en grados Celsius
# Modelo polinomico ajustado: T(t) = 15 - 0.05*t - 0.001*t^2 + 2e-5*t^3

# 6. Datos de consumo de potencia del calefactor de a bordo (W) en el tiempo
# (Se calculara a partir de los tiempos interpolados en el apartado 3)

h_ref = []
t_ref = []
v_ref = []

def set_t(list):            # Para no calcular varias veces las listas h_ref, t_ref y v_ref y asi mejorar la
    global t_ref            # eficiencia de usan variables globales y funciones para guardarlas y usarlas
    t_ref = list

def set_h(list):
    global h_ref
    h_ref = list

def set_v(list):
    global v_ref
    v_ref = list

def get_t():
    return t_ref

def get_h():
    return h_ref

def get_v():
    return v_ref

def solve(ej1g, ej2g, ej3g, ej4g, ej5g, ej6g, ej1s, ej2s, ej3s, ej4s, ej5s, ej6s, temp, ej2t, ej3t, ej4t, ej5t, ej6t):
    solve_1(ej1g, ej1s)
    solve_2(ej2g, ej2s, ej2t)
    solve_3(ej3g, ej3s, ej3t)
    solve_4(ej4g, ej4s, temp, ej4t)
    solve_5(ej5g, ej5s, ej5t)
    solve_6(ej6g, ej6s, ej6t)

def solve_1(ej1g, ej1s):
    gui.display_1(mathematics.solve_system(voltajes_anemometro, viento_referencia), ej1g, ej1s)

def solve_2(ej2g, ej2s, ej2t):
    m, n = mathematics.minim_cuad(v_sensor, ln_presion)
    gui.display_2(m, n, v_sensor, ln_presion, ej2g, ej2s, ej2t)

def solve_3(ej3g, ej3s, ej3t):
    set_t([(t_telemetria[-1]/199)*i for i in range(0, 200)])   #se necesitan 199 intervalos para tener 200 tiempos
    h_reg, poly_coef = mathematics.interpolate(get_t(), t_telemetria, altitud_cruda)
    set_h(h_reg)
    gui.display_3(get_h(), get_t(), t_telemetria, altitud_cruda, ej3g, ej3s, ej3t, poly_coef)

def solve_4(ej4g, ej4s, temp, ej4t):
    def T (t):
        return 15 - (0.05*t) - (0.001*(t**2)) - (0.00002*(t**3)) - temp
    value, iteration_index, iteration_value = mathematics.binary_search(t_telemetria, T, 0)
    gui.display_4(value, iteration_index, iteration_value, ej4g, ej4s, temp, ej4t)

def solve_5(ej5g, ej5s, ej5t):
    set_v(mathematics.interpolate_velocidad(get_t(), get_h()))
    gui.display_5(get_t(), get_v(), ej5g, ej5s, ej5t)
    

def solve_6(ej6g, ej6s, ej6t):
    gui.display_6(mathematics.calc_energy(get_t(), get_v()), get_t(), ej6g, ej6s, ej6t)


if __name__ == "__main__":
    print("hello world!")