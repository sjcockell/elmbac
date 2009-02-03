from elm import ELM, Sequences, Match
import sys

def main(f):
	e = ELM.ELM()
	s = Sequences.Sequences(f)
	seqs = s.sequenceList
	elms = e.elmList
#	test(seqs, elms)
	results = getResultSet(seqs, elms)
	printResultSet(results)

def test(s, e):
	k1 = s.keys()
	k2 = e.keys()
	seq = k1[0]
	seqSeq = s[seq]
	print seq, seqSeq
	for elm in k2:
		elmPat = e[elm]
		m = Match.Match(seqSeq, elmPat)
		if m.getMatches():
			print elm, elmPat
			print m.getMatches()
			print m.getNumberMatches()

def getResultSet(sequences, elmMotifs):
	resultArray = []
	sequenceNames = sequences.keys()
	elmNames = elmMotifs.keys()
	listTitles = elmNames[:]
	listTitles.insert(0, '')
	tupleTitles = tuple(listTitles)
	resultArray.append(tupleTitles)
	i = 1
	for sequenceName in sequenceNames:
		tempList = []
		sequence = sequences[sequenceName]
		tempList.append(sequenceName)
		for elmName in elmNames:
			elmMotif = elmMotifs[elmName]
			matcher = Match.Match(sequence, elmMotif)
			tempList.append(matcher.getNumberMatches())
		tempTuple = tuple(tempList)
		resultArray.append(tempTuple)
		i += 1
	return resultArray

def printResultSet(r):
	fh = open('outfile', 'w')
	for line in r:
		for element in line:
			print str(element)+"\t",
		print
	close(fh)

if __name__ == '__main__':
	try:
		organism = sys.argv[1]
	except IndexError:
		print 'Usage: python elmSearch.py organismName'
		print 'Where viable names are:'
		print 'ecoli'
	else:
		print organism
		file = organism + '.fa'
		main(file)

