"""Задание 3.

Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки
арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.

"""


class Cell:
    def __init__(self, quantity_cells):
        self.quantity_cells = int(quantity_cells)

    def __str__(self):
        return str(self.quantity_cells)

    def __add__(self, other):
        self.quantity_cells += other.quantity_cells
        return self.__str__()

    def __sub__(self, other):
        sub = self.quantity_cells - other.quantity_cells
        if sub > 0:
            self.quantity_cells = sub
            return self.__str__()
        else:
            return 'разность меньше нуля!'

    def __mul__(self, other):
        self.quantity_cells *= other.quantity_cells
        return self.__str__()

    def __truediv__(self, other):
        self.quantity_cells //= other.quantity_cells
        return self.__str__()

    def make_order(self, quantity_cells_in_row):
        make_order = ''
        for el in range(1, self.quantity_cells + 1):
            make_order += '*' if el % quantity_cells_in_row != 0 else '*\n'
        return make_order


cell = Cell(23)
cell2 = Cell(32)

print(cell - cell2)
print(cell + cell2)
print(cell / cell2)
print(cell * cell2)

print(cell.make_order(10))
