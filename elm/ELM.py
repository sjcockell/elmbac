import sys
import os
import re

class ELM:
	elmList = {}
	def __init__(self):
		h = open('data/ELMs', 'r')
		lines = h.readlines()
		for line in lines:
			line = line.rstrip()
			tokens = line.split('\t')
			ELMname = tokens[0]
			ELMpattern = tokens[1]
			self.elmList[ELMname] = ELMpattern

