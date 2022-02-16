# задание 1.
my_f = open('text1.txt', 'w')
str_list = input('Введите текст \n')
while str_list:
    my_f.writelines(str_list)
    str_list = input('Введите текст \n')
    my_f.writelines('\n')
    if not str_list:
        break
my_f.close()
my_f = open('text1.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

# задание 2.
my_file = open('text.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file.close()
my_file = open('text.txt', 'r')
content = my_file.readlines()
print(f'Количество строк - {len(content)}')
my_file.close()
my_file = open('text.txt', 'r')
for line in my_file:
    line = line.split()
    print(len(line))
my_file.close()
# задание 3.
with open('zp.txt', 'r', encoding="utf-8") as my_file:
    zp = []
    poor = []
    my_list = my_file.readlines()
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        zp.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, zp)) / len(zp)}')
# задание 4.
my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(my_dict[i[0]] + '  ' + i[1])
    print(new_file)
with open('text4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

# задание 5.
def summary():
    with open('text5.txt', 'w+') as file_obj:
        line = input('Введите цифры через пробел \n')
        file_obj.writelines(line)
        my_numb = line.split()
        print(f'Сумма = {sum(map(int, my_numb))}')
summary()
# задание 6.
import re
subj = {}
with open("text6.txt", "r", encoding="utf-8" ) as my_file:
    for line in my_file:
        subject, lecture, practice, lab = line.split()
        num = re.findall(r'\d+', line)
        num = [int(i) for i in num]
        subj.update({subject : sum(num)})
    print(subj)
# задание 7.
import json
with open("firm.txt", "r", encoding="utf-8" ) as my_file:
    a = []
    ave_dict = {}
    firm_dict = {}
    for line in my_file:
        firm, form, profit, damage = line.split()
        rich = int(profit) - int(damage)
        if rich >=0:
            a.append(rich)
            n = sum(a) / len(a)
        firm_dict.update({firm : rich})
    ave_dict.update({'average_profit' : n})
    firm_list = [firm_dict, ave_dict]
    print(firm_list)
with open('firm.json', 'w') as write_js:
    json.dump(firm_list, write_js)

    js_str = json.dumps(firm_list)
    print(f'Создан файл с расширением json со данными о состоянии фирм: \n '
          f' {js_str}')