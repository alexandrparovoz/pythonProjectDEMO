# класс вычисления корня квадратного уравнения
import math
class Root:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c

    def discrim(self):
        if self.get_b() ** 2 - 4 * self.get_a() * self.get_c() > 0:
            return True
        if self.get_b() ** 2 - 4 * self.get_a() * self.get_c() == 0:
            return 0
        return False
    def root(self):
        if self.discrim():
            res1 = self.get_b() + math.sqrt(self.discrim() / (2 * self.get_a())
            #res2 = self.get_b() - math.sqrt(self.discrim() / (2 * self.get_a())
            return  res1, res2
        if self.discrim() == 0:
            res = self.get_b / (2 * self.get_a())
            return  res

root1 = Root(3, 6, 3)
print(root1.discrim())
print(root1.root())