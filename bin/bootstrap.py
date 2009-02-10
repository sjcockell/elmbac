from elm import ELM, Sequences, Match
import sys
from random import randrange
from rpy import *

def main(f):
	e = ELM.ELM()
	s = Sequences.Sequences(f)
	seqs = s.sequenceList
	s.setIndexedSequenceLists()
	list = s.getIndexedSequenceList()
	elms = e.elmList
	score = scoreSequences(list, elms['LIG_TRAF2_1'])
	randScore = scoreSequences(getRandomSequences(list, 25), elms['LIG_TRAF2_1'])
	picks = [score, randScore]
	totals = [len(list), 25]
	print r.prop_test(picks, totals)
#	test(seqs, elms)
#	totalScores = []
#	avScores = []
#	for i in range(0, 1000):
#		randomList = getRandomSequences(list, 25)
#		score = scoreSequences(randomList, elms['LIG_TRAF2_1'])
#		totalScores.append(score)
	#print r.wilcox_test(totalScores)
#	r.library('moments')
#	r.kurtosis(totalScores)
#	r.skewness(totalScores)
#	ttestResults = r.t_test(totalScores, conf_level=0.99)
#	mannWhitneyResults = r.wilcox_test(totalScores, conf_int='TRUE' ,conf_level=0.99)
#	summary = r.summary(totalScores)
#	ttestResults = r.t_test(avScores, conf_level=0.99)
#	mannWhitneyResults = r.wilcox_test(avScores, conf_int='TRUE' ,conf_level=0.99)
#	print "Mean:\t"+str(summary['Mean'])
#	print "T Conf:\t"+str(ttestResults['conf.int'])
#	print "MW Conf:\t"+str(mannWhitneyResults['conf.int'])
#	testList = getRandomSequences(list, 25)
#	testScore = scoreSequences(randomList, elms['LIG_TRAF2_1'])
#	testAvScore = float(testScore)/10.0
#	print testScore
	#	print str(k)+':'+str(summary[k])
	#for k in ttestResults.keys():
	#	print str(k)+':'+str(ttestResults[k])
	#for k in mannWhitneyResults.keys():
	#	print str(k)+':'+str(mannWhitneyResults[k])


def getRandomSequences(seqList, number):
	start = 0
	end = len(seqList)
	randList = []
	for i in range(0, number):
		rand = randrange(start, end)
		randList.append(seqList[rand])
	return randList

def scoreSequences(list, elm):
	score = 0
	scoreArray = []
	for seq in list:
		m = Match.Match(seq, elm)
		scoreArray.append(m.getNumberMatches())
		score = score + m.getNumberMatches()
	return score

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

