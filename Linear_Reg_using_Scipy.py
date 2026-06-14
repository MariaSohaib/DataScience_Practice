from scipy import stats
import matplotlib.pyplot as plt
import random
x=[random.randint(5,50) for _ in range(15)]
y=[random.randint(10,80) for _ in range(15)]
plt.scatter(x,y,color='red')
m,Y,r,p,err=stats.linregress(x,y)
lin_model=[m*var+Y for var in x]
plt.plot(x,lin_model,color='black')
plt.show()
print(r)