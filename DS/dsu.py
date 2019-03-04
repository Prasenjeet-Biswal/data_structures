class DSU(object):
	def __init__(self, n):
		self.size = n
		self.rank = [0]*n
		self.par = range(n)

	def find(self, x):
		if self.par[x]==x:
			return x
		else:
			par[x]=self.find(par[x])
		return par[x]

	def union(self, x, y):
		px  = self.find(x)
		py = self.find(y)
		if px==py:
			return False
		elif self.rank[px]<self.rank[py]:
			self.par[py]=px
		elif self.rank[py]<self.rank[px]:
			self.par[px]=py
		elif self.rank[px]==self.rank[py]:
			self.par[px]=py
			self.rank[px]+=1
		return True



		
		
