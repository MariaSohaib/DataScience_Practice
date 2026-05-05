import pandas as pd
df=pd.read_csv('CSV Files/Customers.csv')
print(df.head(10))   #Showing first 10 rows of dataset
print(df.info())        #Showing datatypes and other info
print(df.describe())    #Gives no. of counts,mean,std,min,max etc(statistical analysis)
print(df['Company'].value_counts)   #tells how many times a unique value appears in dataset
print(df.shape)                     #Tells no.of rows and column
print(df.iloc[4])                   #Gives info about specific index
print(df.isnull().sum())            # tells us how much data is missing in each row