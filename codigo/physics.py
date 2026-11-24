from numpy import array
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

def solve():
    solve_1()
    solve_2()
    solve_3()
    solve_4()
    solve_5()
    solve_6()

def solve_1():
    gui.display_1(mathematics.solve_system(voltajes_anemometro, viento_referencia))

def solve_2():
    print("hello world!")

def solve_3():
    print("hello world!")

def solve_4():
    print("hello world!")

def solve_5():
    print("hello world!")

def solve_6():
    print("hello world!")


if __name__ == "__main__":    #esta declaracion se usa para probar logica dentro de mathematics.py
    print("hello world!")