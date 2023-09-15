import pytest
from hw_02.src.rectangle import Rectangle
from hw_02.src.circle import Circle
from hw_02.src.square import Square
from hw_02.src.triangle import Triangle
from hw_02.src.constants import TextException


class TestAddFigures:
    EPS = 1e-3

    @pytest.mark.parametrize(
        ('figure1', 'figure2', 'result'),
        [
            (Rectangle(1, 1), Circle(1), 4.141),
            (Rectangle(1, 1), Square(1), 2),
            (Rectangle(1, 1), Triangle(1, 1, 1), 1.433),
            (Circle(1), Square(1), 4.141),
            (Circle(1), Triangle(1, 1, 1), 3.574),
            (Square(1), Triangle(1, 1, 1), 1.433),
        ],
        ids=[
            'sum_area_rectangle_and_circle',
            'sum_area_rectangle_and_square',
            'sum_area_rectangle_and_triangle',
            'sum_area_circle_and_square',
            'sum_area_circle_and_triangle',
            'sum_area_square_and_triangle',
        ]
    )
    def test_add_figures(self, figure1, figure2, result):
        """Проверяет сложение площадей двух фигур

        Проверка на равенство двух чисел с плавающей точкой
        происходит с заданной точностью epsilon
        """

        assert abs(figure1.add_area(figure2) - result) < TestAddFigures.EPS
        assert abs((figure1 + figure2) - result) < TestAddFigures.EPS

    @pytest.mark.parametrize(
        ('figure1', 'figure2'),
        [
            (Rectangle(1, 1), 1),
            (Circle(1), -2.5),
            (Square(1), '10'),
            (Triangle(1, 1, 1), None),
            (Rectangle(1, 1), True),
            (Square(1), [5]),
            (Circle(1), {'5': 5})
        ],
        ids=[
            'try_to_add_rectangle_and_int',
            'try_to_add_circle_and_float',
            'try_to_add_square_and_string',
            'try_to_add_triangle_and_none',
            'try_to_add_rectangle_and_bool',
            'try_to_add_square_and_list',
            'try_to_add_circle_and_dict',
        ]
    )
    def test_add_figure_to_invalid_type(self, figure1, figure2):
        """Проверяет выкидывание исключения,
        при передаче аргумента с невалидным типом
        """
        with pytest.raises(ValueError, match=TextException.ARGUMENT_IS_NOT_FIGURE):
            figure1.add_area(figure2)
