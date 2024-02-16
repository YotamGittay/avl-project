from avl_template import *
from graph_tree import draw_binary_tree
from UnitTestAVLTree import TestAVLTree

# MIN_KEY = 1
# MAX_KEY = 50
#
# NODES_1 = [30,31,32,33,34,35]
# NODES_2 = [24,25,26]
#
# tree1 = AVLTree()
# for i in range(len(NODES_1)):
#     tree1.insert(NODES_1[i], "")
# tree2 = AVLTree()
# for i in range(len(NODES_2)):
#     tree2.insert(NODES_2[i], "")
# tree1.join(tree2, 29, "")
#
# NODES_1 = [31,30,32]
# NODES_2 = [34,35]

# tree1 = AVLTree()
# for i in range(len(NODES_1)):
#     tree1.insert(NODES_1[i], "")
# tree2 = AVLTree()
# for i in range(len(NODES_2)):
#     tree2.insert(NODES_2[i], "")
# tree1.join(tree2, 33, "")
#
# tree1.print_tree()

#draw_binary_tree( split2[1].get_root() )

test = TestAVLTree()
test.test_avl_delete_node_with_two_rotations()
test.test_avl_delete_leaf_node()
test.test_avl_avl_to_array()
test.test_avl_insert_rebalance()
test.test_avl_insert_rebalance2()
test.test_avl_insert_rebalance_large_tree()14