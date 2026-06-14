from collections import defaultdict
import pandas as pd
df=pd.read_csv('CSV Files/data.csv')
BoW_spam=defaultdict(int)
Bow_ham=defaultdict(int)
spam_rows=df[df['tag']=='spam']
ham_rows=df[df['tag']=='ham'][:747]
for row in spam_rows['text']:
    for words in row.split(" "):
        BoW_spam[words.lower()]+=1
for row in ham_rows['text']:
    for words in row.split(" "):
        Bow_ham[words.lower()]+=1

print(len(BoW_spam))
print(len(Bow_ham))