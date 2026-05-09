import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
df=pd.read_csv('CSV Files\StudentsResult.csv')
dt_model=DecisionTreeClassifier()
dt_model.fit(df[['Study_Hours','Attendance','Assignment']],df.Result)
print(dt_model.predict([[5,80,1]]))
plt.figure(figsize=(10,6))
plot_tree(dt_model,feature_names=df[['Study_Hours','Attendance','Assignment']].columns,filled=True)
plt.show()