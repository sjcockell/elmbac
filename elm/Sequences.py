from Bio import SeqIO
class Sequences:
	sequenceList = {}
	def __init__(self, list):
		h = open('data/'+list, 'r')
		for seq_record in SeqIO.parse(h, "fasta"):
			self.sequenceList[seq_record.id] = str(seq_record.seq)

		
