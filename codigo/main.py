
#*********************************************************************************
# Analisis de telemetria y Ascenso de una Sonda Meteorologica Estratosferica
#*********************************************************************************

import codigo.physics as physics
import codigo.gui as gui
import codigo.mathematics as mathematics



def main():
    physics.solve()
    gui.display_results()


if __name__ == "__main__":
    main()