# Решить систему линейных уравнений:
# x + y + z = 62
# x + 5y - z = -4
# 2x - y + 3z = 27
# 1 1 1 6
# 2 5 -1 -4
# 2 -1 3 27
# AX = b
# inv(A)AX = inv(A)b
# EX = inv(A)b
# X = inv(A)b

import numpy as np

# Матрица коэффициентов A
A = np.array([[1, 1, 1],
              [1, 5, -1],
              [2, -1, 3]])

# Вектор правой части b
b = np.array([62, -4, 27])

# Решение системы
x = np.linalg.solve(A, b)

print("Решение системы:")
print("x =", x[0])
print("y =", x[1])
print("z =", x[2])
