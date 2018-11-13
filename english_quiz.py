import pandas as pd

filename = './data/word_list.xlsx'
df = pd.read_excel(filename, sheet_name='Sheet1')
en_word_list = df['En']
ko_word_list = df['Ko']


