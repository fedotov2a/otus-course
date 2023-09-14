import pytest
from hw_02.src.triangle import Triangle
from hw_02.src.constants import TextException, DefaultFigureName


class TestTriangle:
    EPS = 1e-3

    @pytest.mark.parametrize(
        ('side_a', 'side_b', 'side_c', 'area', 'perimeter'),
        [
            (1, 1, 1, 0.433, 3),  # равносторонний
            (1, 3, 3, 1.479, 7),  # равнобедренный
            (9, 4, 6, 9.562, 19),  # разносторонний
            (3, 4, 5, 6, 12),  # прямоугольный
            (2, 3, 4, 2.904, 9),  # тупоугольный
            (0.91, 2.3, 1.67, 0.634, 4.88)
        ]
    )
    def test_positive_sides(self, side_a, side_b, side_c, area, perimeter):
        triangle = Triangle(side_a, side_b, side_c)

        assert triangle.name == DefaultFigureName.TRIANGLE
        assert abs(triangle.area - area) < TestTriangle.EPS
        assert abs(triangle.perimeter - perimeter) < TestTriangle.EPS

    @pytest.mark.parametrize(
        ('side_a', 'side_b', 'side_c', 'area', 'perimeter'),
        [
            (9, 4, 6, 9.562, 19),
        ]
    )
    def test_change_sides_and_recalculate_area_and_perimeter(self, side_a, side_b, side_c, area, perimeter):
        triangle = Triangle(side_a, side_b, side_c)

        assert triangle.name == DefaultFigureName.TRIANGLE
        assert abs(triangle.area - area) < TestTriangle.EPS
        assert abs(triangle.perimeter - perimeter) < TestTriangle.EPS

        triangle.side_a = 8
        expected_area = 11.618
        expected_perimeter = 18

        assert abs(triangle.area - expected_area) < TestTriangle.EPS
        assert abs(triangle.perimeter - expected_perimeter) < TestTriangle.EPS

        triangle.side_b = 5
        expected_area = 14.981
        expected_perimeter = 19

        assert abs(triangle.area - expected_area) < TestTriangle.EPS
        assert abs(triangle.perimeter - expected_perimeter) < TestTriangle.EPS

        triangle.side_c = 7
        expected_area = 17.321
        expected_perimeter = 20

        assert abs(triangle.area - expected_area) < TestTriangle.EPS
        assert abs(triangle.perimeter - expected_perimeter) < TestTriangle.EPS

    @pytest.mark.parametrize(
        ('side_a', 'side_b', 'side_c', 'area', 'perimeter', 'name'),
        [
            (3, 4, 5, 6, 12, 'My Super Triangle'),
        ]
    )
    def test_set_other_name(self, side_a, side_b, side_c, area, perimeter, name):
        triangle = Triangle(side_a, side_b, side_c, name=name)

        assert triangle.name == name
        assert abs(triangle.area - area) < TestTriangle.EPS
        assert abs(triangle.perimeter - perimeter) < TestTriangle.EPS

    @pytest.mark.parametrize(
        ('side_a', 'side_b', 'side_c'),
        [
            (1, 1, 10),
            (0.1, 0.1, 10),
        ]
    )
    def test_invalid_triangle(self, side_a, side_b, side_c):
        with pytest.raises(ValueError, match=TextException.INVALID_TRIANGLE):
            triangle = Triangle(side_a, side_b, side_c)

    @pytest.mark.parametrize(
        ('side_a', 'side_b', 'side_c'),
        [
            (-2, 5, 0),
            (5, 0, -0.01),
            (0, -2, 5.33),
            (0, 0, 0)
        ]
    )
    def test_negative_and_zero_sides(self, side_a, side_b, side_c):
        with pytest.raises(ValueError, match=TextException.ZERO_OR_NEGATIVE_SIDE):
            triangle = Triangle(side_a, side_b, side_c)

    @pytest.mark.parametrize(
        ('side_a', 'side_b', 'side_c'),
        [
            ('4', 2, 3),
            (1, True, 1),
            (Triangle(1, 1, 1), 1, 1),
            (3, [5], 4),
            ({'5': 5}, 3, 4),
            (None, None, None)
        ]
    )
    def test_test_invalid_type_of_sides(self, side_a, side_b, side_c):
        with pytest.raises(ValueError, match=TextException.NOT_A_NUMBER):
            triangle = Triangle(side_a, side_b, side_c)
