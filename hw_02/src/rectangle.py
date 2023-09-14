from hw_02.src.figure import Figure
from hw_02.src.constants import TextException, DefaultFigureName


class Rectangle(Figure):
    """Реализует класс Прямоугольник"""

    def __init__(self, side_a, side_b, name=DefaultFigureName.RECTANGLE):
        """Конструктор

        Args:
            side_a (int | float): сторона a
            side_b (int | float): сторона b
            name (str): название фигуры
        """

        self._validate_values(side_a, side_b)
        super().__init__(name)

        self._side_a = side_a
        self._side_b = side_b

        self._recalculate_perimeter_and_area()

    def __str__(self):
        """Возвращает строковое представление объекта"""
        return (
            f'{self.name}('
            f'a: {self._side_a}, '
            f'b: {self._side_b}, '
            f'area: {self._area}, '
            f'perimeter: {self._perimeter})'
        )

    def __repr__(self):
        """Возвращает строковое представление объекта"""
        return (
            f'{self.name}('
            f'a: {self._side_a}, '
            f'b: {self._side_b}, '
            f'area: {self.area}, '
            f'perimeter: {self.perimeter})'
        )

    def calculate_area(self):
        """Вычисляет площадь фигуры"""
        return self._side_a * self._side_b

    def calculate_perimeter(self):
        """Вычисляет периметр фигуры"""
        return 2 * (self._side_a + self._side_b)

    @property
    def side_a(self):
        """Возвращает сторону a"""
        return self._side_a

    @side_a.setter
    def side_a(self, value):
        """Задает сторону a

        Args:
            value (int | float): сторона a
        """

        self._validate_values(value)
        self._side_a = value
        self._recalculate_perimeter_and_area()

    @property
    def side_b(self):
        """Возвращает сторону b"""
        return self._side_b

    @side_b.setter
    def side_b(self, value):
        """Задает сторону b

        Args:
            value (int | float): сторона b
        """

        self._validate_values(value)
        self._side_b = value
        self._recalculate_perimeter_and_area()
