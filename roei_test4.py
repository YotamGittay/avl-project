from AVLTree import *

keys = [68, 94, 96, 29, 0, 71, 83, 87, 63, 24, 50, 49, 18, 72, 21, 58, 96, 89, 41, 68, 15, 25, 57, 21, 44, 100, 84, 28, 0, 86]

tree1 = AVLTree()
for i in range(len(keys)):
    tree1.insert(keys[i], "")
tree1.print_tree()
print("*******************")
to_delete = keys[0:7]
for i in range(len(to_delete)):
    print("*******************")
    tree1.print_tree()
    tree1.delete_by_key(to_delete[i])

tree1.print_tree()



