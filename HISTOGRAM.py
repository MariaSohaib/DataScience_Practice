#graph showing the number of observations within each given interval
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(1,30,size=15)
plt.hist(x)   #shows histogram
plt.show()
plt.pie(x)    #shows pie graph
plt.show()
