
#*********************************************************************************
# Analisis de telemetria y Ascenso de una Sonda Meteorologica Estratosferica
#*********************************************************************************

import physics
import gui

def main():
    ej1g, ej2g, ej3g, ej4g, ej5g, ej6g, ej1s, ej2s, ej3s, ej4s, ej5s, ej6s, radio, slider = gui.crea_ejes()
    physics.solve(ej1g, ej2g, ej3g, ej4g, ej5g, ej6g, ej1s, ej2s, ej3s, ej4s, ej5s, ej6s, -10)
    gui.display_results(radio, slider)


if __name__ == "__main__":
    main()