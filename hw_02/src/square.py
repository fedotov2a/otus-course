from hw_02.src.rectangle import Rectangle
from hw_02.src.constants import TextException, DefaultFigureName


class Square(Rectangle):
    """Реализует класс Квадрат"""

    def __init__(self, side, name=DefaultFigureName.SQUARE):
        """Конструктор

        Args:
            side (int | float): сторона квадрата
            name (str): название фигуры
        """
        super().__init__(side, side, name)

    @property
    def side(self):
        """Возвращает сторону квадрата"""
        return self._side_a

    @side.setter
    def side(self, value):
        """Задает сторону квадрата

        Args:
            value (int | float): новая сторона квадрата
        """

        self._validate_values(value)
        self._side_a = value
        self._side_b = value
        self._recalculate_perimeter_and_area()

    @Rectangle.side_a.setter
    def side_a(self, value):
        """Переопределяет сеттер класса родителя"""
        self.side = value

    @Rectangle.side_b.setter
    def side_b(self, value):
        """Переопределяет сеттер класса родителя"""
        self.side = value
