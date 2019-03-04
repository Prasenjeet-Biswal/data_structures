class StringSearch:
	def __init__(self, mainString, pattern):
		self.mainString=mainString
		self.pattern=pattern
		print(self.naive_pattern_search())

	def makelsp():
		self.lsp=[0]*len(pattern)
		pass

	def naive_pattern_search(self):
		matches = []
		if self.pattern=="":
			return matches
		for i in range(len(self.mainString)):
			j=0
			while j<len(self.pattern):
				if self.mainString[i+j]!=self.pattern[j]:
					break
				j+=1
			if j==len(self.pattern):
				matches.append(i)
		return matches

	def kmp_pattern_search(self):
		self.make_lsp()
		pass

	def rabin_karp_pattern_search(self):
		pass


ss = StringSearch("abcdeabcabdabc", " ")
