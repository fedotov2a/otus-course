import math
from hw_02.src.figure import Figure
from hw_02.src.constants import TextException, DefaultFigureName


class Circle(Figure):
    """Реализует класс Круг"""

    def __init__(self, radius, name=DefaultFigureName.CIRCLE):
        """Конструктор

        Args:
            radius (int | float): радиус круга
            name (str): название фигуры
        """

        self._validate_values(radius)
        super().__init__(name)

        self._radius = radius
        self._recalculate_perimeter_and_area()

    def __str__(self):
        """Возвращает строковое представление объекта"""
        return (
            f'{self.name}('
            f'r: {self._radius}, '
            f'area: {self.area}, '
            f'perimeter: {self.perimeter})'
        )

    def __repr__(self):
        """Возвращает строковое представление объекта"""
        return (
            f'{self.name}('
            f'r: {self._radius}, '
            f'area: {self.area}, '
            f'perimeter: {self.perimeter})'
        )

    def calculate_area(self):
        """Вычисляет площадь круга"""
        return math.pi * self._radius * self._radius

    def calculate_perimeter(self):
        """Вычисляет периметр круга"""
        return 2 * math.pi * self._radius

    @property
    def radius(self):
        """Возвращает радиус круга"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Задает радиус круга

        Args:
            value (int | float): новое значение радиуса круга
        """

        self._validate_values(value)
        self._radius = value
        self._recalculate_perimeter_and_area()

    def _validate_values(self, *values):
        """Валидирует значение стороны фигуры"""

        if not self._is_valid_values_type(*values):
            raise ValueError(TextException.NOT_A_NUMBER)

        if not self._is_positive_values(*values):
            raise ValueError(TextException.ZERO_OR_NEGATIVE_RADIUS)
