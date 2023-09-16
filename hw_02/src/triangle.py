import math
from hw_02.src.figure import Figure
from hw_02.src.constants import TextException, DefaultFigureName


class Triangle(Figure):
    """Реализует класс Треугольник"""

    def __init__(self, side_a, side_b, side_c, name=DefaultFigureName.TRIANGLE):
        """Конструктор

        Args:
            side_a (int | float): сторона a
            side_b (int | float): сторона b
            side_c (int | float): сторона c
            name (str): название фигуры
        """

        self._validate_values(side_a, side_b, side_c)
        super().__init__(name)

        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

        if not self.is_valid_triangle():
            raise ValueError(f'{TextException.INVALID_TRIANGLE} {self!s}')

        self._perimeter = self.calculate_perimeter()
        self._area = self.calculate_area()

    def __str__(self):
        """Возвращает строковое представление объекта"""
        return (
            f'{self.name}('
            f'a: {self._side_a}, '
            f'b: {self._side_b}, '
            f'c: {self._side_c}, '
            f'area: {self._area}, '
            f'perimeter: {self._perimeter})'
        )

    def __repr__(self):
        """Возвращает строковое представление объекта"""
        return (
            f'{self.name}('
            f'a: {self._side_a}, '
            f'b: {self._side_b}, '
            f'c: {self._side_c}, '
            f'area: {self._area}, '
            f'perimeter: {self._perimeter})'
        )

    def calculate_area(self):
        """Вычисляет площадь треугольника по формуле Герона"""

        semi_perimeter = self._perimeter / 2

        return math.sqrt(
            semi_perimeter
            * (semi_perimeter - self._side_a)
            * (semi_perimeter - self._side_b)
            * (semi_perimeter - self._side_c)
        )

    def calculate_perimeter(self):
        """Вычисляет периметр треугольника"""
        return self._side_a + self._side_b + self._side_c

    def is_valid_triangle(self):
        """Проверяет существование треугольника
        по теореме о неравенстве треугольника

        Returns:
            True, если каждая сторона треугольника меньше суммы двух других
            False - иначе
        """
        return (
            self._side_a + self._side_b > self._side_c
            and self._side_a + self._side_c > self._side_b
            and self._side_b + self._side_c > self._side_a
        )

    @property
    def side_a(self):
        """Возвращает сторону a"""
        return self._side_a

    @side_a.setter
    def side_a(self, value):
        """Задает сторону a

        Args:
            value (int | float): новое значение стороны a
        """

        self._validate_values(value)
        self._side_a = value

        if not self.is_valid_triangle():
            raise ValueError(f'{TextException.INVALID_TRIANGLE} {self!s}')

        self._perimeter = self.calculate_perimeter()
        self._area = self.calculate_area()

    @property
    def side_b(self):
        """Возвращает сторону b"""
        return self._side_b

    @side_b.setter
    def side_b(self, value):
        """Задает сторону b

        Args:
            value (int | float): новое значение стороны b
        """

        self._validate_values(value)
        self._side_b = value

        if not self.is_valid_triangle():
            raise ValueError(f'{TextException.INVALID_TRIANGLE} {self!s}')

        self._perimeter = self.calculate_perimeter()
        self._area = self.calculate_area()

    @property
    def side_c(self):
        """Возвращает сторону c"""
        return self._side_c

    @side_c.setter
    def side_c(self, value):
        """Задает сторону c

        Args:
            value (int | float): новое значение стороны c
        """

        self._validate_values(value)
        self._side_c = value

        if not self.is_valid_triangle():
            raise ValueError(f'{TextException.INVALID_TRIANGLE} {self!s}')

        self._perimeter = self.calculate_perimeter()
        self._area = self.calculate_area()
