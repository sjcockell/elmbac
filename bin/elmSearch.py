from elm import ELM, Sequences, Match
import sys

def main(f):
	e = ELM.ELM()
	s = Sequences.Sequences(f)
	seqs = s.sequenceList
	elms = e.elmList
	test(seqs, elms)

def test(s, e):
	k1 = s.keys()
	k2 = e.keys()
	elm = k2[0]
	seq = k1[0]
	elmPat = e[elm]
	seqSeq = s[seq]
	print elmPat, seqSeq
	m = Match.Match(seqSeq, elmPat)
	print m.getMatches()

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

