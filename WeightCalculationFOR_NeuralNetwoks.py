import math
def Weight(x1,x2,x3):
    w1=0.9
    w2=0.5
    w3=0.6
    bias=0.75
    calc=(x1*w1)+(x2*w2)+(x3*w3)+bias
    return calc
def Activation_Function(x):
    Sol=1/(1+math.exp(-x))
    return Sol
def main():
    solution=Weight(0.5,0.2,0.3)
    print(f"Solution: {solution}")
    Solution1=Activation_Function(solution)
    print(f"Value of Activation Function: {Solution1}")
if __name__=="__main__":
    main()