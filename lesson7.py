#задание 1.
class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
    def __add__(self):
        matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

my_matrix = Matrix([[1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3]],
                   [[4, 5, 6],
                    [4, 5, 6],
                    [4, 5, 6]])

print(my_matrix.__add__())
#задание 2.
from abc import ABC, abstractmethod
class Dress(ABC):
    def __init__(self, param):
        self.param = param
    @abstractmethod
    def expense(self):
        pass
    def __str__(self):
        return str(self.param)

class Coat(Dress):
    @property
    def expense(self):
        return self.param / 6.5 + 0.5

class Costume(Dress):
    @property
    def expense(self):
        return self.param * 2 + 0.3

coat = Coat(42)
costume = Costume(1.56)
print(coat)
print(costume)
print('Расход ткани на пальто: {:.2f}'. format(coat.expense))
print('Расход ткани на костюм: {:.2f}'. format(costume.expense))
print('Общий расход ткани: {:.2f}'. format(float(coat.expense) + float(costume.expense)))


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_series):
        series = ''
        for i in range(int(self.quantity / cells_series)):
            series += f'{"*" * cells_series} \\n'
        series += f'{"*" * (self.quantity % cells_series)}'
        return series

cells1 = Cell(33)
cells2 = Cell(9)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)