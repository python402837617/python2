def f(u):
    '''杨辉三角形。


    ：打印出杨辉三角形（要求打印出10行如下图）
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1
    1 6 15 20 15 6 1
    1 7 21 35 35 21 7 1
    1 8 28 56 70 56 28 8 1
    1 9 36 84 126 126 84 36 9 1'''
    l=[[1],[1,1]]
    for i in range(2,u):
        l.append([1,1])
        for n in range(0,i-1):
            a=l[i-1][n]+l[i-1][n+1]
            l[i].insert(n+1,a)
    for m in l:
        for k in m:
            print(k,end=' ')
        print()
print(f.__doc__)
f(15)
