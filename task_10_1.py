"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join([''.join([str(f'{el:4}') for el in i]) for i in self.matrix]))

    def __add__(self, other):
        print('*' * 15)
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = self.matrix[x][y] + other.matrix[x][y]
        return self


first_m = Matrix(
    [[25, 10, 19, 45, 3],
     [47, 57, 9, 58, 53],
     [-5, 4, -83, 36, 87],
     [8, 72, -46, 3, -43]])

second_m = Matrix(
    [[-12, 60, 22, -36, 5],
     [-72, 12, 4, -44, 12],
     [50, -4, 72, -80, -95],
     [29, -25, 34, 23, 56]])

print(first_m + second_m)
