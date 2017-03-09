'''
Binary Tree 
March 09, 2017
'''

class Node():
	def __init__(self, key, value):
		self.key = key
		self.value =  value
		self._left = None
		self._right = None

	@left.setter
	def left(self, value):
		self._left = value

	def left(self):
		return self._left

	@right.setter
	def right(self, value):
		self._right = value

	def right(self):
		return self._right

if __name__ == "__main__":
	pass