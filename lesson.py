#задание 1.
name = input('Как Вас зовут?  ')
print('Рады Вам, %s!' % name)
a = int(input('Сколько Вам лет?  '))
b = a + 5
print('Через пять лет Вам будет  %d' % b)
#задание 2.
vr = int(input('Введите время в секундах: '))

#задание 3. не было указано вывести результат на экран.
# сделала это опционально. можно убрать print(b) и будет секрет.
c = int(input('Введите целое число от 1 до 9: '))
s = c * 3 + c * 20 + c * 100
print(s)
#задание 4. наибольшая цифра. печать также не оговорена тз
#задание 5. в условии нет варианта равенства выручки и прибыли, добавлено опционально
vir = float(input('Введите сумму выручки: '))
zatrata = float(input('Введите сумму издержек: '))
if vir > zatrata:
    print('Ваша фирма работает с прибылью. Поздравляем!')
    renta = (vir-zatrata) / vir
    print('Рентабельность выручки составила: %.2f' % renta)
    sotr = int(input('Введите количество сотрудников: '))
    m = (vir - zatrata) / sotr
    print('Прибыль фирмы на одного сотрудника составила: %.2f' % m )
elif vir < zatrata:
    print("Ваша фирма несёт убытки.")
else:
    print('Ваша фирма не принесла доход, но и убытков нет.')


