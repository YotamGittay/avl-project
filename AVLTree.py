#username1 - yotamgittay
#id1      - 208003111
#name1    - yotam gittay
#username2 - roeil
#id2      - 206776304
#name2    - roei levinson

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
	Time complexity: O(1)
	"""
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	Time complexity: O(1)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	Time complexity: O(1)
	"""
	def get_parent(self):
		return self.parent


	"""returns the key
	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	Time complexity: O(1)
	"""
	def get_key(self):
		return self.key


	"""returns the value
	@rtype: any
	@returns: the value of self, None if the node is virtual
	Time complexity: O(1)
	"""
	def get_value(self):
		return self.value


	"""returns the height
	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	Time complexity: O(1)
	"""
	def get_height(self):
		return self.height

	"""returns the last height
	@rtype: int
	@returns: the last height of self
	Time complexity: O(1)
	"""
	def get_last_height(self):
		return self.last_height

	"""returns the size
	@rtype: int
	@returns: the size of the subtree of self as a root
	Time complexity: O(1)
	"""
	def get_size(self):
		return self.size


	"""sets left child
	@type node: AVLNode
	@param node: a node
	Time complexity: O(1)
	"""
	def set_left(self, node):  # sets left son of current node
		if self.is_real_node():
			self.left = node
			node.set_parent(self)
			self.fix_size()  # fix the size of current node


	"""sets right child
	@type node: AVLNode
	@param node: a node
	Time complexity: O(1)
	"""
	def set_right(self, node : 'AVLNode'):
		if self.is_real_node():
			self.right = node
			node.set_parent(self)
			self.fix_size()

	"""fixes the size of the node
	@returns: None 
	Time complexity: O(1)
	"""
	def fix_size(self):
		new_size = 1 + self.get_left().get_size() + self.get_right().get_size()
		self.set_size(new_size)

	"""fixes the height of the node
	@returns: None 
	Time complexity: O(1)
	"""
	def fix_height(self):
		self.set_height(max(self.get_left().get_height() + 1, self.get_right().get_height() +1))

	"""checks the height of the node
	@type: boolean
	@returns: True if the height is the correct height based on the children
	Time complexity: O(1) 
	"""
	def is_correct_height(self):
		return max(self.get_left().get_height() + 1, self.get_right().get_height() +1) == self.get_height()
	"""sets parent
	@type node: AVLNode
	@param node: a node
	Time complexity: O(1)
	"""
	def set_parent(self, node):
		self.parent = node

	"""sets key
	@type key: int or None
	@param key: key
	Time complexity: O(1)
	"""
	def set_key(self, key):
		self.key = key

	"""sets value
	@type value: any
	@param value: data
	Time complexity: O(1)
	"""
	def set_value(self, value):
		self.value = value


	"""sets the height of the node
	@type h: int
	@param h: the height
	Time complexity: O(1)
	"""
	def set_height(self, h):
		self.last_height = self.height
		self.height = h

	"""sets the size of the node
	@type size: int
	@param size: the size
	Time complexity: O(1)
	"""
	def set_size(self, size):
		self.size = size

	"""returns whether self is not a virtual node 
	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	Time complexity: O(1)
	"""
	def is_real_node(self):
		if self.get_key() == None:
			return False
		return True

	"""returns the height
	@rtype: int
	@returns: the height of the node in the tree
	Time complexity: O(1)
	"""
	def get_height(self):
		return self.height

	"""returns the balance factor
	@rtype: int
	@returns: the balance factor of the node in the tree
	Time complexity: O(1)
	"""
	def get_bf(self):
		if self.is_real_node():
			return self.get_left().get_height() - self.get_right().get_height()
		return 0

	"""returns whether self is a leaf 
	@rtype: bool
	@returns: True if self is a leaf , False otherwise
	Time complexity: O(1) 
	"""
	def is_leaf(self):
		if((not self.left.is_real_node()) and (not self.right.is_real_node())):
			return True
		return False

	"""returns the max node in the tree from self 
	@rtype: AVL Node
	@returns: the node with max key in the subtree from self and forward
	Time complexity: O(h) where h is the height of the subtree
	"""
	def get_max(self):
		curr = self
		while curr.is_real_node():
			prev = curr
			curr = curr.right
		return prev


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self, root = None):  
		self.root = root
		self.costs = []

	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	Time complexity: O(log(n)) 
	"""
	def search(self, key):  
		return self.binary_search(self.root, key)

	"""returns the size of the tree  

	@rtype: int
	@returns: the size of the tree (from root)
	Time complexity: O(1)
	"""
	def size(self):
		return self.get_root().get_size()

	"""searches the node with key, starting from node
	@type key: int
	@param key: a key to be searched
	@type node: AVL Node
	@param node: starting node
	@rtype: AVL Node
	@returns: if exists, the node with key value the same as key, None otherwise
	Time complexity: O(log(n)) 
	"""
	def binary_search(self, node, key):
		if node == None or not node.is_real_node():
			return None
		if node.key == key:
			return node
		if node.key < key:
			return self.binary_search(node.right, key)
		return self.binary_search(node.left, key)

	"""searches the successor node
	@type node: AVL Node
	@param node: a node to get the successor of
	@rtype: AVL Node
	@returns: if exists, node that follows it if the keys are arranged in ascending order, None otherwise
	Time complexity: O(log(n)) 
	"""
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

	"""inserts key, val at in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	Time complexity: O(log(n)) 
	"""
	def insert(self, key, val):  
		# find where to insert new node 
		if self.root == None or not self.root.is_real_node():
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
			suspect.fix_height()
			suspect.fix_size()
			suspect = suspect.get_parent()
		return rotations

	"""rebalances the node
	@type node: AVL Node
	@param node: a node to rebalance 
	@returns: None
	Time complexity: O(1)
	"""
	def rebalance(self, node):
		rotations = 0
		if node.get_bf() == 2: # node is left heavy
			if node.get_left().get_bf() >= 0: # left chile of node is left heavy
				rotations += self.right_rotation(node)
			elif node.get_left().get_bf() <= 0: # left child of node is right heavy
				rotations += self.left_rotation(node.get_left())
				rotations += self.right_rotation(node)
		elif node.get_bf() == -2: # node is right heavy
			if node.get_right().get_bf() <= 0: # right child of node is right heavy
				rotations += self.left_rotation(node)
			elif node.get_right().get_bf() >= 0: # right child of node is left heavy
				rotations += self.right_rotation(node.get_right())
				rotations += self.left_rotation(node)
		return rotations

	"""executes right rotation 
	@type node: AVL Node
	@param node: a node to rotate with his left child
	@returns: None
	Time complexity: O(1)
	"""
	def right_rotation(self, B):
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
		if not B.is_correct_height():
			B.fix_height()
		if not A.is_correct_height():
			A.fix_height()
		# fix sizes
		B.fix_size()
		A.fix_size()
		return 1

	"""executes left rotation 
	@type node: AVL Node
	@param node: a node to rotate with his right child
	@returns: None
	Time complexity: O(1)
	"""
	def left_rotation(self, B):
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
		if not B.is_correct_height():
			B.fix_height()
		if not A.is_correct_height():
			A.fix_height()
		# fix sizes
		B.fix_size()
		A.fix_size()
		return 1

	"""deletes node from the dictionary
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	Time complexity: O(log(n))
	"""
	def delete(self, node):
		if node == None :
			return 0
		(pysicallyDeletedParent, counter) = self.delete_BST(node)
		parent = pysicallyDeletedParent
		while parent!= None and parent.is_real_node():
			if not parent.is_correct_height():
				parent.fix_height()
			balance_factor = parent.get_bf()
			if abs(balance_factor) < 2 and parent.get_last_height() == parent.get_height():
				# parent = parent.get_parent()
				return counter
			elif abs(balance_factor) < 2 and parent.get_last_height() != parent.get_height():
				parent = parent.get_parent()
			else:
				next_parent = parent.get_parent()
				counter += self.rebalance_delete(parent)
				parent = next_parent
		return counter

	"""rebalances the node after delete
	@type node: AVL Node
	@param node: a node to rebalance, with special treatment to cases after deletion
	@returns: None
	Time complexity: O(1) 
	"""
	def rebalance_delete(self, parent):
		if parent == None or not parent.is_real_node():
			return
		balance_factor = parent.get_bf()
		counter = 0
		if balance_factor == 2:
			if parent.get_left().get_bf() in [0,1]:
				counter += self.right_rotation(parent)
			else:
				counter += self.left_rotation(parent.get_left())
				counter += self.right_rotation(parent)
		else:
			if parent.get_right().get_bf() in [0,-1]:
				counter += self.left_rotation(parent)
			else:
				counter += self.right_rotation(parent.get_right())
				counter += self.left_rotation(parent)
		return counter

	"""deletes the node from the tree, with no balancing after that
	@type node: AVL Node
	@param node: a node to delete from the BST
	@returns: None
	Time complexity: O(log(n)) 
	"""
	def delete_BST(self, node):
		if node == None or not node.is_real_node():
			return (None, 0)
		if node.is_leaf():
			(parent, counter) = self.delete_leaf(node)
		elif not node.get_left().is_real_node() or not node.get_right().is_real_node():
			(parent, counter) = self.delete_easy(node)
		else:
			(parent, counter) = self.delete_by_successor(node)
		counter2 = self.update_ancestors_heights(parent)
		return (parent, counter2+counter)

	"""deletes a leaf from the tree, with no balancing after that
	@type node: AVL Node
	@param node: a leaf to delete from the BST
	@returns: None
	Time complexity: O(1)
	"""
	def delete_leaf(self, node):
		counter = 0
		if node == None or not node.is_real_node():
			return (None, counter)
		if node == self.get_root():
			# delete root, not supposed to happen but just in case
			self.root = None
			return (None, counter)
		parent = node.get_parent()
		fake_node = AVLNode(None, None)
		if parent.get_left() == node:
			parent.set_left(fake_node)
		else:
			parent.set_right(fake_node)
		return (parent, counter)

	"""deletes a node from the tree in case of easy delete (like was shown in the lecture), with no balancing after that
	@type node: AVL Node
	@param node: a node to delete from the BST
	@returns: None
	Time complexity: O(1)
	"""
	def delete_easy(self, node):
		counter = 0
		if node == None or not node.is_real_node():
			return (None, counter)
		# special case for root
		if node == self.get_root():
			if node.get_left().is_real_node():
				child = node.get_left()
				self.set_root(child)
			else:
				# node has right child
				child = node.get_right()
				self.set_root(child)
			child.set_parent(None)
			node.set_parent(None)
			node.set_right(AVLNode(None, None))
			return (None, counter)
		parent = node.get_parent()
		if not node.get_left().is_real_node():
			# doesn't have left child
			child = node.get_right()
			if parent.get_left() == node:
				parent.set_left(child)
				# child.set_parent(parent)
				# remove node parent and child
				node.set_parent(None)
				node.set_right(AVLNode(None, None))
			else:
				parent.set_right(child)
				# child.set_parent(parent)
				# remove node parent and child
				node.set_parent(None)
				node.set_right(AVLNode(None, None))
		else:
			# doesn't have right child
			child = node.get_left()
			if parent.get_left() == node:
				parent.set_left(child)
				# child.set_parent(parent)
				# remove node parent and child
				node.set_parent(None)
				node.set_left(AVLNode(None, None))
			else:
				parent.set_right(child)
				# child.set_parent(parent)
				# remove node parent and child
				node.set_parent(None)
				node.set_left(AVLNode(None, None))
		# change attributes of nodes
		node.set_height(0)
		node.set_size(1)
		return (parent, counter)

	"""deletes a node from the tree in case of successor delete (like was shown in the lecture), with no balancing after that
	@type node: AVL Node
	@param node: a node to delete from the BST
	@returns: None
	Time complexity: O(log(n)) 
	"""
	def delete_by_successor(self, node):
		successor = self.successor(node)
		successorParent = successor.get_parent()
		successorParentIsNode = successorParent == node
		isRoot = node == self.root
		# delete successor
		(parent, counter) = self.delete_BST(successor)
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
		if successorParentIsNode:
			return (successor, counter)
		return (successorParent, counter)

	"""update all the ancestors sizes from node to the root
	@type node: AVL Node
	@param node: the node to start updating the ancestors from
	@returns: None
	Time complexity: O(log(n)) 
	"""
	def update_ancestors_sizes(self, node):
		while node!= None and node.is_real_node():
			node.fix_size()
			node = node.get_parent()

	"""update all the ancestors heights from node to the root
	@type node: AVL Node
	@param node: the node to start updating the ancestors from
	@returns: None
	Time complexity: O(log(n)) 
	"""
	def update_ancestors_heights(self, node):
		if node == None or not node.is_real_node():
			return 0
		counter = 0
		if not node.is_correct_height():
			counter += 1
			node.fix_height()
		parent = node.get_parent()
		while parent != None and parent.is_real_node():
			parent.fix_size()
			if not parent.is_correct_height():
				counter += 1
				parent.fix_height()
			parent = parent.get_parent()
		return counter


	"""returns an array representing dictionary 
	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	Time complexity: O(n) 
	"""
	def avl_to_array(self): 
		#recursive helper- append (key, value) pairs in order of keys
		def avl_to_array_rec(node, array):
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
	Time complexity: O(1) 
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
	Time complexity: O(log(n)) amortized, O(log(n)^2) w.c 
	"""
	def split(self, node):
		if node == None or not node.is_real_node() or self.size()==1:
			return [AVLTree(), AVLTree()]
		TSmaller = AVLTree()
		TBigger = AVLTree()
		TSmaller.set_root(node.get_left())
		TBigger.set_root(node.get_right())
		lastNode = node
		node = node.get_parent()
		while(node != None and node.is_real_node()):
			currNode = node
			nextParent = node.get_parent()
			if node.get_right() == lastNode:
				TTempSmaller = AVLTree()
				TTempSmaller.set_root(node.get_left())
				TTempSmaller.get_root().set_parent(None)
				self.costs.append(TSmaller.join(TTempSmaller, node.get_key(),  node.get_value()))
			else:
				TTempBigger = AVLTree()
				TTempBigger.set_root(node.get_right())
				TTempBigger.get_root().set_parent(None)
				self.costs.append(TBigger.join(TTempBigger, node.get_key(), node.get_value()))
			lastNode = currNode
			node = nextParent

		if TBigger.get_root() == None or not TBigger.get_root().is_real_node():
			TBigger = AVLTree()
		if TSmaller.get_root() == None or not TSmaller.get_root().is_real_node():
			TSmaller = AVLTree()
		to_return = [TSmaller, TBigger]
		return to_return

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
	Time complexity: O(log(n)) 
	"""
	def join(self, tree2, key, val):
		new_node = AVLNode(key, val)
		if tree2 is None or tree2.get_root() is None or not tree2.get_root().is_real_node():
			if self.get_root() is None or not self.get_root().is_real_node():
				self.insert(key, val)
				return 1
			else:
				height = self.get_root().get_height()
				self.insert(key, val)
				return height + 2
		elif self.get_root() is None or not self.get_root().is_real_node():
			height = tree2.get_root().get_height()
			tree2.insert(key, val)
			self.set_root(tree2.get_root())
			return height + 2
		T1 = self
		T2 = tree2

		if T1.get_root().get_height() < T2.get_root().get_height():
			TEMP = T1
			T1 = T2
			T2 = TEMP

		if T1.get_root().get_key() > new_node.get_key() and T2.get_root().get_key() < new_node.get_key():
			runningLeft = True
		else:
			runningLeft = False
		heights_diff = abs(T1.get_root().get_height() - T2.get_root().get_height())
		if not runningLeft:
			root1 = T1.get_root()
			root2 = T2.get_root()
			# go to the first node that its height is <= T1.height
			node1 = root1
			while node1.get_right() != None and node1.get_right().is_real_node() and node1.get_height() > root2.get_height():
				node1 = node1.get_right()
			cParent = node1.get_parent()
			# connect x and T1 and T2
			node1.set_parent(new_node)
			root2.set_parent(new_node)
			new_node.set_left(node1)
			new_node.set_right(root2)
			new_node.set_parent(cParent)
			if cParent != None:
				# disconnect node2
				cParent.set_right(new_node)
			else:
				# new node is connecting 2 roots
				T1.set_root(new_node)
		else:
			root1 = T2.get_root() # on purpose it's 2
			root2 = T1.get_root()
			# go to the first node that its height is <= T1.height
			node2 = root2
			while node2.get_left() != None and node2.get_left().is_real_node() and node2.get_height() > root1.get_height():
				node2 = node2.get_left()
			cParent = node2.get_parent()
			# connect x and T1 and T2
			node2.set_parent(new_node)
			root1.set_parent(new_node)
			new_node.set_right(node2)
			new_node.set_left(root1)
			new_node.set_parent(cParent)
			if cParent != None:
				# disconnect node2
				cParent.set_left(new_node)
			else:
				# new node is connecting 2 roots
				T1.set_root(new_node)
		#T2.set_root(T1.get_root())
		T1.update_ancestors_heights(new_node)
		T1.update_ancestors_sizes(new_node)
		# rebalancing
		parent = new_node
		while parent != None and parent.is_real_node():
			balance_factor = parent.get_bf()
			next_parent = parent.get_parent()
			if abs(balance_factor) >= 2:
				T1.rebalance(parent)
			parent = next_parent
		self.set_root(T1.get_root())
		return heights_diff + 1

	"""returns the root of the tree representing the dictionary
	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	Time complexity: O(1)
	"""
	def get_root(self):
		return self.root

	"""sets the root of the tree
	@type node: AVLNode
	@param node: a node
	@returns: None
	Time complexity: O(1)
	"""
	def set_root(self, root):
		self.root = root

	"""prints the tree 
	@returns: None
	Time complexity: O(n)
	"""
	def print_tree(self):
		if self.get_root() == None:
			print("The tree is empty!")
			return
		self.print_tree_recursive(self.root, 0)

	"""prints the tree recursively in certain depth and from certain node
	@returns: None
	Time complexity: O(n)
	"""
	def print_tree_recursive(self, node, depth):
		if node is not None and node.is_real_node():
			self.print_tree_recursive(node.get_right(), depth + 1)
			print("    " * depth + str(node.get_key()) + ":" + str(node.get_value()) + " (Height: " + str(node.get_height()) + ")" + " (BF: " + str(node.get_bf()) + ")" + " (Size: " + str(node.get_size()) + ")"  )
			self.print_tree_recursive(node.get_left(), depth + 1)

	"""checks if the tree is AVL Tree
	@rtype: Bool
	@returns: True if the tree is AVL Tree, False otherwise
	Time complexity: O(n)
	"""
	def is_avl(self):
		def is_avl_tree_rec(node, bf, keys):
			if node is None or not node.is_real_node():
				return
			is_avl_tree_rec(node.get_left() , bf, keys)
			bf.append(node.get_bf())
			keys.append(node.get_key())
			is_avl_tree_rec(node.get_right(), bf, keys)
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