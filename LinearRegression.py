import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
x=[1,2,3,4,5,6,7]
y=[1,4,9,16,25,36,49]
plt.scatter(x,y)
plt.xlabel('Independent value')
plt.ylabel('Dependent value')
x=np.array(x).reshape(-1,1)
lin_model=linear_model.LinearRegression()
lin_model.fit(x,y)
print(lin_model.predict([[10]]))
print(f'Slope(m): {lin_model.coef_[0]}')
print(f'Intercept(c): {lin_model.intercept_}')
plt.plot(x,lin_model.predict(x),color='red')
plt.show()