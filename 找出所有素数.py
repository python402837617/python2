def ss():
    n=int(input("please give one number:"))
    b=0
    for i in range(1,n):
        a=i//2
        for c in range(2,a):
            if i%c==0:
                b=1
                break
            else:
                b=0
        if b==0:
            print(i)         
if __name__=="__main__":
    ss()     