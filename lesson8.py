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
today = Data('17 - 8 - 2015')
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
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - не число")
                stop = input(f'для окончания введите stop, для продолжения нажимайте Enter: ')

                if stop != 'stop':
                    print(try_except.my_input())
                elif stop == 'stop':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())

# задание 4.
