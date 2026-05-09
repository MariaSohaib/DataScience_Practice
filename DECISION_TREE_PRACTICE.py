import pandas as pd 
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
df=pd.read_csv('CSV Files\Approving_Loan.csv')
tree_model=DecisionTreeClassifier()
tree_model.fit(df[['Income','Credit_Score','Loan_Amount']],df.Approved)
print(tree_model.predict([[5,700,20]]))
plt.figure(figsize=(10,6))
plot_tree(tree_model, feature_names=df[['Income','Credit_Score','Loan_Amount']].columns,filled=True,max_depth=3)
plt.show()