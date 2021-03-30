import unittest
import numpy as np
from stellar_occultations import cart2pol


class Test_HCLcat(unittest.TestCase):
    def setUp(self):
        """
        Create variables for the tests
        """
        self.cartesian_x_coordinate = 1
        self.cartesian_y_coordinate = 0

    def test_cart2pol(self):
        expected_polar_coordinates = (0, 1)
        output = cart2pol(self.cartesian_x_coordinate, self.cartesian_y_coordinate)
        assert output == expected_polar_coordinates


if __name__ == "__main__":
    unittest.main()
