from geometry import Create, FigureBase


def main() -> None:
    """пример использования библиотеки"""
    c = Create()

    class Rectangle(FigureBase):
        def __init__(self, width, height):
            if width <= 0 or height <= 0:
                raise ValueError("высота и ширина не могут быть отрицательными")

            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    c.register_figure("rectangle", Rectangle)
    new_rectangle = c.create_figure("rectangle", width=2, height=3)

    circle = c.create_figure("circle", radius=2)
    triangle = c.create_figure("triangle", a=2, b=3, c=4)
    print(f"площадь прямоугольника: {new_rectangle.area()}")
    print(f"площадь круга: {circle.area()}")
    print(f"площадь {'' if triangle.is_rectangle_triangle() else 'не'}прямоугольного треугольника: {triangle.area()}")


if __name__ == "__main__":
    main()
