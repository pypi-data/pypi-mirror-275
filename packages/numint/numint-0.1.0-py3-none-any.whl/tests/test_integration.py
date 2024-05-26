import unittest
from NumInt.integration import trapezoidal_rule, simpsons_rule, midpoint_rule, booles_rule, romberg_integration, gauss_legendre_quadrature

class TestIntegrationMethods(unittest.TestCase):

    def test_trapezoidal_rule(self):
        def f(x):
            return x**2
        self.assertAlmostEqual(trapezoidal_rule(f, 0, 10, 1000), 333.333333, places=3)

    def test_simpsons_rule(self):
        def f(x):
            return x**2
        self.assertAlmostEqual(simpsons_rule(f, 0, 10, 1000), 333.333333, places=5)
    
    def test_midpoint_rule(self):
        def f(x):
            return x**2
        self.assertAlmostEqual(midpoint_rule(f, 0, 10, 1000), 333.333333, places=3)

    def test_booles_rule(self):
        def f(x):
            return x**2
        self.assertAlmostEqual(booles_rule(f, 0, 10, 1000), 333.333333, places=3)

    def test_romberg_integration(self):
        def f(x):
            return x**2
        self.assertAlmostEqual(romberg_integration(f, 0, 10), 333.333333, places=5)

    def test_gauss_legendre_quadrature(self):
        def f(x):
            return x**2
        self.assertAlmostEqual(gauss_legendre_quadrature(f, 0, 10, 5), 333.333333, places=5)

if __name__ == "__main__":
    unittest.main()
