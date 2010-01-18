import sys
import os
import re

class EColiELM:
	elmList = {}
	geneTotal = 4060
	def __init__(self):
		h = open('data/EColiTotals', 'r')
		lines = h.readlines()
		for line in lines:
			line = line.rstrip()
			tokens = line.split('\t')
			ELMname = tokens[0]
			ELMnumber = tokens[1]
			self.elmList[ELMname] = ELMnumber

	
