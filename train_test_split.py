import numpy as np
from sklearn.model_selection import train_test_split
X=np.arange(10).reshape(5,2)
y=range(5)
x_train,x_test,y_train,y_test=train_test_split(
    X,y,
    test_size=0.33,
    random_state=42
)
print(f"X training data= {x_train}\n")
print(f"Y training data= {y_train}\n")
print(f"X testing data= {x_test}\n")
print(f"Y testing data= {y_test}\n")