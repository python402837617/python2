def fblq():
    first,second=0,1
    n=int(input("please input a number:"))
    while n>0:
        print(first,end=" ")
        first,second=second,first+second
        n-=1
    else:
        print("\nit's all")
def dg(n,first,second):
    if n>0:
        print(first)
        return dg(n-1,second,first+second)
if __name__=="__main__":
    fblq()
    dg(8,0,1)