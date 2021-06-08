import unittest
import numpy as np
from stellar_occultations import (
    cart2pol,
    calculate_plane,
    pupilCO,
    pupil_doble,
    calculate_separation,
    calculate_binary_parameters,
    calculate_star_radius,
    pol2cart,
    calculate_image_grid,
)


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
        self.n_pixels = 4096
        self.plane = 149799.86648859203
        self.mV = 15
        self.nEst = 29
        self.spectral_type = "M2"

    def test_cart2pol(self):
        expected_polar_coordinates = (0, 1)
        obtained_polar_coordinates = cart2pol(
            self.cartesian_x_coordinate, self.cartesian_y_coordinate
        )
        assert obtained_polar_coordinates == expected_polar_coordinates

    def test_pol2cart(self):
        expected_cartesian_coordinates = (-1, 0)
        obtained_cartesian_coordinates = pol2cart(1, np.pi)
        np.testing.assert_almost_equal(
            obtained_cartesian_coordinates, expected_cartesian_coordinates
        )

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

    def test_calculate_separation(self):
        obtained_separation = calculate_separation(self.n_pixels, self.plane, self.object_diameter)
        expected_separations = 68
        assert obtained_separation == expected_separations

    def test_calculate_binary_parameters(self):
        obtained_binary_parameters = calculate_binary_parameters(self.object_diameter)
        expected_parameters = (3172.3519672766997, 0, 1625.0, 1899.835519196333)
        assert obtained_binary_parameters == expected_parameters

    def test_calc_rstar(self):
        obtainded_star_parameters = calculate_star_radius(
            self.mV, self.spectral_type, self.object_distance_ua
        )
        expected_star_parameters = 852.1977173475242
        assert obtainded_star_parameters == expected_star_parameters

    def test_calculate_image_grid(self):
        obtained_rho_grid, obtained_phi_grid = calculate_image_grid(3, self.plane)
        expected_rho_grid = np.array(
            [
                [-2.35619449, -1.57079633, -0.78539816],
                [3.14159265, 0.0, 0.0],
                [2.35619449, 1.57079633, 0.78539816],
            ]
        )
        expected_phi_grid = np.array(
            [
                [105924.50141492, 74899.9332443, 105924.50141492],
                [74899.9332443, 0.0, 74899.9332443],
                [105924.50141492, 74899.9332443, 105924.50141492],
            ]
        )
        np.testing.assert_array_almost_equal(obtained_rho_grid, expected_rho_grid)
        np.testing.assert_array_almost_equal(obtained_phi_grid, expected_phi_grid)