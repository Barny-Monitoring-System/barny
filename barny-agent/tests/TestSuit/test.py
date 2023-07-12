from classes.Metrics import Metrics

import unittest


class TestMetricsClass(unittest.TestCase):

    def test_upper(self):
        EXPECTED = { "barny": {} }

        self.assertEqual(Metrics([]).metrics(), EXPECTED)

if __name__ == '__main__':
    unittest.main()
