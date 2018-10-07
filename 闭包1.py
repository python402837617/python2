#闭包=内层函数+环境变量  ：由于内层函数调用了环境变量，将内层函数与环境变量封闭起来，环境变量不随外部的改变而改变。
#作用：保存内部信息，保存函数的状态信息，使函数的局部变量信息依然可以保存下来，保存局部信息不被销毁。
def wc():
    a=25
    def nc():
        nonlocal a
        a=a+1
        return a
    return nc
f=wc()
print(f)
print(f())
print(f.__closure__)
print(f.__closure__[0].cell_contents)    
def wc1():
    a=10
    def nc():
        nonlocal a
        a=a+1
        return a    
    return nc()    

print(wc1()) 
     


   
    