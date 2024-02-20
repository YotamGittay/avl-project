

from AVLTree import  AVLTree
from graph_tree import draw_binary_tree

nodes = [79, 54, 23, 9, 31, 84, 7, 3, 77, 55, 86, 17, 1, 84, 3, 80, 15, 10, 62, 13, 14, 43, 66, 2, 16, 27, 29, 62, 40, 94]
tree = AVLTree()
for k in nodes:
    tree.insert(k, k)
print(tree.is_avl())

for k in nodes:
    node = tree.search(k)
    tree.delete(node)
    tree.print_tree()
    if not tree.is_avl():
        print("badddddddd")
        break



