from avl_template import *

# MIN_KEY = 1
# MAX_KEY = 50
#
# NODES =  [11, 4,7, 23,15, 40, 30, 43 ]
#
# tree = AVLTree()
# for i in range(len(NODES)):
#     tree.insert(NODES[i], "")
#
# tree.print_tree()
#
# print("*******")
# node = tree.search(7)
# print(tree.delete(node))
# tree.print_tree()

keys1 = [4,2,5]
keys2 = [20, 22, 16, 18, 14]

tree1 = AVLTree()
for i in range(len(keys1)):
    tree1.insert(keys1[i], "")
tree1.print_tree()
print("***********")
tree2 = AVLTree()
for i in range(len(keys2)):
    tree2.insert(keys2[i], "")
tree2.print_tree()
print("***********")
tree2.join(tree1,10,"")
tree2.print_tree()