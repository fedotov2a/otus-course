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
        ]
    )
    def test_add_figures(self, figure1, figure2, result):
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
        ]
    )
    def test_add_figure_to_invalid_type(self, figure1, figure2):
        with pytest.raises(ValueError, match=TextException.ARGUMENT_IS_NOT_FIGURE):
            figure1.add_area(figure2)
