from elm import ELM, Sequences, Match, Scores
import sys

e = ELM.ELM()
elms = e.elmList
scores = Scores.Scores('ecoli')
score_dict = scores.scores

def main(f, ss, file):
    if ss != 'ecoli':
        scores = Scores.Scores(ss)
    s = Sequences.Sequences(f)
    s.setIndexedSequenceLists()
    #seqs = s.getIndexedSequenceList()
    #seqs = s.indexedSequenceList
    seqs = s.sequenceTuples
    seq_scores = map(score_sequence, seqs)
    out = open(file, 'w')
    for score in seq_scores:
        out.write(score[0]+'\t'+str(score[1])+'\t'+str(score[2])+'\t'+str(score[3])+'\n')
    out.close()

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
    return (sequence[0], total, total/len(sequence[1]), (total/len(sequence[1]))*total)

if __name__ == '__main__':
    try:
        organism = sys.argv[1]
        score_system = sys.argv[2]
        out_file = sys.argv[3]
    except IndexError:
        print 'Usage: python scoreAll.py organismName scoreSystem outFile'
        print 'Where viable names are:'
        print 'ecoli'
    else:
        print organism
        file = organism + '.fa'
        main(file, score_system)

