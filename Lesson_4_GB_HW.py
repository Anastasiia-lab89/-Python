# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В
# расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv


def my_func(hours, hour_rate, bonus):
    try:
        return int(hours) * int(hour_rate) + int(bonus)
    except ValueError:
        print('Необходимо ввести число!')


try:
    print(f'З/плата сотрудника будет равна: {my_func(argv[1], argv[2], argv[3])}')
except IndexError:
    print('Необходимо ввести 3 параметра: выработка в часах, ставку в час, премию')

# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.

my_list = [num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0]
print(my_list)

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import functools

my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(functools.reduce(lambda prev_el, el: prev_el * el, my_list))


# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# ------------------------------а-------------------------------
from itertools import count, cycle, islice
user_min = int(input('Введите минимальное число: '))
user_max = int(input('Введите максимальное число: '))

for i in islice(count(user_min), (user_max - user_min) + 1):
    print(i)
# -----------------------------б---------------------------------
my_str = input('Введите данные через пробел: ').split()

for i in islice(cycle(my_str), 10):
    print(i)

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


for el in fact(7):
    print(el)