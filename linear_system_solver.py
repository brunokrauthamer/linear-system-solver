def linear_system(matrix, array):
    system_len = len(matrix)
    for idx_global_equation in range(1, system_len):
        # print('primeiro for')
        # print('idx_global_equation', idx_global_equation)
        for idx_equation in range(idx_global_equation, system_len):
            # print('segundo for')
            # print('idx_equation', idx_equation)
            # print(f'multiplier = matrix[{idx_equation}][{idx_global_equation - 1}] / matrix[{idx_global_equation - 1}][{idx_global_equation - 1}]')
            multiplier = matrix[idx_equation][idx_global_equation - 1] / matrix[idx_global_equation - 1][idx_global_equation - 1]
            # print('multiplier', multiplier)
            array[idx_equation] = array[idx_equation] - multiplier * array[idx_global_equation - 1]
            # print(f'array[{idx_equation}] = array[{idx_equation}] - {multiplier} * array[{idx_global_equation - 1}]')
            # print('array', array)
            for index, element in enumerate(matrix[idx_equation]):
                # print('terceiro for')
                # print(f'matrix[{idx_equation}][{index}] = {element} - {multiplier} * matrix[{idx_global_equation - 1}][{index}]')
                matrix[idx_equation][index] = element - multiplier * matrix[idx_global_equation - 1][index]

    matrix.reverse()

    for coefs in matrix:
        coefs.reverse()
    
    array.reverse()
    answer = []

    for _ in array:
        answer.append(0)
    
    for idx, element in enumerate(array):
        result = element
        for i_coef, coef in enumerate(matrix[idx]):
            if i_coef != idx:
                result -= coef * answer[i_coef]
        if matrix[idx][idx] == 0:
            if result == 0:
                return 'Sistema possível e indeterminado'
            return 'Sistema impossível'
        result = result / matrix[idx][idx]
        answer[idx] = round(result, 3)
    
    answer.reverse()
    return answer

matrix1 = [[1, 2, -1],[2, -1, 1], [1, 1, 1]]

array1 = [2, 3, 6]

print(linear_system(matrix1, array1))

matrix2 = [[1, 2, 1], [0, 3, -1], [0, 0, 2]]
array2 = [4, 5, 2]

print(linear_system(matrix2, array2))

matrix3 = [[1, 2, -1], [3, -1, 1], [2, 2, 3]]
array3 = [3, 1, -4]

print(linear_system(matrix3, array3))

matrix4 = [[2, 1, 1, 1, 9, -2], [1321, 2, 1, 1, 16, 13], [1, 1, 2, 1, 31, -321], [1, 1, 1, 2, -231, 7], [1321, 13, 11, 23, -2231, 711], [13, 133, 113, 2321, -231, 711]]
array4 = [1, -999999992, 3, 4, 12, 88880]

print(linear_system(matrix4, array4))

matrix5 = [[1, 2], [2, 4]]
array5 = [4, 8]

print(linear_system(matrix5, array5))

matrix6 = [[1, 2], [2, 4]]
array6 = [4, 9]

print(linear_system(matrix6, array6))

matrix7 = [[1, 1, 1], [3/4, -2/3, 0], [1/2, -1/3, -1]]
array7 = [900, 0, 0]

print(linear_system(matrix7, array7))