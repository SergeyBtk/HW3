from random import randint
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

lenght = 250 #введите длину списка
number = 5
number_new = number
number_el_list = 0
list_1 = []
i = 0
while i < lenght:
    item = randint(1, 100)
    list_1.insert(-1, item)
    i += 1
    if number == item:
        number_el_list += 1
        list_sort = list_1.sort()
if list_1.count(number) == 0:
    while (list_1.count(number_new) == 0):
        number_new += 1
        print(number_new)
        print(f'число {number} встречается {number_el_list} раз, ближайшее число: {number_new}')
else:
    print(f'число {number} встречается {number_el_list} раз.')





# if list_1.count(number) == 0:
#     while (list_1.count(number_new) == 0):
#         number_new += 1
#         print(number_new)
# print(f'число {number} встречается {number_el_list} раз, ближайшее число: {number_new}')


