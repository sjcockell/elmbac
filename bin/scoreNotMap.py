from elm import ELM, Sequences, Match, Scores
import sys

e = ELM.ELM()
elms = e.elmList
scores = Scores.Scores('ecoli')
score_dict = scores.scores

def main(f):
    s = Sequences.Sequences(f)
    s.setIndexedSequenceLists()
    #seqs = s.getIndexedSequenceList()
    #seqs = s.indexedSequenceList
    seqs = s.sequenceTuples
    seq_scores = []
    for seq in seqs:
        seq_scores.append(score_sequence(seq))
    #print seqs
    #for score in seq_scores:
    #    print score[0]+'\t'+str(score[1])+'\t'+str(score[2])

def score_sequence(sequence):
    tempList = []
    elmNames = elms.keys()
    for elmName in elmNames:
        elmMotif = elms[elmName]
        matcher = Match.Match(sequence[1], elmMotif)
        try:
            tempList.append(matcher.getNumberMatches()*score_dict[elmName])
        except KeyError:
            pass
    total = reduce(lambda x,y: x+y, tempList)
    print sequence[0]+'\t'+str(total)+'\t'+str(total/len(sequence[1]))
    return (sequence[0], total, total/len(sequence[1]))

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

