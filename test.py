from tests import tests

import unittest
from UnitTestAVLTree import TestAVLTree
t = tests()
t.test_join()
t.testInsertDelete()
t.test_split()
t.test_avl_to_array()

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAVLTree))
runner = unittest.TextTestRunner()
runner.run(suite)

