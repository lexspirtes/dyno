import pandas as pd
import re

class Etl:
    def __init__(self):
        self.data = self.getData()

    def getData(self):
        """
        opens txt file and loads FASTA data in df
        returns
            df: columns =[header,sequence]
        """
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
        df = splitList(f)
        f.close()
        return df
