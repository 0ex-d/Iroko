'''
Binary Tree 
March 09, 2017
'''

#!/usr/bin/env python3

import random
import subprocess

class Node():
	def __init__(self, key, value):
		self.key = key
		self.value =  value
		self._left = None
		self._right = None

	@property
	def left(self):
		return self._left

	@left.setter
	def left(self, value):
		self._left = value

	@property
	def right(self):
		return self._right

	@right.setter
	def right(self, value):
		self._right = value

class Tree():
	def __init__(self, key=lambda x: id(x)):
		self._root = None
		self._key = key

	def _insert(self, node, subtree):
        if node.key <= subtree.key:
            if subtree.left is None:
                subtree.left = node
            else:
                self._insert(node, subtree.left)
        else:
            if subtree.right is None:
                subtree.right = node
            else:
                self._insert(node, subtree.right)

    def insert(self, value):
        node = Node(self._key(value), value)
        if self._root is None:
            self._root = node
        else:
            self._insert(node, self._root)

def _prepare_data():
	return (0, 1, 2, 3, 4, 5, 6, 7)

if __name__ == "__main__":
	data = _prepare_data()

	tree = Tree(lambda x: x)
	
	for item in data:
		tree.insert(item)