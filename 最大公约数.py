def f():
    '''求给定数字的最大公约数
    '''
    try:
        a=int(input("please input a number:"))
        b=int(input("please input a number:"))
    except:
        print("please input a number")
    if a<b:
        small=a
    else:
        small=b
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            gys=i
    return gys
print(f.__doc__)
print(f())        