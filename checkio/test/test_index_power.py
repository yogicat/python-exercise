import unittest
from index_power import index_power, index_power2


class IndexPowerTest(unittest.TestCase):
    def test_index_power(self):
        result = index_power([1, 2, 3], 2)
        self.assertEqual(result, 9)

    def test_index_power_error(self):
        result = index_power([1, 2, 3], 3)
        self.assertEqual(result, -1)

    def test_index_power2(self):
        result = index_power2([1, 2, 3], 2)
        self.assertEqual(result, 9)

    def test_index_power2_error(self):
        result = index_power2([1, 2, 3], 3)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
