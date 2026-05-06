def Weight(x1,x2,x3):
    w1=0.9
    w2=0.5
    w3=0.6
    bias=0.75
    calc=(x1*w1)+(x2*w2)+(x3*w3)+bias
    return calc
def main():
    solution=Weight(0.5,0.2,0.3)
    print(f"Solution: {solution}")
if __name__=="__main__":
    main()