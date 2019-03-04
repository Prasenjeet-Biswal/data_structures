import os, sys, re
from linked_list import SLL

class Stack:
	def __init__(self):
		self.stack=SLL()


	def push(self, val):
		self.stack.insertAtEnd(val)

	def pop(self):
		self.stack.deleteFromEnd()

	def getSize(self):
		return self.stack.size

	def isEmpty(self):
		return self.getSize()==0


