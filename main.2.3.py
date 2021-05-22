# 3. Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся вложенный список. Для
# объектов
# класса реализовать метод сложения и вычитания матриц, а также умножения, деления матрицы на число и user-friendly
# вывода
# матрицы на экран.
import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, num):
        len1 = len(self.matrix) - 1
        while len1 >= 0:
            len2 = len(self.matrix[len1]) - 1
            while len2 >= 0:
                self.matrix[len1][len2] += num
                len2 -= 1
            len1 -= 1
        return np.array(self.matrix)

    def __sub__(self, num):
        len1 = len(self.matrix) - 1
        while len1 >= 0:
            len2 = len(self.matrix[len1]) - 1
            while len2 >= 0:
                self.matrix[len1][len2] -= num
                len2 -= 1
            len1 -= 1
        return np.array(self.matrix)

    def __mul__(self, num):
        len1 = len(self.matrix) - 1
        while len1 >= 0:
            len2 = len(self.matrix[len1]) - 1
            while len2 >= 0:
                self.matrix[len1][len2] *= num
                len2 -= 1
            len1 -= 1
        return np.array(self.matrix)

    def __truediv__(self, num):
        len1 = len(self.matrix) - 1
        while len1 >= 0:
            len2 = len(self.matrix[len1]) - 1
            while len2 >= 0:
                self.matrix[len1][len2] /= num
                len2 -= 1
            len1 -= 1
        return np.array(self.matrix)


matrix1 = ([10, 20, 30], [20, 30, 40], [60, 60, 30])
qwe = Matrix(matrix1)
print(qwe / 2)
print(qwe * 2)
