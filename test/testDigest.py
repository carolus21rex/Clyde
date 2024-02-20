import unittest
from src.digest import distanceParse, multidimensional_distance


class TestGraphFunctions(unittest.TestCase):

    def test_multidimensional_distance(self):
        # Test with 2D points
        node1 = (1.0, 2.0)
        node2 = (4.0, 5.0)
        dimensions = 2
        distance = multidimensional_distance(node1, node2, dimensions)
        self.assertAlmostEqual(distance, 0.0, places=7)

        # Test with 3D points
        node1 = (1.0, 2.0, 3.0)
        node2 = (1.4, 2.1, 3.3)
        dimensions = 3
        distance = multidimensional_distance(node1, node2, dimensions)
        self.assertAlmostEqual(distance, 1.49009808, places=7)

        # Test with invalid dimensions
        node1 = (1.0, 2.0)
        node2 = (4.0, 5.0, 6.0)
        dimensions = 3
        with self.assertRaises(ValueError):
            multidimensional_distance(node1, node2, dimensions)

    def test_distanceParse(self):
        points = [
            [-2.0, 1.0, 0.5, -1.5],
            [-1.5, 2.0, 1.0, -1.0],
            [0.0, 1.5, -0.5, 2.0],
            [2.0, -1.5, 1.0, -0.5]
        ]
        matrix = [[0.0] * 4 for _ in range(4)]
        matrix = distanceParse(matrix, points, 4)
        print(matrix)
        self.assertEqual(matrix,
                         [
                                [2.0, 0.6771243444677046, 0.0, 0.0],
                                [0.6771243444677046, 2.0, 0.0, 0.0],
                                [0.0, 0.0, 2.0, 0.0],
                                [0.0, 0.0, 0.0, 2.0]])

if __name__ == '__main__':
    unittest.main()
