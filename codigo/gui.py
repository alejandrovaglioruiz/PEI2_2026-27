import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Slider
import physics
import mathematics

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
    
    ej2s = fig.add_axes([0.4, 0.15, 0.53, 0.7])
    ej2t = fig.add_axes([0.18, 0.15, 0.1, 0.7])

    ej3s = fig.add_axes([0.4, 0.15, 0.53, 0.7])
    ej3t = fig.add_axes([0.18, 0.15, 0.1, 0.7])
    
    ej4s = fig.add_axes([0.45, 0.15, 0.4, 0.7])
    ej4t = fig.add_axes([0.18, 0.00, 0.2, 1])
    
    ej5s = fig.add_axes([0.35, 0.15, 0.6, 0.7])
    ej5t = fig.add_axes([0.18, 0.15, 0.1, 0.7])
    
    ej6s = fig.add_axes([0.35, 0.15, 0.6, 0.7])
    ej6t = fig.add_axes([0.18, 0.15, 0.1, 0.7])

    ej2t.axis("off")
    ej3t.axis("off")
    ej4t.axis("off")
    ej5t.axis("off")
    ej6t.axis("off")

    ej1s.set_visible(False)
    ej2s.set_visible(False)
    ej3s.set_visible(False)
    ej4s.set_visible(False)
    ej5s.set_visible(False)
    ej6s.set_visible(False)
    ej2t.set_visible(False)
    ej3t.set_visible(False)
    ej4t.set_visible(False)
    ej5t.set_visible(False)
    ej6t.set_visible(False)

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
        ej2t.set_visible(False)
        ej3t.set_visible(False)
        ej4t.set_visible(False)
        ej5t.set_visible(False)
        ej6t.set_visible(False)

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
            ej2t.set_visible(True)
        elif label == "Altitud":
            ej3s.set_visible(True)
            ej3t.set_visible(True)
        elif label == "Convergencia":
            ej4s.set_visible(True)
            sax.set_visible(True)
            ej4t.set_visible(True)
        elif label == "Velocidad":
            ej5s.set_visible(True)
            ej5t.set_visible(True)
        elif label == "Energia":
            ej6s.set_visible(True)
            ej6t.set_visible(True)

        fig.canvas.draw_idle()

    def update_temp(ntemp):
        ej4g.clear()
        ej4s.clear()
        physics.solve_4(ej4g, ej4s, ntemp, ej4t)

    radio.on_clicked(change_view)
    slider.on_changed(update_temp)

    return ej1g, ej2g, ej3g, ej4g, ej5g, ej6g, ej1s, ej2s, ej3s, ej4s, ej5s, ej6s, radio, slider, ej2t, ej3t, ej4t, ej5t, ej6t

def display_1(v, ejg, ejs): #vector

    ejg.quiver(0, 0, 0, v[0], v[1], v[2],
            color="red",
            arrow_length_ratio=0.08)

    ejg.set_xlabel("X")
    ejg.set_ylabel("Y")
    ejg.set_zlabel("Z")

    ejg.set_title(f"Vector de Coeficietes de Calibracion\nV = ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})")

    margin = 1.2

    ejg.set_xlim(0, v[0] * margin)
    ejg.set_ylim(0, v[1] * margin)
    ejg.set_zlim(0, v[2] * margin)

    ejs.quiver(0, 0, 0, v[0], v[1], v[2],
        color="red",
        arrow_length_ratio=0.08)

    ejs.set_xlabel("X")
    ejs.set_ylabel("Y")
    ejs.set_zlabel("Z")

    ejs.set_title(f"Vector de Coeficietes de Calibracion\nV = ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})")

    margin = 1.2

    ejs.set_xlim(0, v[0] * margin)
    ejs.set_ylim(0, v[1] * margin)
    ejs.set_zlim(0, v[2] * margin)

def display_2(m, n, v, lnP, ejg, ejs, ejt):   #float, float, vector, vector
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

    datos = [[mathematics.round_22(m),mathematics.round_22(n)]]

    tabla = ejt.table(
        cellText=datos,
        colLabels=["m", "n"],
        loc="center"
    )

    ejt.text(
        0.5, 0.6,
        "f(x) = mx+n",
        transform=ejt.transAxes,
        ha="center",
        va="bottom",
        fontsize=12
    )

    for x in range(2):
        tabla[(x, 0)].set_height(0.05)
        tabla[(x, 1)].set_height(0.05)



def display_3(h_reg, t_reg, t_telemetria, altitud_cruda, ejg, ejs, ejt, poly_coef):
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

    datos = [[t, h] for t, h in zip(["C0", "C1", "C2"], [mathematics.round_22(i) for i in poly_coef])]

    tabla = ejt.table(
        cellText=datos,
        colLabels=["Cn", "Valor"],
        loc="center"
    )

    ejt.text(
        0.5, 0.65,
        "P(x) = C0 + C1x + C2x^2",
        transform=ejt.transAxes,
        ha="center",
        va="bottom",
        fontsize=12
    )

    for x in range(4):
        tabla[(x, 0)].set_height(0.05)
        tabla[(x, 1)].set_height(0.05)

def display_4(value, iteration_index, iteration_value, ejg, ejs, t, ejt):
    ejg.plot(iteration_index, iteration_value, color="purple")

    ejg.set_xlabel("Indice de iteracion")
    ejg.set_ylabel("Valor de la iteracion (segundos)")
    ejg.set_title(f"Conv. de T(t) a {t} grados \n Resultado de la convergencia = {value:.2f} s")

    ejs.plot(iteration_index, iteration_value, color="purple")

    ejs.set_xlabel("Indice de iteracion")
    ejs.set_ylabel("Valor de la iteracion (segundos)")
    ejs.set_title(f"Conv. de T(t) a {t} grados \n Resultado de la convergencia = {value:.2f} s")

    datos = [[t, f"{h:.14f}"] for t, h in zip([int(x) for x in iteration_index][0:200:2], iteration_value[0:200:2])]

    tabla = ejt.table(
        cellText=datos,
        colLabels=["Indice", "Valor de iteracion"],
        loc="center"
    )

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(12)

    for x in range(len(iteration_value[0:200:2])+1):
        tabla[(x, 0)].set_width(0.25)
        tabla[(x, 1)].set_width(0.75)

    for x in range(len(iteration_value[0:200:2])+1):
        tabla[(x, 0)].set_height(0.03)
        tabla[(x, 1)].set_height(0.03)

def display_5(tiempos, velocidades, ejg, ejs, ejt):
    ejg.plot(tiempos, velocidades, color="orange")

    ejg.set_xlabel("Tiempo (segundos)")
    ejg.set_ylabel("Veocidad (m/s)")
    ejg.set_title("Velocidad de la Sonda frente el Tiempo")

    ejs.plot(tiempos, velocidades, color="orange")
    ejs.plot(tiempos[0:200:5], velocidades[0:200:5], marker = ".", markerfacecolor = "orange", markeredgecolor = "red", linestyle = "none")

    ejs.set_xlabel("Tiempo (segundos)")
    ejs.set_ylabel("Veocidad (m/s)")
    ejs.set_title("Velocidad de la Sonda frente el Tiempo")

    datos = [[t, h] for t, h in zip([mathematics.round_22(x) for x in tiempos][0:200:5], [mathematics.round_22(x) for x in velocidades][0:200:5])]

    tabla = ejt.table(
        cellText=datos,
        colLabels=["Tiempo", "Velocidad"],
        loc="center"
    )

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(8)

    for x in range(len(tiempos[0:200:10])+1):
        tabla[(x, 0)].set_height(0.03)
        tabla[(x, 1)].set_height(0.03)

def display_6(energia, tiempo, ejg, ejs, ejt):
    ejg.plot(tiempo, energia, color="brown")

    ejg.set_xlabel("Tiempo (segundos)")
    ejg.set_ylabel("Energia (Julios)")
    ejg.set_title(f"Energia total consumida = {sum(energia)-energia[-1]:.2f} Julios")

    ejs.plot(tiempo, energia, color="brown")
    ejs.plot(tiempo[0:200:5], energia[0:200:5], marker = ".", markerfacecolor = "brown", markeredgecolor = "black", linestyle = "none")

    ejs.set_xlabel("Tiempo (segundos)")
    ejs.set_ylabel("Energia (Julios)")
    ejs.set_title(f"Energia total consumida = {sum(energia)-energia[-1]:.2f} Julios")

    datos = [[t, h] for t, h in zip([mathematics.round_22(x) for x in tiempo][0:200:5], [mathematics.round_22(x) for x in energia][0:200:5])]

    tabla = ejt.table(
        cellText=datos,
        colLabels=["Tiempo", "Energia"],
        loc="center"
    )

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(8)

    for x in range(len(tiempo[0:200:10])+1):
        tabla[(x, 0)].set_height(0.03)
        tabla[(x, 1)].set_height(0.03)

if __name__ == "__main__":
    print("hello world!")