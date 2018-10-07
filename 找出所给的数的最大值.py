def max_1():
    l=[]
    n=int(input("please input a int number:"))
    for i in range(n):
        i=i+1
        number1=float(input("please input a floate number:"))
        l.append(number1)
    max_n=max(l)
    return max_n
if __name__=="__main__":
    print(max_1())