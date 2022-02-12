# задание 1.вариант с функцией создала, потому что на вариант с argv идет ошибка (описано ниже)
def zp():
    try:
        fam = input('Фамилия: ')
        time = float(input('Отработано часов: '))
        stavka = float(input('Ставка в час: '))
        bonus = float(input('Премия: '))
        zp = time * stavka + bonus
        print(f'{fam} к выдаче: {zp}')
    except ValueError:
        print('Ошибка. Проверьте данные.')
n = int(input('Введите количество сотрудников: '))
for i in range(0, n):
    zp()
    i +=1
#вариант 2. При "прогонке" задания выходит ошибка, как при неправильном количестве аргументов
#from sys import argv

#fam, time, stavka, bonus = argv
#try:
#    fam = input('Фамилия: ')
#    time = float(input('Отработано часов: '))
#    stavka = float(input('Ставка в час: '))
#    bonus = float(input('Премия: '))
#    zp = time * stavka + bonus
#    print(f'{fam} к выдаче: {zp}')
#except ValueError:
#    print('Ошибка. Проверьте данные.')
# >Traceback (most recent call last):
#  >File "C:\Users\Любовь и Александра\Lyubov\geek\python.git\lesson4.py", line 15, in <module>
#  >  fam, time, stavka, bonus = argv
#>ValueError: not enough values to unpack (expected 4, got 1)
#задание 2. больше предыдущего
my_list = [300, 715, 20, 14, 67]
my_biglist = [my_list[i] for i in range (0, len(my_list)) if my_list[i] > my_list[i-1]]
print(my_biglist)
# задание 3. кратность.
a_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(a_list)
# задание 4. список не повторяющихся.
a = [5, 6, 66, 4, 5, 4, 7, 19, 20, 1, 1, 1, 1, 20]
new_a = [a[i] for i in range(0, len(a)) if a.count(a[i]) == 1]
print(new_a)
# задание 5. четные 100-1000, произведение.
from functools import reduce
chet = [x for x in range(100, 1001) if x % 2 == 0]
print(chet)
def chet_func(prev_el, el):
    return prev_el * el
print(reduce(chet_func, chet))
# задание 6.
from itertools import cycle
i = 0
a = input('Введите список элементов через пробел: ').split()
b = int(input('количество повторений: '))
for el in cycle(a):
    if i > b:
        break
    else:
        print(el)
    i += 1
from itertools import count
m = int(input('Введите первое число: '))
n = int(input('Введите последнее число: '))
for el in count(m):
    if el > n:
        break
    else: print(el)
# задание 7.
import math
n = int(input('Введите целое положительное число: '))
def fact(n):
    for i in range (1, n + 1):
        yield math.factorial(i)
for el in fact(n):
    print(el)
# второй вариант без math:
n = int(input('Введите целое положительное число: '))
a = [el for el in range(1, n + 1)]
print(a)
def fact(n):
    el = 1
    for i in range(1, n + 1):
        el *= i
        yield el
for el in fact(n):
    print(el)





