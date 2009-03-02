from elm import Sequences

def main(f):
	s = Sequences.Sequences(f)
	seqs = s.sequenceList

	getSequenceStats(seqs)

def getSequenceStats(sequences):
	total = 0
	freqs = {'A':0,'C':0,'D':0,
	'E':0,'F':0,'G':0,'H':0,
	'I':0,'K':0,'L':0,'M':0,
	'N':0,'P':0,'Q':0,'R':0,
	'S':0,'T':0,'V':0,'W':0,
	'Y':0,'U':0}
	for sequence in sequences:
		s = sequences[sequence]
		for char in s:
			total += 1
			try:
				freqs[char] += 1
			except KeyError:
				print char
				exit()
	for f in freqs:
		freq = freqs[f]
		percent = float(freq)/float(total)
		print f+"\t"+str(freq)+"\t"+str(percent)

if __name__ == '__main__':
	main('ecoli.fa')
