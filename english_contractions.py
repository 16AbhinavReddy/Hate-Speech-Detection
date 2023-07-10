import pandas as pd

eng_cont = {}

data = pd.read_csv('contractions.csv')

list1 = data['Contraction'].tolist()
list2 = data['Meaning'].tolist()

for i in range(len(data)):
    eng_cont[list1[i]] = list2[i]

print(eng_cont)

