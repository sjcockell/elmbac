class Scores:
    scores = {}
    def __init__(self, species):
        fh = open('data/'+species+'.scores', 'r')
        for line in fh.readlines():
            line = line.rstrip()
            split = line.split('\t')
            self.scores[split[0]] = float(split[1])

