from Bio import SeqIO
class Sequences:
    sequenceList = {}
    indexedSequenceIDList = []
    indexedSequenceList = []
    sequenceTuples = []
	
    def __init__(self, list):
        h = open('data/'+list, 'r')
        for seq_record in SeqIO.parse(h, "fasta"):
            self.sequenceList[seq_record.id] = str(seq_record.seq)

    def setIndexedSequenceLists(self):
        i = 0
        keys = self.sequenceList.keys() 
        for key in keys:
            self.indexedSequenceIDList.append(key)
            self.indexedSequenceList.append(self.sequenceList[key])
            self.sequenceTuples.append((key, self.sequenceList[key]))
            i += 1
	
    def getIndexedSequenceList(self):
        return self.indexedSequenceList
