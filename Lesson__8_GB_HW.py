# 1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self):
        self.my_date = '31-12-2020'

    @classmethod
    def make_num(cls):
        new_list = [int(i) for i in Date().my_date.split('-')]
        return Date.valid_date(new_list)

    @staticmethod
    def valid_date(param):
        if param[0] > 31 or param[0] < 1 or param[1] > 12 or param[1] < 1 or param[2] > 2020 or param[2] < 1990:
            return f'Неверно указана дата, проверьте число, месяц и год!'
        else:
            return f'Шел {param[0]} день {param[1]} месяца {param[2]} года...'


print(Date.make_num())

# 2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    inp_data = (input('Введите числа через пробел для получения результата деления: ')).split()
    if int(inp_data[1]) == 0:
        raise OwnError('На ноль делить нельзя!!!')
except ValueError:
    print('Надо ввести число!!!')
except IndexError:
    print('Необходимо ввести 2 числа!!!')
except OwnError as err:
    print(err)
else:
    print(f'Результат деления: {round(int(inp_data[0]) / int(inp_data[1]), 2)}')


# 3) Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        num = input('Введите число или stop для завершения программы: ')
        if num == 'stop':
            print(f'Список введенных чисел: {my_list}')
            break
        if not num.isdigit():
            raise OwnError('Это не число! Попробуйте еще раз!')
    except OwnError as err:
        print(err)
    else:
        my_list.append(int(num))

# 4, 5, 6) Проект «Склад оргтехники»:


class Storage:
    def __init__(self):
        self.total = []
        self.dep = ['Отдел продаж', 'Транспортный отдел', 'Бухгалтерия']
        self.dep_res = {}

    def storage_info(self, *units):
        for unit in units:
            self.total.append(unit)
        return f'\nВсего на складе на данный момент: {self.total}'

    def department(self, num_1, num_2, num_3):
        self.dep_res = dict(zip(self.dep, [num_1, num_2, num_3]))
        return self.dep_res


class OfficeEq:
    def __init__(self, number):
        self.title = None
        self.number = number
        self.res = {}

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if number < 0:
            self.__number = 0
        else:
            self.__number = number

    def total_quantity(self):
        self.res.update({self.title: self.number})
        return self.res


class Printer(OfficeEq):
    def __init__(self, number):
        super().__init__(number)
        self.title = 'Принтер'

    def __add__(self, other):
        return Printer(self.number + other.number)

    def __sub__(self, other):
        return Printer(self.number - other.number)


class Scanner(OfficeEq):
    def __init__(self, number):
        super().__init__(number)
        self.title = 'Сканер'

    def __add__(self, other):
        return Scanner(self.number + other.number)

    def __sub__(self, other):
        return Scanner(self.number - other.number)


class Xerox(OfficeEq):
    def __init__(self, number):
        super().__init__(number)
        self.title = 'Ксерокс'

    def __add__(self, other):
        return Xerox(self.number + other.number)

    def __sub__(self, other):
        return Xerox(self.number - other.number)


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


storage = Storage()


def storage_moving(class_name, name):
    print(f'\n________{name.upper()}________')
    while True:
        try:
            p_1 = class_name(int(input('Укажите кол-во позиций для передачи на склад: ')))
            moved_unit = storage.department(abs(int(input('Сколько передать в Отдел продаж: '))),
                                     abs(int(input('В Транспортный отдел: '))), abs(int(input('В Бухгалтерию: '))))
            p_2 = class_name(sum(storage.dep_res.values()))
            p_3 = p_1 - p_2
            if p_1.number < p_2.number:
                raise OwnError(f'На складе не будет столько {name}ов!!! Попробуйте еще раз!')

        except ValueError:
            print('Необходимо ввести целое положительное число! Попробуйте еще раз с начала!')
        except OwnError as err:
            print(err)

        else:
            print(f'Передано в отделы: {moved_unit}')
            print(f'Всего остаток на складе: {p_3.total_quantity()}')
            return p_3.total_quantity()


print(storage.storage_info(storage_moving(Printer, 'Принтер'), storage_moving(Scanner, 'Сканер'),
                           storage_moving(Xerox, 'Ксерокс')))

# 7) Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:

    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return ComplexNumber(self.number_1 + other.number_1, self.number_2 + other.number_2)

    def __mul__(self, other):
        return ComplexNumber(self.number_1 * other.number_1 - self.number_2 * other.number_2,
                             self.number_1 * other.number_2 + self.number_2 * other.number_1)

    def __str__(self):
        return f'Получилось комплексное число {self.number_1}+{self.number_2}j.'


num = ComplexNumber(5, 8)
num_1 = ComplexNumber(2, 9)
print(num + num_1)
print(num * num_1)
print()
print(num)
