from unittest import TestCase
from shapes_library.shapes_package.shapes_module import Circle
from shapes_library.shapes_package.shapes_module import Rectangle
from shapes_library.shapes_package.shapes_module import Triangle


class CircleTests(TestCase):
    """
    Contains all unit tests for the shapes_module.Circle class
    """
    def test_circle_area_returns_correct_result_with_valid_radius(self):
        """
        Tests that a Circle object with a radius > 0 returns the correct area
        """
        mock_radius = 5.0
        expected_area = 78.54
        mock_circle = Circle(radius=mock_radius)
        self.assertEqual(mock_circle.area(), expected_area)

    def test_circle_area_raises_ValueError_with_negative_radius(self):

        with self.asertRaises(Exceptions):
            mock_circle = Circle(radius=-1.0)
       

class RectangleTests(TestCase):
    """
    Contains all the unit tests for the shapes_module.Rectangle class
    """
    def test_rectangle_area_returns_correct_result_with_valid_height_and_width(self):
        """
        Tests that a Rectangle object with a height > 0 and a width > 0 returns the correct area
        """
        mock_height, mock_width = 10., 10.
        expected_area = 100.
        mock_rectangle = Rectangle(height=mock_height, width=mock_width)
        self.assertEqual(mock_rectangle.area(), expected_area)


class TriangleTests(TestCase):
    """
    Contains all the units test for the shape_module.Triangle class
    """
    def test_triangle_area_return_correct_result_with_valid_height_and_base(self):
        """
        Tests that a triangle object with a hight > 0 and a base > 0 returns the correct area
        """
        mock_height, mock_base = 10., 10.
        expected_area = 50.
        mock_triangle = Rectangle(height=mock_height, base=mock_base)
        self.assertEqual(mock_triangle.area(), expected_area)

