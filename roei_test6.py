
from AVLTree import  AVLTree
from graph_tree import draw_binary_tree


keys1 = [33, 54, 29, 31]
keys2 = [23]

tree1 = AVLTree.create_tree_from_keys(keys2)
tree2 = AVLTree.create_tree_from_keys(keys1)

tree1.join(tree2, 25,"")
tree1.print_tree()