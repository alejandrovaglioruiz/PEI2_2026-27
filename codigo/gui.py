import matplotlib.pyplot as plt

def display_results():
    plt.show()

def crea_ejes():
    fig = plt.figure(figsize=(15, 7))

    ej1 = fig.add_subplot(231, projection='3d')
    ej2 = fig.add_subplot(232)
    ej3 = fig.add_subplot(233)
    ej4 = fig.add_subplot(234)

    fig.subplots_adjust(wspace=0.25, hspace = 0.38, left = 0.054, right = 0.97, top = 0.93, bottom = 0.084)
    
    return ej1, ej2, ej3, ej4

def display_1(v, ej): #vector

    ej.quiver(0, 0, 0, v[0], v[1], v[2],
            color='red',
            arrow_length_ratio=0.15)

    ej.set_xlabel('X')
    ej.set_ylabel('Y')
    ej.set_zlabel('Z')

    ej.set_title(f'Vector Resultante de Viento\nV = ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})')

    margin = 1.2

    ej.set_xlim(0, v[0] * margin)
    ej.set_ylim(0, v[1] * margin)
    ej.set_zlim(0, v[2] * margin)

def display_2(m, n, v, lnP, ej):   #float, float, vector, vector
    ej.scatter(v, lnP, color="green")

    ej.plot([v[0], v[-1]],[(v[0] * m) + n, (v[-1] * m) + n],color="green")

    ej.set_xlabel("Voltage")
    ej.set_ylabel("ln(Presion)")
    ej.set_title("Recta de ajuste Voltage frente Ln(Presion)")

def display_3(h_reg, t_reg, t_telemetria, altitud_cruda, ej):
    ej.scatter(t_telemetria, altitud_cruda, color="blue")
    ej.plot(t_reg, h_reg, color="blue")

    ej.set_xlabel("Tiempo")
    ej.set_ylabel("Altitud")
    ej.set_title("Altitud frente Tiempo Interpolada")

def display_4(value, iteration_index, iteration_value, ej):
    ej.plot(iteration_index, iteration_value, color="purple")

    ej.set_xlabel("Indice de iteracion")
    ej.set_ylabel("Valor de la iteracion (tiempo)")
    ej.set_title(f"Conv. de T(t) a -10 grados \n Resultado de la convergencia = {value:.2f} s")

if __name__ == "__main__":    #esta declaracion se usa para probar logica dentro de mathematics.py
    print("hello world!")