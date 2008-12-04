import re

class Match:
	def __init__(self, sequence, elm):
		p = re.compile('(?=('+elm+'))')
		self.m = p.findall(sequence)

	def getMatches(self):
		return self.m

	def getNumberMatches(self):
		return len(self.m)
