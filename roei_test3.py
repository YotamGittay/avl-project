import unittest

from avl_template import *
from graph_tree import draw_binary_tree
from UnitTestAVLTree import TestAVLTree
import inspect

# NODES = [15,8,22,4,20,11,24,2,18,12,9,13]
# tree = AVLTree()
# for i in range(len(NODES)):
#     tree.insert(NODES[i], "")

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAVLTree))
runner = unittest.TextTestRunner()
runner.run(suite)

