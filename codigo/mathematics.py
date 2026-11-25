from numpy import array, vstack, delete, append, mean, where, zeros

def my_dot (A, X):        #vector, vector
    return sum(A[i]*X[i] for i in range (len(A)))

def matrix_dot (A, B):          #matrix, matrix
    return array([[my_dot(A[i, :],B[:, j]) for j in range (len(B[0]))] for i in range (len(A))])

def matrix_array_dot (A, B):    #matrix, vector
    return array([my_dot(A[i,:],B) for i in range (len(A))])

def transpose(A):
    return array([list(row) for row in zip(*A)])

def solve_system(A, b):   #matrix, vector
    B = A.astype(float).copy()  #esto se hace para evitar que la funcion modifique la variable global
    v = b.astype(float).copy()

    Filas = len(B)
    Columnas = len(B[0])

    solution = array([0.0]*Columnas)

    for c in range(Columnas):
        for f in range(Filas):
            if not(all(B[c:,c] == 0)):    #evitar division por cero
                if f > c:
                    while B[c,c] == 0:
                        B = vstack((B, B[c,:]))
                        B = delete(B, c, axis=0)
                        v = append(v, v[c])
                        v = delete(v, c)
                    v[f] = v[f] - (v[c]*(B[f,c]/B[c,c]))
                    B[f,:] = B[f,:] - (B[c,:]* (B[f,c]/B[c,c]))

    for c in range(Columnas):
        for f in range(Filas):
            if f < c:
                v[f] = v[f] - (v[c]*(B[f,c]/B[c,c]))
                B[f,:] = B[f,:] - (B[c,:] * (B[f,c]/B[c,c]))

    for f in range(Filas):
        solution[f] = v[f]/B[f,f]

    return solution

def minim_cuad(v, u):   #vector, vector

    m = ((len(v)*(my_dot(v, u)))-(sum(v)*sum(u)))/(((len(v))*(my_dot(v,v)))-(sum(v)**2))

    n = mean(u) - m*mean(v)

    return m, n

def find_lw_bound(value, vector):   #float, vector
    for i in vector[::-1]:
        if i < value:
            return i

def find_up_bound(value, vector):   #float, vector
    for i in vector:
        if i >= value:
            return i

#***********************************************************************************************************************************************
def interpolate(t_reg, t_crud, a_crud): #vector, vector, vector
    h_reg = []
    A = zeros((len(t_crud), 3))

    for x in range(len(t_crud)):
        A[x,:] = [1, t_crud[x], t_crud[x]**2]

    At = transpose(A)
    poly_coef = solve_system(matrix_dot(At, A), matrix_array_dot(At, a_crud))

    for t in range(len(t_reg)):
        h_reg.append(poly_coef[0] + (poly_coef[1]*t_reg[t]) + (poly_coef[2]*(t_reg[t]**2)))

    return h_reg, poly_coef


#***********************************************************************************************************************************************

def binary_search(range, f, target):        #vector, float, float
    lw_bnd = range[0]
    up_bnd = range[-1]
    mid = (lw_bnd+up_bnd)/2
    iteration_index = [1]
    iteration_value = [mid]
    buffer = mid - 1

    while True:
        if buffer == mid:                                       #La estructura de IFs esta hecha para que el algoritmo funcione con funciones de pendiente negativa al igual que positiva
            return mid, iteration_index, iteration_value
        elif f(mid) < target and f(mid) < f(mid + 1):
            lw_bnd = mid
            buffer = mid
            mid = (lw_bnd+up_bnd)/2
            iteration_index.append(iteration_index[-1]+1)
            iteration_value.append(mid) 
        elif f(mid) > target and f(mid) < f(mid + 1):
            up_bnd = mid
            buffer = mid
            mid = (lw_bnd+up_bnd)/2 
            iteration_index.append(iteration_index[-1]+1)
            iteration_value.append(mid)
        elif f(mid) < target and f(mid) > f(mid + 1):
            up_bnd = mid
            buffer = mid
            mid = (lw_bnd+up_bnd)/2 
            iteration_index.append(iteration_index[-1]+1)
            iteration_value.append(mid)
        elif f(mid) > target and f(mid) > f(mid + 1):
            lw_bnd = mid
            buffer = mid
            mid = (lw_bnd+up_bnd)/2 
            iteration_index.append(iteration_index[-1]+1)
            iteration_value.append(mid)

def interpolate_velocidad(t_reg, h_reg): #vector, vector, vector
    velocidad = []

    for t in range  (len(t_reg)):
        if t == 0:              #esto es necesario para que no haya un error al calcular las bandas inferiores y superiores
            up = t+2
            lw = t
        elif t == (len(t_reg) - 1):
            up = t
            lw = t-2
        else:
            up = t + 1
            lw = t - 1
        velocidad.append((h_reg[up]-h_reg[lw])/(2*(t_reg[up]-t_reg[lw])))

    return array(velocidad)      

def calc_energy(tiempo, velocidad):     #vector, vector
    potencia = []
    energias = []
    energia = 0
    
    for t in range (len(tiempo)):
        potencia.append(5+abs(velocidad[t])*0.1+(tiempo[t])*0.02)

    for t in range (len(tiempo)):
        if t == (len(tiempo) - 1):
            energia = energias[-1]
        else:
            energia = ((potencia[t]+potencia[t+1])/2)*(tiempo[t+1] - tiempo[t])
        energias.append(energia)

    return(energias)

def round_22 (x): #float
    return (int(x*100))/100

if __name__ == "__main__":    #esta declaracion se usa para probar logica dentro de mathematics.py
    print(solve_system(array([[1,2,3],
                              [4,5,6],
                              [7,8,10]]), 
                       array([3,2,1])))