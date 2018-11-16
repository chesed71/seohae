import pandas as pd

class FileHandler:
    def readFile(self, filename):
        df = pd.read_csv(filename, delimiter="\t")
        return df['En'], df['Ko']