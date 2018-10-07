def f():
    '''求近似圆周率'''
    sum1=1
    n=int(input("输入近似精确度:"))
    while n>1:
        sum1=sum1-1/(2*n-1)*(-1)**(n)
        n=n-1
    return sum1*4
print(f())