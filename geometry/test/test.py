# test/test.py

import unittest
from geometry.src.figures import Circle, Triangle, FigureBase
from geometry.src.create import Create
from math import pi


class Test(unittest.TestCase):
    """Тестирование модулей figures.py и create.py"""

    def test_create_circle(self):
        """Проверка корректности создания объекта класса Circle"""
        # Проверка исключений при некорректных значениях радиуса
        with self.assertRaises(ValueError):
            Circle(-2)
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(TypeError):
            Circle('a')
        with self.assertRaises(TypeError):
            Circle()

        # Проверка успешного создания круга
        self.assertEqual(type(Circle(5)), Circle)

    def test_create_triangle(self):
        """Проверка корректности создания объекта класса Triangle"""
        # Проверка исключений при некорректных значениях сторон
        with self.assertRaises(ValueError):
            Triangle(-2, 3, 2)
        with self.assertRaises(TypeError):
            Triangle('a', 1, 2)
        with self.assertRaises(ValueError):
            Triangle(100, 1, 1)
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)

        # Проверка исключений при неправильном количестве аргументов
        with self.assertRaises(TypeError):
            Triangle(3, 4, 5, 6)
        with self.assertRaises(TypeError):
            Triangle(3, 4)
        with self.assertRaises(TypeError):
            Triangle()

        # Проверка успешного создания треугольника
        self.assertEqual(type(Triangle(5, 3, 4)), Triangle)

    def test_area_circle(self):
        """Проверка метода area() для круга"""
        self.assertEqual(Circle(5).area(), 5 ** 2 * pi)
        self.assertEqual(Circle(1).area(), 1 ** 2 * pi)
        self.assertEqual(Circle(10).area(), 10 ** 2 * pi)

    def test_area_triangle(self):
        """Проверка метода area() для треугольника"""
        self.assertEqual(round(Triangle(2, 2, 1).area(), 4), 0.9682)
        self.assertEqual(Triangle(3, 4, 5).area(), 6.0)

    def test_rectangle_triangle(self):
        """Проверка метода is_rectangle_triangle()"""
        self.assertEqual(Triangle(3, 4, 5).is_rectangle_triangle(), True)
        self.assertEqual(Triangle(4, 5, 3).is_rectangle_triangle(), True)
        self.assertEqual(Triangle(5, 3, 4).is_rectangle_triangle(), True)

        self.assertEqual(Triangle(2, 2, 3).is_rectangle_triangle(), False)

    def test_create(self):
        """Проверка регистрации и создания новых фигур через Create"""
        c = Create()

        class Rectangle_bad1(object):
            """Не унаследован от FigureBase"""
            pass

        class Rectangle_bad2(FigureBase):
            """Унаследован от FigureBase, но нет метода area"""
            pass

        class Rectangle(FigureBase):
            def __init__(self, width, height):
                if width <= 0 or height <= 0:
                    raise ValueError("высота и ширина не могут быть отрицательными")
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

        # Проверка: регистрация несовместимого класса (не унаследован от FigureBase)
        with self.assertRaises(TypeError):
            c.register_figure("rectangle", Rectangle_bad1)

        # Проверка: класс унаследован, но не реализован метод area()
        with self.assertRaises(NotImplementedError):
            c.register_figure("rectangle_bad", Rectangle_bad2)
            bad_rectangle = c.create_figure("rectangle_bad")
            bad_rectangle.area()

        # Регистрация и создание корректной фигуры
        c.register_figure("rectangle", Rectangle)
        new_rectangle = c.create_figure("rectangle", width=2, height=3)
        self.assertEqual(new_rectangle.area(), 6)

        # Проверка: отрицательные параметры
        with self.assertRaises(ValueError):
            c.create_figure("rectangle", width=0, height=-1)

        # Проверка: попытка зарегистрировать уже существующую фигуру
        with self.assertRaises(ValueError):
            c.register_figure("rectangle", Rectangle)

        # Проверка: попытка создать несуществующую фигуру
        with self.assertRaises(ValueError):
            c.create_figure("new_figure", parametr=223)


if __name__ == '__main__':
    unittest.main()