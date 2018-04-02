# Hellofresh machine learning engineer tasks
# 2. Apache Spark, unit test
#
# Author: Kai Chen
# Date: Apr, 2018
#

import unittest
from recipes import *


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
        #self.assertEqual(mins, 60)

    def test_add_extra_field(self):
        """
        test function 'add_extra_field' in recipes.py
        :return:
        """
        pass


if __name__ == '__main__':
    unittest.main()
