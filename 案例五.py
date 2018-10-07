def f():
    '''案例5.


    输入三个整数x,y,z，请把这三个数由小到大输出。'''
    x=int(input('请输入：'))
    y=int(input('请输入：'))
    z=int(input('请输入：'))
    L=[]
    L.append(x)
    L.append(y)
    L.append(z)

    print(sorted(L))
print(f.__doc__)
f()
