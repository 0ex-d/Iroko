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

	def _insert(self, value):
		pass

	def insert(self, subtree):
		pass

if __name__ == "__main__":
	pass