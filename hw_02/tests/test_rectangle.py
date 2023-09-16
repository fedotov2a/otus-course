import pytest
from hw_02.src.rectangle import Rectangle
from hw_02.src.constants import TextException, DefaultFigureName


class TestRectangle:
    EPS = 1e-3

    @pytest.mark.parametrize(
        ('side_a', 'side_b', 'area', 'perimeter'),
        [
            (1, 2, 2, 6),
            (2, 2, 4, 8),
            (0.05, 0.1, 0.005, 0.3),
        ]
    )
    def test_positive_sides(self, side_a, side_b, area, perimeter):
        """Проверяет вычисление площади и периметра фигуры

        Проверка на равенство двух чисел с плавающей точкой
        происходит с заданной точностью epsilon
        """

        rectangle = Rectangle(side_a, side_b)

        assert rectangle.name == DefaultFigureName.RECTANGLE
        assert abs(rectangle.area - area) < TestRectangle.EPS
        assert abs(rectangle.perimeter - perimeter) < TestRectangle.EPS

    @pytest.mark.parametrize(
        ('side_a', 'side_b', 'area', 'perimeter'),
        [
            (1, 2, 2, 6)
        ]
    )
    def test_change_sides_and_recalculate_area_and_perimeter(self, side_a, side_b, area, perimeter):
        """Проверяет вычисление площади и периметра фигуры,
        при изменении стороны фигуры

        Проверка на равенство двух чисел с плавающей точкой
        происходит с заданной точностью epsilon
        """

        rectangle = Rectangle(side_a, side_b)

        assert rectangle.name == DefaultFigureName.RECTANGLE
        assert abs(rectangle.area - area) < TestRectangle.EPS
        assert abs(rectangle.perimeter - perimeter) < TestRectangle.EPS

        rectangle.side_a = 5
        expected_area = 10
        expected_perimeter = 14

        assert abs(rectangle.area - expected_area) < TestRectangle.EPS
        assert abs(rectangle.perimeter - expected_perimeter) < TestRectangle.EPS

        rectangle.side_b = 5
        expected_area = 25
        expected_perimeter = 20

        assert abs(rectangle.area - expected_area) < TestRectangle.EPS
        assert abs(rectangle.perimeter - expected_perimeter) < TestRectangle.EPS

    @pytest.mark.parametrize(
        ('side_a', 'side_b', 'area', 'perimeter', 'name'),
        [
            (1, 2, 2, 6, 'My Super Rectangle'),
        ]
    )
    def test_set_other_name(self, side_a, side_b, area, perimeter, name):
        """Проверяет установку названия фигуры"""

        rectangle = Rectangle(side_a, side_b, name=name)

        assert rectangle.name == name
        assert abs(rectangle.area - area) < TestRectangle.EPS
        assert abs(rectangle.perimeter - perimeter) < TestRectangle.EPS

    @pytest.mark.parametrize(
        ('side_a', 'side_b'),
        [
            (-2, 5),
            (5, -0.01),
            (-0.01, -2),
            (0, 5),
            (5, 0),
            (0, 0)
        ]
    )
    def test_negative_and_zero_sides(self, side_a, side_b):
        """Проверяет выкидывание исключения,
        при передаче аргумента с невалидными значениями
        """
        with pytest.raises(ValueError, match=TextException.ZERO_OR_NEGATIVE_SIDE):
            rectangle = Rectangle(side_a, side_b)

    @pytest.mark.parametrize(
        ('side_a', 'side_b'),
        [
            ('5', 2),
            (3, False),
            (Rectangle(1, 2), 4),
            (2, [5]),
            ({'5': 5}, 2),
            (None, None)
        ],
        ids=[
            'string_value',
            'bool_value',
            'rectangle_object',
            'list',
            'dict',
            'none_value',
        ]
    )
    def test_test_invalid_type_of_sides(self, side_a, side_b):
        """Проверяет выкидывание исключения,
        при передаче аргумента с невалидным типом
        """
        with pytest.raises(ValueError, match=TextException.NOT_A_NUMBER):
            rectangle = Rectangle(side_a, side_b)
