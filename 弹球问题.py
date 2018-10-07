def f():
    '''弹球。'''
    sum=0
    h=int(input(""))
    n=int(input(""))
    while n>0:
        sum=h+0.6*h+sum
        h=0.6*h
        n=n-1
    return sum
print(f())