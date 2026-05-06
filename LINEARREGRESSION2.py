import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
x=np.array([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30])
y=x+2+np.random.randint(2,40,size=len(x))
plt.scatter(x,y)
plt.xlabel('Independent value')
plt.ylabel('Dependent value')
l_model=linear_model.LinearRegression()
x=x.reshape(-1,1)
l_model.fit(x,y)
print(l_model.predict([[40]]))
print(f'Slope(m): {l_model.coef_[0]}')
print(f'Intercept(c): {l_model.intercept_}')
plt.plot(x,l_model.predict(x),color='red')
plt.show()
