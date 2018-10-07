import time
#原函数
#def yuan(x,y):
 #   return x+y
#实现在调用函数的时候，同时输出调用函数的时间。
#方法一
#def fs1(f,x,y):
 #   print(time.time())    
  #  print(f(x,y))

#fs1(yuan,1,2) 
#方法二
#def fs2(f):
    #def zs(x,y):
     #   print(time.time())
      #  return f(x,y)
    #return zs
#@fs2
#def yuan(x,y):
 #   print(x(2.5))
#yuan(int,2)
def print_time(f):
    def wrapper(*arg,**kw):
        print(time.time())
        f(*arg,**kw)
        print(time.time())
    return wrapper
@print_time
def bl(n):
    l=[]
    for i in range(n):
       l.append(i)
    return l
bl(9000)        
