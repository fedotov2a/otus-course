import pytest
from hw_02.src.square import Square
from hw_02.src.constants import TextException, DefaultFigureName


class TestSquare:
    EPS = 1e-3

    @pytest.mark.parametrize(
        ('side', 'area', 'perimeter'),
        [
            (1, 1, 4),
            (0.1, 0.01, 0.4),
        ]
    )
    def test_positive_sides(self, side, area, perimeter):
        square = Square(side)
        print(square)

        assert square.name == DefaultFigureName.SQUARE
        assert abs(square.area - area) < TestSquare.EPS
        assert abs(square.perimeter - perimeter) < TestSquare.EPS

    @pytest.mark.parametrize(
        ('side', 'area', 'perimeter'),
        [
            (1, 1, 4)
        ]
    )
    def test_change_sides_and_recalculate_area_and_perimeter(self, side, area, perimeter):
        square = Square(side)

        assert square.name == DefaultFigureName.SQUARE
        assert abs(square.area - area) < TestSquare.EPS
        assert abs(square.perimeter - perimeter) < TestSquare.EPS

        square.side = 3
        expected_area = 9
        expected_perimeter = 12

        assert abs(square.area - expected_area) < TestSquare.EPS
        assert abs(square.perimeter - expected_perimeter) < TestSquare.EPS

    @pytest.mark.parametrize(
        ('side', 'area', 'perimeter', 'name'),
        [
            (1, 1, 4, 'My Super Square'),
        ]
    )
    def test_set_other_name(self, side, area, perimeter, name):
        square = Square(side, name=name)

        assert square.name == name
        assert abs(square.area - area) < TestSquare.EPS
        assert abs(square.perimeter - perimeter) < TestSquare.EPS

    @pytest.mark.parametrize(
        'side',
        [
            -2,
            -0.01,
            0,
        ]
    )
    def test_negative_and_zero_sides(self, side):
        with pytest.raises(ValueError, match=TextException.ZERO_OR_NEGATIVE_SIDE):
            square = Square(side)

    @pytest.mark.parametrize(
        'side',
        [
            '5',
            False,
            Square(1),
            [5],
            {'5': 5},
            None,
        ]
    )
    def test_test_invalid_type_of_sides(self, side):
        with pytest.raises(ValueError, match=TextException.NOT_A_NUMBER):
            square = Square(side)
