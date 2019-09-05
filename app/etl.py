import pandas as pd
import re

class Etl:
    def __init__(self):
        self.location = "Users/Lex/desktop/Parvoviridae_full_130_refseq_sequence.txt"
        self.data = self.getData()

    def getData(self):
        f = open(u"/Users/Lex/desktop/Parvoviridae_full_130_refseq_sequence.txt", "r").read()
        def splitList(f):
            f = re.sub("\n", "", f)
            fList = filter(None,f.split('>'))
            for index,r in enumerate(fList):
                r = r.rsplit(']', 1)
                r[0] += ']'
                fList[index] = r
            df = pd.DataFrame(fList, columns=['header', 'sequence'])
            return df
        return splitList(f)
