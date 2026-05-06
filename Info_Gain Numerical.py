def Info_GAIN(entropy_before,entropy_after):
    INFO_GAIN_RESULT=entropy_before-entropy_after
    return INFO_GAIN_RESULT
def probablities(p,q):
    sol=(-p*m.log2(p))-(q*m.log2(q))
    return sol
import pandas as pd
import math as m
df=pd.read_csv('CSV Files\StudentsResult.csv')
length=len(df)
counts=df['Assignment'].value_counts()
prob_of_yes=float(counts[0]/length)
prob_of_no=float(counts[1]/length)