import pytest
from hw_02.src.circle import Circle
from hw_02.src.constants import TextException, DefaultFigureName


class TestCircle:
    EPS = 1e-3

    @pytest.mark.parametrize(
        ('radius', 'area', 'perimeter'),
        [
            (1, 3.142, 6.283),
            (0.05, 0.007, 0.314),
        ]
    )
    def test_positive_radius(self, radius, area, perimeter):
        circle = Circle(radius)

        assert circle.name == DefaultFigureName.CIRCLE
        assert abs(circle.area - area) < TestCircle.EPS
        assert abs(circle.perimeter - perimeter) < TestCircle.EPS

    @pytest.mark.parametrize(
        ('radius', 'area', 'perimeter'),
        [
            (10, 314.159, 62.831),
        ]
    )
    def test_change_radius_and_recalculate_area_and_perimeter(self, radius, area, perimeter):
        circle = Circle(radius)

        assert circle.name == DefaultFigureName.CIRCLE
        assert abs(circle.area - area) < TestCircle.EPS
        assert abs(circle.perimeter - perimeter) < TestCircle.EPS

        circle.radius = 5.5
        expected_area = 95.033
        expected_perimeter = 34.557

        assert abs(circle.area - expected_area) < TestCircle.EPS
        assert abs(circle.perimeter - expected_perimeter) < TestCircle.EPS

    @pytest.mark.parametrize(
        ('radius', 'area', 'perimeter', 'name'),
        [
            (1, 3.142, 6.283, 'My Super Circle'),
        ]
    )
    def test_set_other_name(self, radius, area, perimeter, name):
        circle = Circle(radius, name=name)

        assert circle.name == name
        assert abs(circle.area - area) < TestCircle.EPS
        assert abs(circle.perimeter - perimeter) < TestCircle.EPS

    @pytest.mark.parametrize(
        'radius',
        [
            -2,
            -0.01,
            0,
        ]
    )
    def test_negative_and_zero_radius(self, radius):
        with pytest.raises(ValueError, match=TextException.ZERO_OR_NEGATIVE_RADIUS):
            circle = Circle(radius)

    @pytest.mark.parametrize(
        'radius',
        [
            '5',
            False,
            None,
            Circle(1),
            [5],
            {'5': 5}
        ]
    )
    def test_invalid_type_of_radius(self, radius):
        with pytest.raises(ValueError, match=TextException.NOT_A_NUMBER):
            circle = Circle(radius)
