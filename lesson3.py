# задание 1. частное
def my_div(arg_1, arg_2):
    return arg_1 / arg_2
arg_1 = int(input('Введите делимое: '))
arg_2 = int(input('Введите делитель: '))
if arg_2 == 0:
    print('На ноль делить нельзя!')
    arg_2 = int(input('Введите делитель: '))
print(my_div(arg_1, arg_2))
# задание 2.
def f_sved(*args):
    return args
name = input('Введите Ваше имя: ')
fam = input('Введите Вашу фамилию: ')
year = input('Год Вашего рождения: ')
city = input('Город проживания: ')#
mail = input('Ваш e-mail: ')
tel = input('Номер телефона в международном формате: ')
f_sved(name, fam, year, city, mail, tel)
print(f_sved(name, fam, year, city, mail, tel))
# задание 3. сумма максимальных двух (пока не задала начальный num = 0 не хотело работать ни разу)
num = 0
def my_func(num):
    f_list = []
    i = 0
    for i in range(0, 3, 1):
        el = int(input('Введите число: '))
        f_list.append(el)
        i += 1
    f_list.sort()
    num = f_list[1] + f_list[2]
    return num
print(my_func(num))
# задание 4. степень
def my_func(x, y):
    return x ** y
x = int(input('Введите положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(my_func(x, y))
# задание 4 вариант без **
def my_func(x, y):
    z = abs(y)
    s = x
    for i in range(1, z, 1) :
        s = s * x
        i += 1
    div = 1 / s
    return div
x = int(input('Введите положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(my_func(x, y))
# задание 5.
b = 0
def slogenie(b):
    a = input('Введите числа через пробел. Для остановки ввода нажмите n: ').split()
    #b = slogenie(b)
    for el in a:
        if el == 'n':
            print('Задача окончена. Сумма чисел:')
            break
        else:
            el = int(el)
            b = b + el
    return b
    print(b)
i = 0
while i != 'n':
    i = input('Продолжаем вводить числа? y - да, n - нет: ')
    if i != 'n':
        print(slogenie(b))
    else:
  #  print(b)
    #i = input('Для выхода из задачи нажмите "n", для продолжения - любую клавишу:')
        print('Алексей, осталось проверить 2 задания.') #здесь могло быть любое прощание


# задание 6.
word = input('Введите слово на латинице маленькими буквами: ')
def int_func(word):
    word2 = word.title()
    return word2
print(int_func(word))
# задание 7.
word = input('Введите фразу на латинице маленькими буквами: ')
print(int_func(word))
