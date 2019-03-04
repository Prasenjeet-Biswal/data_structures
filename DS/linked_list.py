import os, re, sys

class SLNode:
	def __init__(self, val):
		self.data=val
		self.next=None

	def get_data(self):
		return self.data

	def set_data(self, val):
		self.data=val

class DLNode:
	def __init__(self, val):
		self.data=val
		self.next=None
		self.prev=None

	def get_data(self):
		return self.data

	def set_data(self, val):
		self.data=val


class SLL:
	def __init__(self):
		self.head=None
		self.tail=None
		self.size=0

	def insertAtEnd(self, val):
		t = SLNode(val)
		if self.tail==None:
			self.tail=t
			self.head=t
		else:
			self.tail.next=t
			self.tail=tail.next
		self.size+=1

	def insertAtStart(self, val):
		t = SLNode(val)
		if self.head=None:
			self.head=t
			self.tail=t
		else:
			t.next=self.head
			self.head=t
		self.size+=1

	def traverseForward(self):
		node=self.head
		result=[]
		while node!=None:
			result.append(node.data)
			node=node.next

	def traverseBackward(self):
		## not possible will have to insert the values in the start.
		node=self.head
		result=[]
		while node!=None:
			result.insert(0, node.data)
			node=node.next

	def search(self, val, rtype):
		node=self.head
		while node!=None:
			if node.data==val:
				if rtype==bool:
					return True
				else:
					return node
			node=node.next
		if rtype==bool:
			return False
		else:
			return None

	def deletefromStart(self):
		if self.head==None:
			pass
		elif self.head==self.tail:
			self.head=None
			self.tail=None
		else:
			node=self.head.next
			prev=self.head
			while node.next!=None

	def deleteFromEnd(self):
		if self.tail==None:
			pass
		elif self.head==self.tail:
			self.head=None
			self.tail=None
		else:
			node=self.head.next
			prev=self.head
			while node.next!=None:
				prev=prev.next
				node=node.next


	def deleteGivenNode(self, node):
		if node==None:
			pass
		elif node.next==None:
			node=None
		else:
			node.data=node.next.data
			node.next=node.next.next
		self.size-=1

	def delete(self, val):
		node = self.search(val, None)
		if node!=None:
			self.deleteGivenNode(node)
			self.size-=1

class DLL:
	def __init__(self):
		self.head=None
		self.tail=None
		self.size=0

	def insertAtEnd(self, val):
		t = DLNode(val)
		if tail==None:
			tail=t
			head=t
		else:
			tail.next=t
			t.prev=tail
			tail=tail.next
		self.size+=1

	def insertAtStart(self, val):
		t = DLNode(val)
		if head==None:
			head=t
			tail=t
		else:
			head.prev=t
			t.next=head
			head=head.prev
		self.size+=1

	def traverseForward(self):
		node=self.head
		result=[]
		while node!=None:
			result.append(node.data)
			node=node.next

	def traverseBackward(self):
		node=self.tail
		result=[]
		while node!=None:
			result.append(node.data)
			node=node.prev

	def search(self, val, rtype):
		node=self.head
		while node!=None:
			if node.data==val:
				if rtype==bool:
					return True
				else:
					return node
			node=node.next
		if rtype==bool:
			return False
		else:
			return None

	def deleteGivenNode(self, node):







