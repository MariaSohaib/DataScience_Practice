import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df=pd.read_csv('CSV Files\StudentsResult.csv')
features=['Study_Hours','Attendance','Assignment']
k_model=KMeans(n_clusters=3)
k_cluster=k_model.fit_predict(df[features])
df['Cluster']=k_cluster
cluster_0=df[df['Cluster']==0]
cluster_1=df[df['Cluster']==1]
cluster_2=df[df['Cluster']==2]
plt.scatter(cluster_0['Study_Hours'], cluster_0['Attendance'])
plt.scatter(cluster_1['Study_Hours'], cluster_1['Attendance'])
plt.scatter(cluster_2['Study_Hours'], cluster_2['Attendance'])
plt.show()
print(k_model.predict([[3,67,1]]))