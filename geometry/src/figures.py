from math import pi, sqrt

class FigureBase(object):
    """базовый класс для фигур"""
    def area(self):
        raise NotImplementedError("Метод area должен быть реализован в классе-наследнике")

class Circle(FigureBase):
    """класс для круга"""
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError('Радиус круга должен быть больше нуля')
        self.radius = radius

    def area(self) -> float:
        """площадь круга"""
        return self.radius ** 2 * pi


class Triangle(FigureBase):
    """класс для треугольника"""
    def __init__(self, a:float, b:float, c:float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Стороны треугольника должны быть больше нуля')
        elif a >= b + c or b >= a + c or c >= a + b:
            raise ValueError('Недопустимые стороны треугольника')
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """площадь треугольника по формуле Герона"""
        p = (self.a + self.b + self.c) / 2
        if p > 0:
            if p - self.a > 0 and p - self.b > 0 and p - self.c > 0:
                return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_rectangle_triangle(self) -> bool:
        """является ли треугольник прямоугольным"""
        mas = sorted([self.a, self.b, self.c])
        if mas[0] ** 2 + mas[1] ** 2 == mas[2] ** 2:
            return True

        return False
