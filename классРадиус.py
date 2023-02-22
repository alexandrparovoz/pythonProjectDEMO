# принимаем радиус, находим площадь круга  S = p * r2 и длину окружности C = 2 * p * r
import math

class Circle:
    def __init__(self, rad):
        self.rad = rad
    def circle_len(self):
        len = 2 * math.pi * self.rad
        return len
    def roun(self, circle_len):
        sqr = circle_len ** 2/ 4
        return sqr

    # def round_square(self):
    #     sqr = math.pi * self.rad ** 2
    #     return f'Площадь круга равна - {sqr} единиц.'

radius = Circle(40)
print(radius.roun())
#print(radius.circle_len())