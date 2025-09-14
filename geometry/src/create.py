from geometry.src.figures import Circle, Triangle, FigureBase


class Create:
    """Фабрика фигур"""

    __registry = {
        "circle": Circle,
        "triangle": Triangle
    }  # Словарь фигур

    def register_figure(self, figure_type: str, figure_class):
        """Регистрация фигуры"""
        if figure_type in self.__registry:
            raise ValueError("Такая фигура уже существует")

        if not issubclass(figure_class, FigureBase):
            raise TypeError(f"Класс {figure_class.__name__} не является подклассом FigureBase")

        self.__registry[figure_type] = figure_class  # регистрация новой фигуры

    def create_figure(self, figure_type: str, **kwargs):
        """Cоздание фигуры"""
        figure_type = figure_type.strip().lower()
        if figure_type in self.__registry:
            return self.__registry[figure_type](**kwargs)
        else:
            raise ValueError("Такой фигуры не существует")
