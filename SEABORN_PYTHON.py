import matplotlib.pyplot as plt
import seaborn as sns
x=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
y=[1,2,3,4,5,6,7]
sns.set(style='darkgrid')    #setting the background style of grid
#sns.stripplot(x=x,y=y)      #plotting stripplot
#sns.swarmplot(x=x,y=y)      #plotting swarmplot
sns.barplot(x=x,y=y)         #plotting barplot
#sns.boxplot(x=x,y=y)        #plotting boxplot
plt.show()
