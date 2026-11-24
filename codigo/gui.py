import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Slider
import physics

def display_results(radio, slider):
    radio = radio
    slider = slider
    plt.show()

def crea_ejes():
    fig = plt.figure(figsize=(15, 7))

    ej1g = fig.add_subplot(231, projection='3d')
    ej2g = fig.add_subplot(232)
    ej3g = fig.add_subplot(233)
    ej4g = fig.add_subplot(234)
    ej5g = fig.add_subplot(235)
    ej6g = fig.add_subplot(236)

    fig.subplots_adjust(wspace=0.25, hspace = 0.38, left = 0.19, right = 0.97, top = 0.93, bottom = 0.084)

    ej1s = fig.add_axes([0.15, 0.15, 0.7, 0.7], projection='3d')
    ej2s = fig.add_axes([0.25, 0.15, 0.7, 0.7])
    ej3s = fig.add_axes([0.25, 0.15, 0.7, 0.7])
    ej4s = fig.add_axes([0.25, 0.15, 0.55, 0.7])
    ej5s = fig.add_axes([0.25, 0.15, 0.7, 0.7])
    ej6s = fig.add_axes([0.25, 0.15, 0.7, 0.7])

    ej1s.set_visible(False)
    ej2s.set_visible(False)
    ej3s.set_visible(False)
    ej4s.set_visible(False)
    ej5s.set_visible(False)
    ej6s.set_visible(False)

    rax = fig.add_axes([0.01, 0.3, 0.12, 0.4])
    radio = RadioButtons(rax, ("Todos", "Vector", "Presion", "Altitud", "Convergencia", "Velocidad", "Energia"))

    sax = fig.add_axes([0.9, 0.15, 0.03, 0.65])
    slider = Slider(ax=sax, label='Temperatura Critica', valmin=-20, valmax=0, valinit=-10, valstep=1, orientation='vertical')

    sax.set_visible(False)

    def change_view(label):
        ej1s.set_visible(False)
        ej2s.set_visible(False)
        ej3s.set_visible(False)
        ej4s.set_visible(False)
        ej5s.set_visible(False)
        ej6s.set_visible(False)
        ej1g.set_visible(False)
        ej2g.set_visible(False)
        ej3g.set_visible(False)
        ej4g.set_visible(False)
        ej5g.set_visible(False)
        ej6g.set_visible(False)
        sax.set_visible(False)

        if label == "Todos":
            ej1g.set_visible(True)
            ej2g.set_visible(True)
            ej3g.set_visible(True)
            ej4g.set_visible(True)
            ej5g.set_visible(True)
            ej6g.set_visible(True)
        elif label == "Vector":
            ej1s.set_visible(True)
        elif label == "Presion":
            ej2s.set_visible(True)
        elif label == "Altitud":
            ej3s.set_visible(True)
        elif label == "Convergencia":
            ej4s.set_visible(True)
            sax.set_visible(True)
        elif label == "Velocidad":
            ej5s.set_visible(True)
        elif label == "Energia":
            ej6s.set_visible(True)

        fig.canvas.draw_idle()

    def update_temp(ntemp):
        ej4g.clear()
        ej4s.clear()
        physics.solve_4(ej4g, ej4s, ntemp)

    radio.on_clicked(change_view)
    slider.on_changed(update_temp)

    return ej1g, ej2g, ej3g, ej4g, ej5g, ej6g, ej1s, ej2s, ej3s, ej4s, ej5s, ej6s, radio, slider

def display_1(v, ejg, ejs): #vector

    ejg.quiver(0, 0, 0, v[0], v[1], v[2],
            color="red",
            arrow_length_ratio=0.15)

    ejg.set_xlabel("X")
    ejg.set_ylabel("Y")
    ejg.set_zlabel("Z")

    ejg.set_title(f"Vector Resultante de Viento\nV = ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})")

    margin = 1.2

    ejg.set_xlim(0, v[0] * margin)
    ejg.set_ylim(0, v[1] * margin)
    ejg.set_zlim(0, v[2] * margin)

    ejs.quiver(0, 0, 0, v[0], v[1], v[2],
        color="red",
        arrow_length_ratio=0.15)

    ejs.set_xlabel("X")
    ejs.set_ylabel("Y")
    ejs.set_zlabel("Z")

    ejs.set_title(f"Vector Resultante de Viento\nV = ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})")

    margin = 1.2

    ejs.set_xlim(0, v[0] * margin)
    ejs.set_ylim(0, v[1] * margin)
    ejs.set_zlim(0, v[2] * margin)

def display_2(m, n, v, lnP, ejg, ejs):   #float, float, vector, vector
    ejg.scatter(v, lnP, color="green")

    ejg.plot([v[0], v[-1]],[(v[0] * m) + n, (v[-1] * m) + n],color="green")

    ejg.set_xlabel("Voltage (Voltios)")
    ejg.set_ylabel("ln(Presion)")
    ejg.set_title("Recta de ajuste Voltage frente Ln(Presion)")

    ejs.scatter(v, lnP, color="green")

    ejs.plot([v[0], v[-1]],[(v[0] * m) + n, (v[-1] * m) + n],color="green")

    ejs.set_xlabel("Voltage (Voltios)")
    ejs.set_ylabel("ln(Presion)")
    ejs.set_title("Recta de ajuste Voltage frente Ln(Presion)")

def display_3(h_reg, t_reg, t_telemetria, altitud_cruda, ejg, ejs):
    ejg.scatter(t_telemetria, altitud_cruda, color="blue")
    ejg.plot(t_reg, h_reg, color="blue")

    ejg.set_xlabel("Tiempo (segundos)")
    ejg.set_ylabel("Altitud (metros)")
    ejg.set_title("Altitud frente Tiempo Interpolada")

    ejs.scatter(t_telemetria, altitud_cruda, color="blue")
    ejs.plot(t_reg, h_reg, color="blue")

    ejs.set_xlabel("Tiempo (segundos)")
    ejs.set_ylabel("Altitud (metros)")
    ejs.set_title("Altitud frente Tiempo Interpolada")


def display_4(value, iteration_index, iteration_value, ejg, ejs, t):
    ejg.plot(iteration_index, iteration_value, color="purple")

    ejg.set_xlabel("Indice de iteracion")
    ejg.set_ylabel("Valor de la iteracion (segundos)")
    ejg.set_title(f"Conv. de T(t) a {t} grados \n Resultado de la convergencia = {value:.2f} s")

    ejs.plot(iteration_index, iteration_value, color="purple")

    ejs.set_xlabel("Indice de iteracion")
    ejs.set_ylabel("Valor de la iteracion (segundos)")
    ejs.set_title(f"Conv. de T(t) a {t} grados \n Resultado de la convergencia = {value:.2f} s")


def display_5(tiempos, velocidades, ejg, ejs):
    ejg.plot(tiempos, velocidades, color="orange")

    ejg.set_xlabel("Tiempo (segundos)")
    ejg.set_ylabel("Veocidad (m/s)")
    ejg.set_title("Velocidad de la Sonda frente el Tiempo")

    ejs.plot(tiempos, velocidades, color="orange")

    ejs.set_xlabel("Tiempo (segundos)")
    ejs.set_ylabel("Veocidad (m/s)")
    ejs.set_title("Velocidad de la Sonda frente el Tiempo")


def display_6(energia, tiempo, ejg, ejs):
    ejg.plot(tiempo, energia, color="brown")

    ejg.set_xlabel("Tiempo (segundos)")
    ejg.set_ylabel("Energia (Julios)")
    ejg.set_title("Energia frente el Tiempo")

    ejs.plot(tiempo, energia, color="brown")

    ejs.set_xlabel("Tiempo (segundos)")
    ejs.set_ylabel("Energia (Julios)")
    ejs.set_title("Energia frente el Tiempo")

if __name__ == "__main__":    #esta declaracion se usa para probar logica dentro de mathematics.py
    print("hello world!")