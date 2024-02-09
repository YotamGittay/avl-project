#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  

from typing import Optional
import random




"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value): # constructor of node
		self.key = key
		self.value = value
		if key is not None: # if node is real create 2 virtual childes
			self.left = AVLNode(None, None)
			self.right = AVLNode(None, None)
		self.parent = None
		if key is None:  # check if node is virtual
			self.size = 0
			self.height = -1
			self.left = None
			self.right = None
		else: # if node is real
			self.size = 1
			self.height = 0
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self) -> 'Optional[AVLNode]':
		return self.left



	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self) -> 'Optional[AVLNode]':  
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height
	
	def get_size(self):
		return self.size


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):  # sets left son of current node
		self.left = node
		node.set_parent(self)
		self.fix_size()  # fix the size of current node
		self.fix_height()   # fix the height of current node



	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node : 'AVLNode'):
		self.right = node
		node.set_parent(self)
		self.fix_size()
		self.fix_height()

	def fix_size(self):
		new_size = 1 + self.get_left().get_size() + self.get_right().get_size()
		self.set_size(new_size)

	def fix_height(self):
		self.set_height(max(self.left.height, self.right.height) + 1)

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h

	def set_size(self, size):
		self.size = size


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if self.get_key == None:
			return False
		return True

	def get_height(self):
		return self.height

	def get_bf(self):
		if self.is_real_node():
			return self.get_left().get_height() - self.get_right().get_height()
		return 0

	"""returns whether self is a leaf 

		@rtype: bool
		@returns: True if self is a leaf , False otherwise 
	"""
	def is_leaf(self):
		if((not self.left.is_real_node()) and (not self.right.is_real_node())):
			return True
		return False


	def is_criminal(self): # checks if a node is avl criminal, means its bf > 1 or < -1 
		bf = self.get_bf()
		if bf < -1 or bf > 1:
			return True
		return False
	
	def what_child(self): # checks what child is the node to its father (left or right)
		if self.get_parent() == None: # node has no father
			return None
		if self.get_parent().get_left() == self:
			return "L"
		if self.get_parent().get_right() == self:
			return "R"
		
	
	def rotate_right(self, other : 'AVLNode'): # need to check end cases
		self.set_left(other.get_right()) # b.left <- a.right
		self.get_left().set_parent(self) # b.left.parent <- b
		other.set_right(self) # a.right <- b
		other.set_parent(self.get_parent) # a.parent <- b.parent
		if self.what_child() == "L":  # a.parent.left/right <- a
			self.get_parent().set_left(self)
		if self.what_child() == "R":
			self.get_parent().set_right(self)
		self.set_parent(other) # b.parent <- other


	def rotate_left(self, other : 'AVLNode'): 
		self.set_right(other.get_left()) # b.right <- a.left
		self.get_right().set_parent(self) # b.right.parent <- b
		other.set_left(self) # a.left <- b
		other.set_parent(self.get_parent) # a.parent <- b.parent
		if self.what_child() == "L":  # a.parent.left/right <- a
			self.get_parent().set_left(self)
		if self.what_child() == "R":
			self.get_parent().set_right(self)
		self.set_parent(other) # b.parent <- other






		############################################### IGNORE- JUST FOR TESTS



"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):  # probebly need to add more fields
		self.root = None
		self.size = 0



	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
	def search(self, key):  
		return self.binary_search(self.root, key)

	def binary_search(self, node, key):
		if node == None or not node.is_real_node():
			return None
		if node.key == key:
			return node
		if node.key < key:
			return self.binary_search(node.right, key)
		return self.binary_search(node.left, key)


	def successor(self, node):  # returns successor of node
		if not node.is_real_node():  # if node is virtual
			return None
		if node.get_right().is_real_node():  # if node has right child
			curr = node.get_right()
			while curr.left.is_real_node(): 
				curr = curr.get_left()
			return curr
		parent = node.get_parent()  # if node doesnt have right chile 
		while parent != None and parent.right == node:  
			node = parent
			parent = parent.get_parent()
		return parent
	


	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val): # what if key is in the tree already?
		new_node = AVLNode(key, val)
		# find where to insert new node 
		if self.root == None:
			self.root = AVLNode(key, val)
			return None
		curr = self.root
		if curr is None:
			return None
		while curr.key is not None:  # while node is real
			if key < curr.get_key():
				if not curr.get_left().is_real_node():
					curr.set_left(new_node)
					break
				else: 
					curr = curr.get_left()
			elif key > curr.get_key():
				if not curr.get_right().is_real_node():
					curr.set_right(new_node)
					break
				else:
					curr = curr.get_right()
		self.update_ancestors_heights(new_node)
		# rebalance
		suspect = curr
		rotations = 0
		while suspect.is_criminal():
			temp = suspect.rebalance() # rebalance node and return the number of rotations
			if temp > 0:
				rotations += temp
				break # break atfer first rotate
			suspect = suspect.get_parent()
		return rotations
	

	def rebalance(self, node : 'AVLNode'):
		rotations = 0
		if node.get_bf == 2: # node is left heavy
			if node.get_left().get_bf() == 1: # left chile of node is left heavy
				node.rotate_right(node.get_left())
				rotations += 1
			elif node.get_left().get_bf() == -1: # left child of node is right heavy
				node.get_left().rotate_left(node.get_left().get_right())
				node.rotate_right(node.get_left())
				rotations += 2

		elif node.get_bf == -2: # node is right heavy
			if node.get_right().get_bf() == -1: # right child of node is right heavy
				node.rotate_left(node.get_left())
				rotations += 1
			elif node.get_right().get_bf() == 1: # right child of node is left heavy
				node.get_left().rotate_right(node.get_right().get_left)
				node.rotate_left(node.get_right())
				rotations += 2






	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		if not node.is_real_node() or node == None:
			return
		if node.is_leaf():
			parent = self.deleteLeaf(node)
		elif not node.get_right.is_real_node() or not node.get_right.is_real_node():
			parent = self.deleteEasy(node)
		else:
			parent = self.deleteBySuccessor(node)
		self.update_ancestors_heights(parent)

	def deleteLeaf(self, node):
		if node == self.root:
			# delete root, not supposed to happen but just in case
			self.root = None
		parent = node.parent
		fake_node = AVLNode()
		if parent.getLeft() == node:
			parent.setLeft(fake_node)
		else:
			# right node
			parent.setRight(fake_node)

	def update_ancestors_heights(self, node):
		parent = node
		while parent != None and parent.is_real_node():
			parent.fix_height()
			parent = parent.get_parent()



	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return -1	

	
	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None

	
	"""joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree2, key, val):
		return None


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return None

	def _print_tree(self):
		"""Prints the AVL tree."""
		self._print_tree_recursive(self.root, 0)

	def _print_tree_recursive(self, node, depth):
		"""Recursive helper function for printing the AVL tree."""
		if node is not None and node.is_real_node():
			self._print_tree_recursive(node.get_right(), depth + 1)
			print("    " * depth + str(node.get_key()) + ":" + str(node.get_value()))
			self._print_tree_recursive(node.get_left(), depth + 1)
	

#### IGNORE
	
	



tree = AVLTree()



# Constants for random number generation
MIN_KEY = 1
MAX_KEY = 1000
NUM_NODES = 50

# Generate and insert 50 random nodes
for _ in range(NUM_NODES):
    # Generate a random key and value
    key = random.randint(MIN_KEY, MAX_KEY)
    value = f"Value for key {key}"  # Example value format

    # Insert the new node into the AVL tree
    tree.insert(key, value)

print(tree.root.key)
tree.print_tree()