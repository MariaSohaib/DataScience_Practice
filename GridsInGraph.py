import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20,3])
y=np.array([15,56,4])
                #1st Plot
plt.subplot(1,2,1)
plt.plot(x,y,linestyle='dashed',marker='o')
plt.title('x,y-graph',loc='left')
plt.xlabel('x-axis')   
plt.ylabel('y-axis') 
plt.grid(axis='x') 
                #2nd Plot
plt.subplot(1,2,2)
plt.plot(y,x,linestyle='dashed',marker='o')
plt.title('y,x-graph',loc='left')
plt.xlabel('x-axis')   
plt.ylabel('y-axis') 
plt.grid(axis='y') #all properties are same for grid lines as plot line
plt.show()