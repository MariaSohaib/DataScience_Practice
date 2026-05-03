import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors1=np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x,y,c=colors1,cmap='viridis')

x=np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y=np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
colors2=np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100,44,56])
plt.scatter(x, y,c=colors2,cmap='viridis',alpha=0.5)
plt.colorbar()
plt.bar(x,y)        #Vertical Bar
plt.show()
plt.barh(x,y,color='red')       #horizontal bar
plt.show()