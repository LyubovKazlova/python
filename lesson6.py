#задание 1.
import time
class TrafficLight():
    traffic_color = ['красный', 'желтый', 'зеленый']
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор показывет сигнал: {TrafficLight.traffic_color[i]}')
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(2)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()
#задание 2.
class Road():
    def _init_(self, _length, _width):
        self._length = _length
        self._width = _width
    def massa(self):
        _length = float(input('Длина дороги в метрах: '))
        _width = float(input('Ширина дороги в метрах: '))
        self.mass_1 = float(input('Масса асфальта на 1 м.кв. тощиной 1 см (стандарт 25 кг): '))
        self.thick = float(input('Толщина покрытия в см: '))
        return _length * _width * self.mass_1 * self.thick
road = Road()
print (f'Масса асфальта: {road.massa()} т')
# Задание 3.
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage' : wage, 'bonus' : bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage,bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position("Иван", "Иванов", "менеджер", 100, 700)
b = Position('Федор', 'Федоров', 'дворник', 50, 150)
c = Position('Инга', 'Борге', 'Для_красоты', 1000, 1000)
print(a.position)
print(a.get_full_name())
print(a.get_total_income())
print(b.position)
print(b.get_full_name())
print(b.get_total_income())
print(c.position)
print(c.get_full_name())
print(c.get_total_income())
# задание 4.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} поехала'
    def stop(self):
        return f'{self.name} остановилась'
    def turn_rigth(self):
        return f'{self.name} повернула направо'
    def turn_left(self):
        return f'{self.name} повернула налево'
    def show_speed(self):
        return f'скорость {self.speed} км/ч'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'скорость {self.speed} км/ч, скорость превышена!'
        else:
            return f'скорость {self.speed} км/ч'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'скорость {self.speed} км/ч, скорость превышена!'
        else:
            return f'скорость {self.speed} км/ч'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

bmw = SportCar(150, 'черный', 'БМВ', False)
citroen = TownCar(70, 'серебристый', 'Ситроен', False)
lada = WorkCar(40, 'белый', 'Лада', False)
skoda = PoliceCar(80, 'синий', 'Шкода', True)
print(f'{bmw.color} {bmw.turn_left()} {bmw.show_speed()}')
print(f'{lada.color} {lada.turn_rigth()} {lada.show_speed()}')
print(f'{citroen.color} {citroen.go()} {citroen.show_speed()}')
print(f'{skoda.color} {skoda.turn_rigth()} {skoda.show_speed()}')
print(f'{lada.name} полицейская машина? {lada.is_police}')
print(f'{skoda.name} полицейская машина? {skoda.is_police}')
#задание 5.
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'{self.title} запуск отрисовки'
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Инструмент {self.title}, запуск отрисовки'
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли {self.title}, запуск отрисовки'
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли инструмент {self.title}, запуск отрисовки'
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())


