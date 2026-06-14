import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


df=pd.read_csv('CSV Files\students.csv')    #reading csv file

df['Gender_num']=df['Gender'].map({'Male':0,'Female':1})    #mapping string values to numerical values

model=KMeans(n_clusters=3)    #creating model object and assigning no. of clusters

cluster_predict=model.fit_predict(df[['Age','Marks','Gender_num']])  #training model on these columns

df['Cluster']=cluster_predict    #making new column named Cluster with predicted values

cluster_0=df[df['Cluster']==0]    #mapping cluster values to clusters 
cluster_1=df[df['Cluster']==1]    #mapping cluster values to clusters 
cluster_2=df[df['Cluster']==2]    #mapping cluster values to clusters 

plt.scatter(cluster_0['Age'],cluster_0['Marks'],label='Cluster 0')    #plotting scatter graph
plt.scatter(cluster_1['Age'],cluster_1['Marks'],label='Cluster 1')    #plotting scatter graph
plt.scatter(cluster_2['Age'],cluster_2['Marks'],label='Cluster 2')    #plotting scatter graph

plt.xlabel('Age')    #Labeling x-axis
plt.ylabel('Marks')  #Labeling y-axis
plt.legend()         #show which dot belongs to which clusters in a separate box
plt.show()           #Shows the plotted graph

new_student=pd.DataFrame([[24,95,0]],columns=['Age','Marks','Gender_num'])    #add new student's data with column names
print(model.predict(new_student))    #Shows to which cluster new student belongs.
