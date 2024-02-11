from avl_template import *

MIN_KEY = 1
MAX_KEY = 50

NODES = [7,32,43,16,8,38,41,50,2,23,28,9,12]

tree = AVLTree()
for i in range(len(NODES)):
    tree.insert(NODES[i], "")
print("*******")
tree.print_tree()
node = tree.search(41)
tree.split(node)



# def tester(SIZE=100, num_of_trees=100):
#     for k in range(num_of_trees):
#         tree = AVLTree()
#         keys = [random.randint(0, 10000) for i in range(SIZE)]
#         for i in keys:
#             tree.insert(i, "")
#         if not tree.is_avl():
#             return False
#         print("insert is good!- tree number" + str(k))
#
#         for i in range(len(keys)):
#             random_element = random.choice(keys)
#             keys.remove(random_element)
#             node = tree.search(random_element)
#             tree.delete(node)
#             if not tree.is_avl():
#                 return False
#
#     return True
#
# tester(100, 100)