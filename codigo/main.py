
#*********************************************************************************
# Analisis de telemetria y Ascenso de una Sonda Meteorologica Estratosferica
#*********************************************************************************

import physics
import gui

def main():
    physics.solve()
    gui.display_results()


if __name__ == "__main__":
    main()