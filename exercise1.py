# Hellofresh machine learning engineer task
#
# 1 General Programming
#
# Author: Kai Chen
# Date: Apr, 2018
#

class Link(object):
    parent = None # a link has a parent link

    def __init__(self, parent_name, child_name, parent=None):
        self.parent_name = parent_name
        self.child_name = child_name
        self.parent = parent

def find_venture(list_of_links, account_name):
    """
    given a list of links and an account name, find the name of the venture it belongs to.
    - root: the node of the tree with no parent.
    - venture: all the children of the root.
    - accounts: all the nodes which are not the root neither the venture nodes.

    :param list_of_links: a list contains the links.
    :param account_name: a string contains an account name.
    :return:
    """
    account = None

    # find the account node in the list
    for link in list_of_links:
        if link.child_name == account_name:
            account = link

    if account is None:
        return None

    parent = account.parent

    if parent is None:
        return None

    while not parent.parent is None:
        if parent.parent.parent is None:
            return parent.child_name
        else:
            parent = parent.parent

    return None


# Note this is not a proper test. The proper test can be found in 'test_exercise1.py'

# create a tree
list_of_links = []

root_link = Link(None, "Root")
list_of_links.append(root_link)

top_left_link = Link("Root","Hellofresh UK", root_link)
list_of_links.append(top_left_link)
top_right_link = Link("Root","Hellofresh US", root_link)
list_of_links.append(top_right_link)

account1_link = Link("Hellofresh UK","account1", top_left_link)
list_of_links.append(account1_link)
account2_link = Link("Hellofresh UK","account2", top_left_link)
list_of_links.append(account2_link)

account3_link = Link("Hellofresh US", "account3", top_right_link)
list_of_links.append(account3_link)

account4_link = Link("account3", "account4", account3_link)
list_of_links.append(account4_link)
account5_link = Link("account3", "account5", account3_link)
list_of_links.append(account5_link)

account6_link = Link("account4", "account6", account4_link)
list_of_links.append(account6_link)

# test
venture_name = find_venture(list_of_links, "account5")
print(venture_name)

venture_name = find_venture(list_of_links, "account1")
print(venture_name)

venture_name = find_venture(list_of_links, "account6")
print(venture_name)

venture_name = find_venture(list_of_links, "HelloFresh UK")
print(venture_name)

venture_name = find_venture(list_of_links, "account7")
print(venture_name)