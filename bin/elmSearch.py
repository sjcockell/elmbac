from elm import ELM, Sequences, Match
import sys
import xlwt

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
#	fh = open('outfile', 'w')
#	for line in r:
#		for element in line:
#			print str(element)+"\t",
#		print
#	close(fh)
	wb = xlwt.Workbook()
	ws = wb.add_sheet("Results")
	row = 0
	for line in r:
		col = 0
		for element in line:
			ws.write(row, col, element)
			col += 1
		row += 1
	print row, col
	for cell in range(1, col):
		col = convertColumn(cell)
		formula1 = "SUM("+col+"2:"+col+str(row)+")"
		formula2 = "AVERAGE("+col+"2:"+col+str(row)+")"
		ws.write(row, cell, xlwt.Formula(formula1))
		ws.write(row+1, cell, xlwt.Formula(formula2))
	wb.save("out.xls")

def convertColumn(c):
	letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
	if c > 25:
		div = int(c/26)
		letter1 = letters[div-1]
		letter2 = letters[c-(26*div)]
		return letter1+letter2
	else:
		return letters[c]



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

