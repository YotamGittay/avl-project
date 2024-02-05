#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value, isFake = False): # constructor of node
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		if isFake: # if node is virtual
			self.size = 0
			self.height = -1
		else: # if node is real
			self.size = 1
			self.height = 0
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left



	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self): 
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
		self.fixSize()  # fix the size of current node
		self.fixHight()   # fix the hight of current node



	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node
		self.fix_size()
		self.fix_hight()

	def fix_size(self):
		new_size = 1 + self.get_left().get_size() + self.get_right.get_size()
		self.set_size(new_size)

	def fix_hight(self):
		self.set_height(max(self.get_left().get_hight(), self.get_right().get_left()) + 1)

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
		if self.get_value == None:
			return False
		return True
	
	def get_bf(self):
		return self.get_left().get_hight() - self.get_right().get_hight()

	"""returns whether self is a leaf 

		@rtype: bool
		@returns: True if self is a leaf , False otherwise 
	"""
	def is_leaf(self):
		if not self.left.is_real_node() and not self.right.is_real_node():
			return True
		return False



"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		# add your fields here



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


	def successor(self, node):
		if not node.is_real_node():
			return None
		if node.get_right().is_real_node():
			curr = node.get_right()
			while curr.left.is_real_node():
				curr = curr.get_left()
			return curr
		parent = node.get_parent()
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
	def insert(self, key, val):
		return -1


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
			parent = self.deleteLeaf(node);
		elif not node.get_right.is_real_node() or not node.get_right.is_real_node():
			parent = self.deleteEasy(node);
		else:
			parent = self.deleteBySuccessor(node)
		self.update_ancestors_heights(parent)
		# test2

	def deleteLeaf(self, node):
		if node == self.root:
			# delete root
			self.root = None

		parent = node.parent
		fake_node = AVLNode();
		if parent.getLeft() == node:
			parent.setLeft(fake_node)
		else:
			# right node
			parent.setRight(fake_node)

	def update_ancestors_heights(self, node):
		parent = node
		while parent != None and parent.is_real_node():
			parent.fix_heights()




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
	




	node1 = AVLNode(2, "a")
	node2 = AVLNode(3, "b")

	root = AVLNode(4, "c")

	root.
