import matplotlib.pyplot as plt

def display_results():
    plt.show()

def display_1(v): #vector
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection='3d')

    ax.quiver(0, 0, 0, v[0], v[1], v[2],
            color='red',
            arrow_length_ratio=0.15)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_title(f'Vector Resultante de Viento\nR = ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})')

    margin = 1.2

    ax.set_xlim(0, v[0] * margin)
    ax.set_ylim(0, v[1] * margin)
    ax.set_zlim(0, v[2] * margin)


if __name__ == "__main__":    #esta declaracion se usa para probar logica dentro de mathematics.py
    print("hello world!")