#lambda表达式
a=lambda x,y:x+y
#print(a(1,2))
#三元表达式
x=1
y=2
b=x if x>y else y
#print(b)
# map 类
l1=[1,2,3,4,5,6]
l2=map(lambda x,y,z:y+z if x>y else x+z,l1,l1,l1)
print(list(l2))
#reduce   
from functools import reduce
l3=[(1,2),(1,2)]
wz=reduce(lambda x,y:(x[0]+y[0],x[1]+y[1]),l3)
print(wz)
#filter 过滤掉某些元素  只能传入一个list 但可以通过设置list的形式达到传入多个list的效果
l4=[1,0,1,0,2,0]
l5=filter(lambda x:True if x!=0 else False,l4)
print(list(l5))
l6=["a","A"]
l7=filter(lambda x:True if x in "[a-z]" else False, l6)
print(list(l7))
