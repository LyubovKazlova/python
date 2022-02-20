#задание 1.
import time
class TrafficLight():
    traffic_color = ['красный', 'желтый', 'зеленый']
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор показывет сигнал: {TrafficLight.traffic_color[i]}')
            if i == 0:
                time.sleep(1)#7
            elif i == 1:
                time.sleep(1)#2
            elif i == 2:
                time.sleep(1)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()
#задание 2.
class Road():
    def _init_(self):
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


