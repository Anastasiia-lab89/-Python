# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:

    def __init__(self, color_1, color_2, color_3):
        self.__color = [color_1, color_2, color_3]

    def running(self):
        if self.__color == ['красный', 'желтый', 'зеленый']:
            print('Ура, светофор начал работать!')
            while True:
                print(f'\r\033[41m\033[30m{self.__color[0]}\033[0m', end='')
                sleep(7)
                print(f'\r\033[43m\033[30m{self.__color[1]}\033[0m', end='')
                sleep(2)
                print(f'\r\033[42m\033[30m{self.__color[2]}\033[0m', end='')
                sleep(7)
                print(f'\r\033[43m\033[30m{self.__color[1]}\033[0m', end='')
                sleep(2)
        else:
            print('Цвета указаны неправильно! Светофор не работает!')


lights = TrafficLight((input('Введите запрещающий цвет сфетофора: ').lower()),
                      (input('Введите предупреждающий цвет сфетофора: ')).lower(),
                      (input('Введите разрешающий цвет сфетофора: ').lower()))
lights.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Для покрытия дорожного поплотна тербутся {round((length * width * 25 * 5) / 1000):,}т асфальта.')


south_road = Road(20, 5000)
print(south_road._length)
print(south_road._width)

# 3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": salary, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f'Доход с учетом премии составляет {self._income["salary"] + self._income["bonus"]:,}')


purchase_manager = Position('Александр', "Иванов", 'менеджер по закупкам', 50000, 2500)
purchase_manager.get_full_name()
purchase_manager.get_total_income()
print(purchase_manager._income)
print(purchase_manager.surname)

# 4) Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import random


class Car:
    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False
        print(f'Название автомобиля: {name}\nЦвет: {color}\nМаксимальная скорость автомобиля: {speed} км/ч')

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self):
        print(random.choice(['Поворачивает налево', 'Поворачевает направо', 'Двигается прямо', 'Сдает назад']))

    def show_speed(self, current_speed):
        print(f'Текущая скорость автомобиля {current_speed} км/ч')


class TownCar(Car):
    def show_speed(self, current_speed):
        print(f'Вы превысили скорость, максимальная разршенная скорость 60 км/ч') if current_speed > 60 \
            else print(f'Текущая скорость автомобиля {current_speed} км/ч')


class SportCar (Car):
    pass


class WorkCar(Car):
    def show_speed(self, current_speed):
        print(f'Вы превысили скорость, разршенная скорость 40 км/ч') if current_speed > 40 \
            else print(f'Текущая скорость автомобиля {current_speed} км/ч')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True


town_car = TownCar('Volvo', 'Голубой', '260')
town_car.go()
town_car.show_speed(90)
town_car.turn()
town_car.stop()
print(town_car.color)
print()

sport_car = SportCar('Nissan GT-R', 'Белый', '340')
sport_car.go()
sport_car.turn()
sport_car.show_speed(180)
sport_car.stop()
print(sport_car.name)
print()

work_car = WorkCar('Ford', 'Красный', '160')
work_car.go()
work_car.turn()
work_car.show_speed(50)
work_car.stop()
print(work_car.speed)
print()

police_car = PoliceCar('Ford', 'Серебристый', '180')
police_car.go()
police_car.stop()
print(police_car.is_police)

# 5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Пишем ручкой {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашами {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Выделяем маркером {self.title}.')


pen_1 = Pen('Pilot')
pen_1.draw()

pencil_1 = Pencil('Crayola')
pencil_1.draw()

handle_1 = Handle('TextLiner')
handle_1.draw()
