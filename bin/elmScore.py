from elm import EColiELM, ELM, Sequences, Match
import elmSearch
import sys
from optparse import OptionParser
from rpy import *

def main(inf, outf):
	e = ELM.ELM()
	s = Sequences.Sequences(inf)
	ece = EColiELM.EColiELM()
	seqs = s.sequenceList
	elms = e.elmList
	results = elmSearch.getResultSet(seqs, elms)
	#stats = getStats(results, ece)
	stats = None
	elmSearch.printResultSet(results, outf, stats)

def getStats(res, eColi):
	statTotals = {}
	geneTotal = 0
	for number in range(1, len(res)):
		geneTotal += 1
		for index in range(1, len(res[number])):
			try:
				statTotals[res[0][index]] = statTotals[res[0][index]] + res[number][index]
			except KeyError:
				statTotals[res[0][index]] = 0 + res[number][index]
	statKeys = statTotals.keys()
	statKeys = sorted(statKeys)
	print geneTotal, eColi.geneTotal
	for key in statKeys:
		numberTest = statTotals[key]
		numberBack = eColi.elmList[key]
		picks = [int(numberBack), numberTest]
		totals = [eColi.geneTotal, geneTotal]
		print picks
		print totals
		print r.prop_test(picks, totals)

if __name__ == '__main__':
	parser = OptionParser(usage="Usage: %prog [options] infile.fa outfile.xls",
		version="%prog 0.2")
	(options, args) = parser.parse_args()
	if len(args) != 2:
		print 'Usage error, you need to define an infile and an outfile'
		parser.print_help()
	else:
		infile = args[0]
		outfile = args[1]
		main(infile, outfile)
	#try:
	#	comparator = sys.argv[1]
	#except IndexError:
	#	print 'Usage: python elmSearch.py sequences'
	#	print 'Where viable names are:'
	#	print 'epec'
	#else:
	#	print comparator
	#	if comparator == 'ecoli':
	#		print 'You are comparing ecoli to ecoli, this seems a little fruitless, don\'t you think?'
	#	else:
	#		file = comparator + '.fa'
	#		main(file)

