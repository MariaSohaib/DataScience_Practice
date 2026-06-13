import numpy as np
import math
import random
def two_hidden_layers():
    input_layer=[random.random() for _ in range(3)]
    input_weights=[[random.random() for _ in range(3)],
                    [random.random() for _ in range(3)]]
    b1=random.random()
    first_hidden_layer_input=np.dot(input_layer,np.array(input_weights).T)+b1
    first_hidden_layer_weights=[[random.random() for _ in range(2)],
                                 [random.random() for _ in range(2)],
                                 [random.random() for _ in range(2)]]
    b2=random.random()
    sec_hidden_layer_input=np.dot(first_hidden_layer_input,np.array(first_hidden_layer_weights).T)+b2
    sec_hidden_layer_weights=[random.random() for _ in range(3)]
    b3=random.random()
    output=np.dot(sec_hidden_layer_input,np.array(sec_hidden_layer_weights).T)+b3
    sigmoid=1/(1+math.exp(-output))
    print(sigmoid)

two_hidden_layers()

"""
O       O
    O
O       O   O
    O
O       O
"""