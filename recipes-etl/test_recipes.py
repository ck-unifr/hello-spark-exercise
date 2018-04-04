# Hellofresh machine learning engineer task
#
# 2. Apache Spark, unit test
#
# Author: Kai Chen
# Date: Apr, 2018
#

import unittest
from recipes import *
import pandas as pd
import numpy as np


class TestLink(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_get_mins(self):
        """
        test function 'get_mins' in recipes.py
        """
        mins = get_mins('PT1h30m')
        self.assertEqual(mins, 90)

        mins = get_mins('PT2h')
        self.assertEqual(mins, 120)

        mins = get_mins('PT10H')
        self.assertEqual(mins, 600)

        mins = get_mins('PT30m')
        self.assertEqual(mins, 30)

        mins = get_mins('PT')
        self.assertEqual(mins, 0)


if __name__ == '__main__':
    unittest.main()
