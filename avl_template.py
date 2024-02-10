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
			self.last_height = -1
			self.left = None
			self.right = None
		else: # if node is real
			self.size = 1
			self.height = 0
			self.last_height = 0
		

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

	def get_last_height(self):
		return self.last_height

	def get_size(self):
		return self.size


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):  # sets left son of current node
		if self.is_real_node():
			self.left = node
			node.set_parent(self)
			self.fix_size()  # fix the size of current node
			self.fix_height()   # fix the height of current node



	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node : 'AVLNode'):
		if self.is_real_node():
			self.right = node
			node.set_parent(self)
			self.fix_size()
			self.fix_height()

	def fix_size(self):
		new_size = 1 + self.get_left().get_size() + self.get_right().get_size()
		self.set_size(new_size)

	def fix_height(self):
		self.set_height(max(self.get_left().get_height() + 1, self.get_right().get_height() +1))

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
		self.last_height = self.height
		self.height = h

	def set_size(self, size):
		self.size = size


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if self.get_key() == None:
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
		


	def print_node(self):
		"""Prints the details of the AVL node."""
		if self.is_real_node():
			print("Key:", self.key)
			print("Value:", self.value)
			print("Height:", self.height)
			print("BF:", self.get_bf())
			print("Size:", self.size)
			print("Parent:", self.parent.key if self.parent else None)
			print("Left Child:", self.left.key if self.left.is_real_node() else None)
			print("Right Child:", self.right.key if self.right.is_real_node() else None)
		else:
			print("Virtual Node")







"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self, root = None):  # probebly need to add more fields
		self.root = root
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

	def delete_by_key(self, key):
		node = self.search(key)
		self.delete(node)


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
	def insert(self, key, val):  # still has some issues with large trees, cand find problem

		# find where to insert new node 
		if self.root == None:
			self.root = AVLNode(key, val)
			return 0
		
		curr = self.root
		parent = None # To keep track of the parent for the new insertion
		while curr.is_real_node():  
			parent = curr
			if key == curr.get_key(): # Update the value if the key already exists
				return 0
			if key < curr.get_key():
				curr = curr.left
			elif key > curr.get_key():
				curr = curr.right

		new_node = AVLNode(key, val)
		if key < parent.get_key():
			parent.set_left(new_node)
		else:
			parent.set_right(new_node)

		# rebalance from the new node to the root, if needed
		self.update_ancestors_heights(new_node)
		suspect = parent
		rotations = 0
		while suspect != None:
			temp = self.rebalance(suspect) # rebalance node and return the number of rotations
			rotations += temp
			suspect = suspect.get_parent()
		return rotations




	def rebalance(self, node : 'AVLNode'):
		rotations = 0
		if node.get_bf() == 2: # node is left heavy
			if node.get_left().get_bf() >= 0: # left chile of node is left heavy
				self.right_rotation(node)
				rotations += 1
			elif node.get_left().get_bf() <= 0: # left child of node is right heavy
				self.left_rotation(node.get_left())
				self.right_rotation(node)
				rotations += 2

		elif node.get_bf() == -2: # node is right heavy
			if node.get_right().get_bf() <= 0: # right child of node is right heavy
				self.left_rotation(node)
				rotations += 1
			elif node.get_right().get_bf() >= 0: # right child of node is left heavy
				self.right_rotation(node.get_right())
				self.left_rotation(node)
				rotations += 2
		return rotations

	def right_rotation(self, B):
		# according to slide 55 on presentation
		parent = B.get_parent()
		A = B.get_left()
		AR = A.get_right()
		# put AR
		AR.set_parent(B)
		B.set_left(AR)
		# put B
		B.set_parent(A)
		A.set_right(B)
		if parent != None:
			if parent.get_right() == B:
				parent.set_right(A)
			else:
				parent.set_left(A)
		else:
			# node was root
			self.set_root(A)
		A.set_parent(parent)
		# fix heights
		A.fix_height()
		B.fix_height()
		# fix sizes
		A.fix_size()
		B.fix_size()

	def left_rotation(self, B):
		# according to slide 55 on presentation
		parent = B.get_parent()
		A = B.get_right()
		AL = A.get_left()
		# put AL
		AL.set_parent(B)
		B.set_right(AL)
		# put B
		B.set_parent(A)
		A.set_left(B)
		if parent != None:
			if parent.get_right() == B:
				parent.set_right(A)
			else:
				parent.set_left(A)
		else:
			# node was root
			self.set_root(A)
		A.set_parent(parent)
		# fix heights
		A.fix_height()
		B.fix_height()
		# fix sizes
		A.fix_size()
		B.fix_size()

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		pysicallyDeletedParent = self.delete_BST(node)
		parent = pysicallyDeletedParent
		counter = 0
		while parent!= None and parent.is_real_node():
			balance_factor = parent.get_bf()
			if abs(balance_factor) < 2 and parent.get_last_height() == parent.get_height():
				return counter
			elif abs(balance_factor) < 2 and parent.get_last_height() != parent.get_height():
				parent = parent.get_parent()
			else:
				next_parent = parent.get_parent()
				counter += self.rebalance_delete(parent)
				parent = next_parent
		return counter

	def rebalance_delete(self, parent):
		balance_factor = parent.get_bf()
		counter = 0
		if balance_factor == 2:
			if parent.get_left().get_bf() in [0,1]:
				self.right_rotation(parent)
				counter += 1
			else:
				self.left_rotation(parent.get_left())
				self.right_rotation(parent)
				counter += 2
		else:
			if parent.get_left().get_bf() in [0,-1]:
				self.left_rotation(parent)
				counter += 1
			else:
				self.right_rotation(parent.get_right())
				self.left_rotation(parent)
				counter += 2
		return counter

	def delete_BST(self, node):
		if node == None or not node.is_real_node():
			return
		if node.is_leaf():
			parent = self.delete_leaf(node)
		elif not node.get_right().is_real_node() or not node.get_right().is_real_node():
			parent = self.delete_easy(node)
		else:
			parent = self.delete_by_successor(node)
		self.update_ancestors_heights(parent)
		return parent


	def delete_leaf(self, node):
		if node == None or not node.is_real_node():
			return
		if node == self.get_root():
			# delete root, not supposed to happen but just in case
			self.root = None
			return
		parent = node.get_parent()
		fake_node = AVLNode(None, None)
		if parent.get_left() == node:
			parent.set_left(fake_node)
		else:
			parent.set_right(fake_node)
		return parent

	def delete_easy(self, node):
		if node == None or not node.is_real_node():
			return
		parent = node.parent
		if not node.get_left().is_real_node():
			# doesn't have left child
			child = node.get_right()
			if parent.get_left() == node:
				parent.set_left(child)
				child.set_parent(parent)
				# remove node parent and child
				node.set_parent(None)
				node.set_right(AVLNode(None, None))
			else:
				parent.set_right(child)
				child.set_parent(parent)
				# remove node parent and child
				node.set_parent(None)
				node.set_left(AVLNode(None, None))
		else:
			# doesn't have right child
			child = node.get_left()
			if parent.get_left() == node:
				parent.set_left(child)
				child.set_parent(parent)
				# remove node parent and child
				node.set_parent(None)
				node.set_left(AVLNode(None, None))
			else:
				parent.set_left(child)
				child.set_parent(parent)
				# remove node parent and child
				node.set_parent(None)
				node.set_left(AVLNode(None, None))
		# change attributes of nodes
		node.set_height(0)
		return child.parent

	def delete_by_successor(self, node):
		successor = self.successor(node)
		successorParent = successor.get_parent()
		isRoot = node == self.root
		# delete successor
		self.delete(successor)
		# connect successor to the node
		successor.set_parent(node.get_parent())
		successor.set_right(node.get_right())
		successor.set_left(node.get_left())
		successor.set_height(node.get_height())
		# connect successor to parent
		if node.get_parent() != None and node.get_parent().is_real_node():
			if node.get_parent().get_left() == node:
				node.get_parent().set_left(successor)
			else:
				node.get_parent().set_right(successor)
		# disconnect node
		node.set_parent(None)
		node.set_right(AVLNode(None, None))
		node.set_left(AVLNode(None, None))
		node.set_height(0)
		# check if root
		if isRoot:
			self.root = successor
		return successorParent

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
		#recursive helper- append (key, value) pairs in order of keys
		def avl_to_array_rec(node : 'AVLNode', array): 
			if node is None or not node.is_real_node():
				return
			avl_to_array_rec(node.get_left(), array)
			array.append((node.get_key(), node.get_value()))
			avl_to_array_rec(node.get_right(), array)

		array = []
		avl_to_array_rec(self.get_root(), array)
		return array


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.root.get_size()

	
	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node : 'AVLNode'): # using joins
		sm_tree = AVLTree()
		bg_tree = AVLTree()

		sm_tree.join(AVLTree(node.get_left)) # seperate left and right subtrees of node
		bg_tree.join(AVLTree(node.get_right))

		curr = node
		while curr is not None: # split rest of the tree 
			parent = curr.get_parent()
			if curr.what_child() is None: # made it to the root
				return
			if curr.what_child() == "R": # if curr is right child to its father
				parent.set_right(AVLNode(None, None)) # disconnect father from right child
				sm_tree.insert(parent) 
				sm_tree.join(AVLTree(parent.get_left()))
			if curr.what_child() == "L": # if curr is left child of its father
				parent.set_left(AVLNode(None, None)) # disconnect father from left child
				bg_tree.insert(parent)
				bg_tree.join(AVLTree(parent.get_right()))

		

	
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
		separate_node = AVLNode(key, val)
		sm_tree = AVLTree()
		bg_tree = AVLTree()
		
		# Determine the smaller and bigger tree
		if self.root.size >= tree2.root.size:
			bg_tree, sm_tree = self, tree2
		else:
			bg_tree, sm_tree = tree2, self

		# Traverse down the bigger tree to find the correct position
		b = bg_tree.root
		parent_b = None
		while b and b.size >= sm_tree.root.size:
			parent_b = b
			b = b.get_left()

		# Reconfigure the tree structure
		if b:
			separate_node.set_right(b)
			b.set_parent(separate_node)
		if parent_b:
			parent_b.set_left(separate_node)
		else:  # separate_node becomes new root
			bg_tree.set_root(separate_node)

		separate_node.set_left(sm_tree.root)
		sm_tree.root.set_parent(separate_node)

		# Rebalance the tree starting from separate_node upwards
		rotations = 0
		curr = separate_node
		while curr:
			rotations += bg_tree.rebalance(curr)
			curr = curr.get_parent()

		return bg_tree


		



	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root

	def set_root(self, root):
		self.root = root

	def print_tree(self):
		"""Prints the AVL tree."""
		self.print_tree_recursive(self.root, 0)

	def print_tree_recursive(self, node, depth):
		"""Recursive helper function for printing the AVL tree."""
		if node is not None and node.is_real_node():
			self.print_tree_recursive(node.get_right(), depth + 1)
			print("    " * depth + str(node.get_key()) + ":" + str(node.get_value()) + " (Height: " + str(node.get_height()) + ")" + " (BF: " + str(node.get_bf()) + ")"  )
			self.print_tree_recursive(node.get_left(), depth + 1)



	def is_avl(self):
		def is_avl_tree_rec(node : 'AVLNode', bf, keys):
			if node is None or not node.is_real_node():
				return
			
			is_avl_tree_rec(node.left , bf, keys)
			bf.append(node.get_bf())
			keys.append(node.get_key())
			is_avl_tree_rec(node.right, bf, keys)
		
		bf = []
		keys = []
		is_avl_tree_rec(self.get_root(), bf, keys)

		is_balnced = True
		for k in bf:
			if abs(k) > 1:
				is_balnced = False
				break
		
		
		is_bst = all(keys[i] <= keys[i+1] for i in range(len(keys)-1))

		return is_balnced and is_bst
	


