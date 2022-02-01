#задание 1. типы элементов списка.
a = [3, None, 'g', 'mama', 412]
for i in a:
    print(type(i))
# задание 2. обмен значений соседних элементов.
b = input('Введите список значений через пробел: ').split()
for i in range(0, len(b) - 1,2):
    b[i], b[i+1] = b[i+1], b[i]
print(b)
# задание 3. через list
my_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
c = int(input('Введите номер месяца от 1 до 12: '))
i = my_list.index(c)
if i < 3:
    print('зима')
elif 3 <= i < 6:
    print('весна')
elif 6 <= i < 9:
    print('лето')
else:
    print('осень')
# задание 3 через dict
#c = int(input('Введите номер месяца от 1 до 12: '))
#my_dict = dict(зима = 1, весна = 3, лето = 6, осень = 9)
#print(my_dict.get('1'))
#print(my_dict.get(c))