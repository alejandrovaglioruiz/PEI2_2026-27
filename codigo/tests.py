import mathematics
from numpy import array, allclose

def run_test():

    # my_dot
    if mathematics.my_dot(array([1, 2, 3]), array([4, 5, 6])) == 32:
        print("my_dot                test successful")
    else:
        print("my_dot                test failed")

    # my_matrix_dot
    if (mathematics.my_matrix_dot(array([[1, 2], [3, 4]]), array([[5, 6], [7, 8]])) == array([[19, 22], [43, 50]])).all():
        print("my_matrix_dot         test successful")
    else:
        print("my_matrix_dot         test failed")

    # my_matrix_array_dot
    if (mathematics.my_matrix_array_dot(array([[1, 2], [3, 4]]), array([5, 6])) == array([17, 39])).all():
        print("my_matrix_array_dot   test successful")
    else:
        print("my_matrix_array_dot   test failed")

    # my_transpose
    if (mathematics.my_transpose(array([[1, 2, 3], [4, 5, 6]])) == array([[1, 4], [2, 5], [3, 6]])).all():
        print("my_transpose          test successful")
    else:
        print("my_transpose          test failed")

    # solve_system
    if (mathematics.solve_system(array([[2, 1], [1, 3]]), array([5, 5])) == array([2, 1])).all():
        print("solve_system          test successful")
    else:
        print("solve_system          test failed")

    # minim_cuad
    if mathematics.minim_cuad(array([1, 2, 3]), array([3, 5, 7])) == (2.0, 1.0):
        print("minim_cuad            test successful")
    else:
        print("minim_cuad            test failed")

    # find_lw_bound
    if mathematics.find_lw_bound(4, array([1, 2, 3, 4, 5])) == 3:
        print("find_lw_bound         test successful")
    else:
        print("find_lw_bound         test failed")

    # find_up_bound
    if mathematics.find_up_bound(4, array([1, 2, 3, 4, 5])) == 4:
        print("find_up_bound         test successful")
    else:
        print("find_up_bound         test failed")

    # interpolate
    h_reg, poly_coef = mathematics.interpolate(
        array([0, 1, 2]),
        array([0, 1, 2, 3]),
        array([1, 6, 17, 34])
    )

    if (abs(poly_coef - array([1, 2, 3])) < 1e-10).all():
        print("interpolate           test successful")
    else:
        print("interpolate           test failed")

    def f(x):
        return x**2

    # binary_search
    result, iteration_index, iteration_value = mathematics.binary_search(
        array([0,1,2,3,4,5,6,7,8,9,10]),
        f,
        25
    )

    if result == 5:
        print("binary_search         test successful")
    else:
        print("binary_search         test failed")

    # interpolate_velocidad
    if (mathematics.interpolate_velocidad(
        array([0, 1, 2, 3]),
        array([0, 2, 4, 6])
    ) == array([2, 2, 2, 2])).all():
        print("interpolate_velocidad test successful")
    else:
        print("interpolate_velocidad test failed")


    # calc_energy
    energias = mathematics.calc_energy(
            array([0, 1, 2]),
            array([1, 1, 1])
        )
    
    if mathematics.round_22(sum(energias)-energias[-1]) == 10.24:
        print("calc_energy           test successful")
    else:
        print("calc_energy           test failed")

    # round_22
    if mathematics.round_22(3.14159) == 3.14:
        print("round_22              test successful")
    else:
        print("round_22              test failed")


if __name__ == "__main__":    #esta declaracion se usa para probar logica dentro de mathematics.py
    run_test()