from numpy import array, vstack, delete, append

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

if __name__ == "__main__":    #esta declaracion se usa para probar logica dentro de mathematics.py
    print(solve_system(array([[1,2,3],
                              [4,5,6],
                              [7,8,10]]), 
                       array([3,2,1])))