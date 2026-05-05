import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df=pd.read_csv('CSV Files\students.csv')
df['Gender_num']=df['Gender'].map({'Male':0,'Female':1})
model=KMeans(n_clusters=3)
cluster_predict=model.fit_predict(df[['Age','Marks','Gender_num']])
df['Cluster']=cluster_predict
cluster_0=df[df['Cluster']==0]
cluster_1=df[df['Cluster']==1]
cluster_2=df[df['Cluster']==2]
plt.scatter(cluster_0['Age'],cluster_0['Marks'],label='Cluster 0')
plt.scatter(cluster_1['Age'],cluster_1['Marks'],label='Cluster 1')
plt.scatter(cluster_2['Age'],cluster_2['Marks'],label='Cluster 2')
plt.xlabel('Age')
plt.ylabel('Marks')
plt.legend()
plt.show()
new_student=pd.DataFrame([[24,95,0]],columns=['Age','Marks','Gender_num'])
print(model.predict(new_student))