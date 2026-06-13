import math
def Activation_Function(x):
    Sol=1/(1+math.exp(-x))
    return Sol
def Input_layer(x1,x2,x3):
    w1,w2,w3,w4,w5,w6=1,2,3,4,5,6
    calc1=(x1*w1)+(x2*w3)+(x3*w5)
    calc2=(x1*w2)+(x2*w4)+(x3*w6)
    return calc1,calc2
def first_hidden_layer(x4,x5):
    w7,w8,w9,w10,w11,w12=1,2,3,4,5,6
    calc3=(x4*w7)+(x5*w10) 
    calc4=(x4*w8)+(x5*w11)
    calc5=(x4*w9)+(x5*w12)
    return calc3,calc4,calc5
def sec_hidden_layer(x6,x7,x8):
    w13,w14,w15,w16,w17,w18=1,2,3,4,5,6
    calc6=(x6*w13)+(x7*w15)+(x8*w17)
    calc7=(x6*w14)+(x7*w16)+(x8*w18)
    return calc6,calc7
def last_layer(x9,x10):
    w19,w20=1,2
    bias=0.6
    calc=(x9*w19)+(x10*w20)+bias
    return calc
def main():
    sol1,sol2=Input_layer(0.3,0.2,0.1)
    sol1=Activation_Function(sol1)
    sol2=Activation_Function(sol2)
    sol3,sol4,sol5=first_hidden_layer(sol1,sol2)
    sol3=Activation_Function(sol3)
    sol4=Activation_Function(sol4)
    sol5=Activation_Function(sol5)
    sol6,sol7=sec_hidden_layer(sol3,sol4,sol5)
    sol6=Activation_Function(sol6)
    sol7=Activation_Function(sol7)
    output=last_layer(sol6,sol7)
    output=Activation_Function(output)
    print(f"Solution: {output}")
if __name__=="__main__":
    main()