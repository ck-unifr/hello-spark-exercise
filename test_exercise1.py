# Hellofresh machine learning engineer tasks
# 1 General Programming, unit test
#
#
# Author: Kai Chen
# Date: Apr, 2018
#

import unittest
from exercise1 import *


class TestLink(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def create_link_list(self):
        """
        create a list of links
        :return: a list contains the links
        """
        list_of_links = []

        root_link = Link(None, "Root")
        list_of_links.append(root_link)

        top_left_link = Link("Root", "Hellofresh UK", root_link)
        list_of_links.append(top_left_link)
        top_right_link = Link("Root", "Hellofresh US", root_link)
        list_of_links.append(top_right_link)

        account1_link = Link("Hellofresh UK", "account1", top_left_link)
        list_of_links.append(account1_link)
        account2_link = Link("Hellofresh UK", "account2", top_left_link)
        list_of_links.append(account2_link)

        account3_link = Link("Hellofresh US", "account3", top_right_link)
        list_of_links.append(account3_link)

        account4_link = Link("account3", "account4", account3_link)
        list_of_links.append(account4_link)
        account5_link = Link("account3", "account5", account3_link)
        list_of_links.append(account5_link)

        account6_link = Link("account4", "account6", account4_link)
        list_of_links.append(account6_link)

        return list_of_links

    def test_find_venture(self):
        """
        test the 'find_venture' function in exercise1.py
        """
        list_of_links = self.create_link_list()

        venture_name = find_venture(list_of_links, "account5")
        self.assertEqual(venture_name, "Hellofresh US")

        venture_name = find_venture(list_of_links, "account1")
        self.assertEqual(venture_name, "Hellofresh UK")

        venture_name = find_venture(list_of_links, "account2")
        self.assertEqual(venture_name, "Hellofresh UK")

        venture_name = find_venture(list_of_links, "HelloFresh UK")
        self.assertIsNone(venture_name)

        venture_name = find_venture(list_of_links, "account7")
        self.assertIsNone(venture_name)

        venture_name = find_venture(list_of_links, "Root")
        self.assertIsNone(venture_name)


if __name__ == '__main__':
    unittest.main()