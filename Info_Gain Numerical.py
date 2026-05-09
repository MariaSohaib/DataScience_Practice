import math as m
def Info_GAIN(entropy_before,entropy_after):
    INFO_GAIN_RESULT=entropy_before-entropy_after
    return INFO_GAIN_RESULT
def probabilities(p,q):
    total=p+q
    p1=p/total
    q1=q/total
    if p1>0:
        t1=p1*m.log2(p1)
    else:
        t1=0
    if q1>0:
        t2=q1*m.log2(q1)
    else:
        t2=0
    sol=-t1-t2
    return sol
import pandas as pd
df=pd.read_csv('CSV Files\StudentsResult.csv')
length=len(df)
counts=df['Assignment'].value_counts()
prob_of_yes=float(counts[1]/length)
prob_of_no=float(counts[0]/length)
count_pass_yes=count_pass_no=count_fail_yes=count_fail_no=0
for i,row in df.iterrows():
    if row['Assignment']==0:
        if row['Result']=='Pass':
            count_pass_no+=1
        else:
            count_fail_no+=1
    elif row['Assignment']==1:
        if row['Result']=='Pass':
            count_fail_yes+=1
        else:
            count_pass_yes+=1
group_yes=probabilities(count_fail_yes,count_pass_yes)
group_no=probabilities(count_fail_no,count_pass_no)
E_before=probabilities(prob_of_yes,prob_of_no)
E_after=(prob_of_yes*group_yes)+(prob_of_no*group_no)
Answer=E_before-E_after
print(Answer)
