import unittest
from rectangle import area, perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_normal_values(self):
        res = area(3, 7)
        self.assertEqual(res, 21)

    def test_area_float_values(self):
        res = area(2.5, 6.0)
        self.assertAlmostEqual(res, 15.0)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_perimeter_zero_side(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_square(self):
        res = perimeter(15, 15)
        self.assertEqual(res, 60)

    def test_perimeter_normal_values(self):
        res = perimeter(3, 7)
        self.assertEqual(res, 20)

    def test_perimeter_float_values(self):
        res = perimeter(2.5, 6.0)
        self.assertAlmostEqual(res, 17.0)


if __name__ == "__main__":
    unittest.main()