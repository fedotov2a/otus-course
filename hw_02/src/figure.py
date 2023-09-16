from abc import ABC, abstractmethod
from hw_02.src.constants import TextException


class Figure(ABC):
    """Абстрактный класс Фигура"""

    def __init__(self, name):
        """Конструктор

        Args:
            name (str): название фигуры
        """

        self._name = name
        self._area = None
        self._perimeter = None

    @abstractmethod
    def calculate_area(self):
        """Вычисляет площадь фигуры"""
        pass

    @abstractmethod
    def calculate_perimeter(self):
        """Вычисляет периметр фигуры"""
        pass

    @property
    def name(self):
        """Возвращает название фигуры"""
        return self._name

    @name.setter
    def name(self, value):
        """Задает название фигуры

        Args:
            value (str): название фигуры
        """
        self._name = value

    @property
    def area(self):
        """Возвращает площадь фигуры"""
        return self._area

    @property
    def perimeter(self):
        """Возвращает периметр фигуры"""
        return self._perimeter

    @staticmethod
    def _is_positive_values(*args):
        """Проверяет все ли значения положительные

        Args:
            args: список значений

        Returns:
            True, если все значения положительные
            False - иначе
        """
        return all(value > 0 for value in args)

    @staticmethod
    def _is_valid_values_type(*args):
        """Проверяет все ли значения являются числовыми типами

        Args:
            args: список значений

        Returns:
            True, если все значения являются числовыми типами
            False - иначе
        """
        return all(
            isinstance(value, (int, float)) and not isinstance(value, bool)
            for value in args
        )

    def add_area(self, other_figure):
        """Возвращает сумму площадей двух фигур

        Args:
            other_figure (Figure): фигура

        Returns:
            Сумму площадей двух фигур
        """

        if not isinstance(other_figure, Figure):
            raise ValueError(TextException.ARGUMENT_IS_NOT_FIGURE)

        return self.area + other_figure.area

    def __add__(self, other_figure):
        """Возвращает сумму площадей двух фигур

        Args:
            other_figure (Figure): фигура

        Returns:
            Сумму площадей двух фигур
        """

        return self.add_area(other_figure)

    def _validate_values(self, *values):
        """Валидирует значение стороны фигуры"""

        if not self._is_valid_values_type(*values):
            raise ValueError(TextException.NOT_A_NUMBER)

        if not self._is_positive_values(*values):
            raise ValueError(TextException.ZERO_OR_NEGATIVE_SIDE)
