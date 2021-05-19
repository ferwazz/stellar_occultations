import unittest
import numpy as np
from stellar_occultations import cart2pol, calculate_plane, pupilCO, pupil_doble


class Test_StellarOccultations(unittest.TestCase):
    def setUp(self):
        """
        Create variables for the tests
        """
        self.cartesian_x_coordinate = 1
        self.cartesian_y_coordinate = 0
        self.object_diameter = 5000
        self.wavelenght = 600e-9
        self.object_distance_ua = 50

    def test_cart2pol(self):
        expected_polar_coordinates = (0, 1)
        output = cart2pol(self.cartesian_x_coordinate, self.cartesian_y_coordinate)
        assert output == expected_polar_coordinates

    def test_calculate_plane(self):
        total_plane_size_obtained = calculate_plane(
            self.object_diameter, self.wavelenght, self.object_distance_ua
        )
        total_plane_size_expected = 149799.86648859203
        assert total_plane_size_obtained == total_plane_size_expected

    def test_pupilCO(self):
        circular_object_obtained = pupilCO(11, 3, 2)
        circular_object_expected = np.array(
            [
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
                [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
                [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            ]
        )
        np.testing.assert_array_equal(circular_object_obtained, circular_object_expected)

    def test_pupil_doble(self):
        binary_object_obtained = pupil_doble(10, 2, 1)
        binary_object_expected = np.array(
            [
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            ]
        )
        np.testing.assert_array_equal(binary_object_obtained, binary_object_expected)
