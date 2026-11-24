
#*********************************************************************************
# Analisis de telemetria y Ascenso de una Sonda Meteorologica Estratosferica
#*********************************************************************************

import physics
import gui

def main():
    ej1, ej2 = gui.crea_ejes()
    physics.solve(ej1, ej2)
    gui.display_results()


if __name__ == "__main__":
    main()