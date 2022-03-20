# 7
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + i * b'

    def __add__(self, other):
        print(f'Сумма равна')
        return f'z = {self.a + other.a} + {self.b + other.b}'

    def __mul__(self, other):
        print(f'Произведение равно')
        return f'z = {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}'

    def __str__(self):
        return f'z = {self.a} + i * {self.b}'

z_1 = ComplexNumber(2, -2)
z_2 = ComplexNumber(4, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)

# задание 1.
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'
today = Data('20 - 03 - 2022')
print(today)
print(Data.valid(12, 5, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('4 - 4 - 2004'))
print(Data.valid(1, 11, 2000))

# задание 2.
class OwnErrorZero(Exception):
    def __init__(self, txt):
        self.txt = txt

a = float(input('введите делимое: '))
b = float(input('введите делитель: '))
try:
    if b == 0:
        raise OwnErrorZero("На ноль делить нельзя")
except OwnErrorZero as err:
    print(err)
else:
   print(f'частное: {a / b}')
finally:
    print("Программа завершена")
# задание 3.
class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        for i in range(n):
            try:
                val = int(input('Введите значения и нажимайте Enter: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list}')
            except:
                print(f"Недопустимое значение - не число")
                stop = input(f'для окончания введите stop, для продолжения нажимайте Enter: ')
                if stop != 'stop':
                    print(try_except.my_input())
                else:
                    return f'Вы вышли'
                break

try_except = Error(1)
n = int(input('Какое количество элементов списке? '))
print(try_except.my_input())

# задание 4,5,6:
class StoreMashines:
    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store_printer = []
        self.my_store_scaner = []
        self.my_store_copier = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            i = 0
            number = int(input('Определите количество наименований техники: '))
            for i in range(0, number):
                unit_t = input('Определите тип устройства: p - принтер, s - сканер, с - копир: ')
                if unit_t == 'p':
                    unit = input(f'Введите наименование ')
                    unit_p = int(input(f'Введите цену за ед '))
                    unit_q = int(input(f'Введите количество '))
                    unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
                    self.my_store_printer.append(unique)
                    self.my_store_full.append(unique)
                    print(f' {self.my_store_printer}, {self.my_store_full}')
                    i += 1

                elif unit_t == 's':
                    unit = input(f'Введите наименование ')
                    unit_p = int(input(f'Введите цену за ед '))
                    unit_q = int(input(f'Введите количество '))
                    unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
                    self.my_store_scaner.append(unique)
                    self.my_store_full.append(unique)
                    print(f'Склад сканеров: {self.my_store_scaner}, Общий склад: {self.my_store_full}')
                    i += 1
                elif unit_t == 'c':
                    unit = input(f'Введите наименование ')
                    unit_p = int(input(f'Введите цену за ед '))
                    unit_q = int(input(f'Введите количество '))
                    unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
                    self.my_store_copier.append(unique)
                    self.my_store_full.append(unique)
                    print(f'Склад копиров: {self.my_store_copier}, Общий склад: {self.my_store_full}')
                    i += 1
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            print(f'Весь склад -\n {self.my_store_full}')
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'

unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_1.to_print())
print(unit_3.to_copier())