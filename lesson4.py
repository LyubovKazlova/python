#задание 2. больше предыдущего
my_list = [300, 715, 20, 14, 67]
my_biglist = [my_list[i] for i in range (0, len(my_list)) if my_list[i] > my_list[i-1]]
print(my_biglist)
# задание 3. кратность. сделано
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



# задание 1
#from my_func import zp
#import sys
#fam = input('Фамилия: ')
#hour = input('Отработано часов: ')
#stavka = input('Ставка в час: ')
#bonus = input('Премия: ')
#print(zp(hour), (stavka), (bonus))


