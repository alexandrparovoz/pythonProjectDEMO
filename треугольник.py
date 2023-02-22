# ищем площадь, периметр и углы треугольника
# заданы либо два катета либо катет и гипотенуза

import math

class Retriangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.sides()
    def sides(self):
        if  self.a == '':
            self.a = math.sqrt(self.c ** 2 - self.b ** 2)
        elif self.b == '':
            self.b = math.sqrt(self.c ** 2 - self.a ** 2)
        elif self.c == '':
            self.c = math.sqrt(self.a ** 2 + self.b ** 2)
        return self.a, self.b, self.c
    def square(self):
        s = self.a * self.b / 2
        return f' Площадь равна  {s}'

dataTr = Retriangle(a='', b=3, c=5)
print(dataTr.sides())
print(dataTr.square())