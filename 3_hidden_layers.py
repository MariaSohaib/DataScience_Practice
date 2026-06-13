import numpy as np
def three_hidden_layers():
    input_layer=[0.5,0.3,0.7,-0.1]
    input_weights=[[0.2,0.6,0.4,0.7],
                   [0.5,0.9,0.4,0.1]]
    b1=np.array([1,2])
    first_hidden_layer_input=np.dot(input_layer,np.array(input_weights).T)+b1
    first_hidden_layer_weight=[0.6,-0.3]
    b2=3
    sec_hidden_layer_input=np.dot(first_hidden_layer_input,np.array(first_hidden_layer_weight).T)+b2
    sec_hidden_layer_weights=[[0.1],[0.2],[0.3]]
    b3=np.array([1,2,3])
    third_hidden_layer_input=np.dot(sec_hidden_layer_input,np.array(sec_hidden_layer_weights).T)+b3
    third_hidden_layer_weight=[0.5,0.3,0.1]
    b4=0.7
    output=np.dot(third_hidden_layer_input,np.array(third_hidden_layer_weight).T)+b4
    sigmoid=1/(1+np.exp(-output))
    print(sigmoid)

three_hidden_layers()
"""
O
    O       O
O
        O   O   O
O           
    O       O
O           
"""