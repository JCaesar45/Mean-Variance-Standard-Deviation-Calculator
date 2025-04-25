import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate_correct(self):
        actual = calculate([2,6,2,8,4,0,1,5,7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0],
                     [3.3333333333333335, 4.0, 4.333333333333333],
                     3.888888888888889],
            'variance': [[9.555555555555555, 0.6666666666666666, 13.555555555555555],
                         [4.0, 10.666666666666666, 6.888888888888889],
                         9.209876543209875],
            'standard deviation': [[3.091206165165235, 0.816496580927726, 3.683748105624071],
                                   [2.0, 3.265986323710904, 2.6246692913372702],
                                   3.0347778408328137],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        self.assertAlmostEqual(actual['mean'][0][0], expected['mean'][0][0])
        self.assertEqual(actual['max'][2], expected['max'][2])
        self.assertEqual(actual['sum'][2], expected['sum'][2])

    def test_calculate_raises_error(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3, 4, 5, 6, 7, 8])  # Only 8 numbers

if __name__ == "__main__":
    unittest.main()
