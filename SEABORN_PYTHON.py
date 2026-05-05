import matplotlib.pyplot as plt
import seaborn as sns
x=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
y=[1,2,3,4,5,6,7]
sns.set(style='darkgrid')
#sns.stripplot(x=x,y=y)
#sns.swarmplot(x=x,y=y)
sns.barplot(x=x,y=y)
#sns.boxplot(x=x,y=y)
plt.show()
