# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.numbers])

    def __add__(self, other):
        return Matrix([(self.numbers[i][j] + other.numbers[i][j] for j in range(len(other.numbers)))
                       for i in range(len(self.numbers))])


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
print(m_1)
print(m_2)
print(m_1 + m_2)

# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return f'Оющий расход ткани для пошива изделий составляет: {self.consumption + other.consumption} м.'


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Расход ткани для пошива пальто составляет {self.consumption} м.'


men_coat = Coat(38)
print(men_coat)


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        return round(2 * self.height + 0.3, 2)

    def __str__(self):
        return f'Расход ткани для пошива костюма составляет {self.consumption} м.'


men_suit = Suit(1.9)
print(men_suit)
print(men_coat + men_suit)
print(men_coat.consumption + men_suit.consumption)

# 3)Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.


class Cell:

    def __init__(self, partition):
        self.partition = partition

    def __str__(self):
        return f'В клетке содержится {self.partition} ячеек/й(ки/ка)'

    def __add__(self, other):
        return f'{Cell(self.partition + other.partition)} при сложении.'

    def __sub__(self, other):
        if self.partition > other.partition:
            return f'{Cell(self.partition - other.partition)} при вычитании.'
        else:
            return 'Первая клетка меньше второй, надо попробовать вычесть наоборот!'

    def __mul__(self, other):
        return f'{Cell(self.partition * other.partition)} при умножении.'

    def __truediv__(self, other):
        try:
            return f'{Cell(self.partition // other.partition)} при делении.'
        except ZeroDivisionError:
            return 'Деление на ноль!'

    def make_order(self, sep):
        for i in range(self.partition // sep):
            print(sep * '*')
        print((self.partition % sep) * '*')


cell_1 = Cell(11)
cell_2 = Cell(4)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 / cell_2)
cell_1.make_order(5)
cell_2.make_order(4)