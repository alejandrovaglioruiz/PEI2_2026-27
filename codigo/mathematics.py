from numpy import array, vstack, delete, append, mean, where

def my_dot (A, X):        #vector, vector
    return sum(A[i]*X[i] for i in range (len(A)))

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

def interpolate(t_reg, t_crud, a_crud): #vector, vector, vector
    h_reg = []

    for t in t_reg:
        if t == t_crud[0]:              #esto es necesario para que no haya un error al calcular las bandas inferiores y superiores
            up = find_up_bound(t+0.00000000001, t_crud)
            lw = find_lw_bound(t+0.00000000001, t_crud)
        else:
            up = find_up_bound(t, t_crud)
            lw = find_lw_bound(t, t_crud)
        h_reg.append(a_crud[where(t_crud==lw)]+((t-lw)/(up-lw))*(a_crud[where(t_crud==up)]-a_crud[where(t_crud==lw)]))

    return array(h_reg)

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
            
        
if __name__ == "__main__":    #esta declaracion se usa para probar logica dentro de mathematics.py
    print(solve_system(array([[1,2,3],
                              [4,5,6],
                              [7,8,10]]), 
                       array([3,2,1])))