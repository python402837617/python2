print(1.23e9)
print(11/2)
l=[1,2,3]
print(l[::-1])
l.insert(1,5)
l.remove(1)
l.pop(1)
del l[0]
l[0]=9
print(l)
tuple1=[1,2,3]
tuple2=["a","b","c"]
tuple2=tuple1#元组赋值,列表也可以
print(tuple2[0])
def f(x,y):
    return (x,y)
test1="4580"
t=test1.split("5")
print(t)
dict1=dict()
dict1["a"]=1
dict1["b"]=2
dict1["c"]=3
dict2={b:a for a,b in dict1.items()}
print(dict)
print(dict1.get("d",9))
set1=set([1,2,3])
set1.add(1)
print(set1)
import math
print(math.sqrt(5))
print(l)
for a,b in enumerate(l):#对list的效果类似item对dict的效果
    print(a,b)
l1=[3,4,5]
for i in zip(l,l1):
    print(i)
print(",".join("sdfg"))#join函数针对字符类型
tuple3={m:n for m in range(10)  for n in range(10)}#生成列表里的语句是嵌套关系
print(tuple3)
from functools import reduce
test2=reduce(lambda x,y:x+y if x<y else x-y,l1)
print(test2)
test3=filter(lambda x: 1 if x<4 else 0,l1)
print(list(test3))
dict1["d"]=0
print(dict1)
sort_dict1=sorted(l1,key=lambda x:-x)
print(sort_dict1)
def fw(*arg):
    a=25
    def fn():
        nonlocal a
        a=a+1
        return a
    return fn
print(fw()())
bb=fw()
print(bb.__closure__)
print(bb.__closure__[0].cell_contents)
import time
def zsq(f):
    def wrapper(*arg,**kw):
        satrt_time=time.time()
        f(*arg,**kw)
        end_time=time.time()
        print("函数%s花费%ss时间"%(f,end_time-satrt_time))
    return wrapper
@zsq
def f1():
    sum=0
    for i in range(100000):
        sum=sum+i
    return sum
f1()
class N_type(object):
    def __len__(self):
        return 0
test4=N_type()
if not test4:
    print(1)
try:
    r=int(input("please input a int:"))
except:
    print("error")
else:
    print("right")
finally:
    print(1)
from 类 import Human
class test(Human):
    mod="fx"
    def __init__(self,name,age,sex):
        Human.__init__(self,name,age)
        self.sex=sex
    def __time(self):
        a=time.time()
        return time.ctime(a)
    @classmethod
    def __time1(cls):
        return time.clock()
    def go(self):
        select=bool(input("please input your select"))
        if not select:
            print(self.__time())
        else:
            print(self.__time1())
jyf=test("jyf",22,"nan")
jyf.go()
print(jyf._test__time())
str1="i am a boy"
print(str1.upper(),str1.capitalize())
from enum import unique,IntEnum,Enum
class vip(IntEnum):
    yellow=1
    ye=1
    blue=2
    red=3
print(vip.ye,"\n",vip.blue.name,"\n",vip.red.value)
for v in vip.__members__:
    print(v)
print(vip.ye.value)
str2="xjy is a boy"
str2=str2.replace("boy","girl")
print(str2)
float1=5.6
print(int(float1),round(float1),math.ceil(float1))
print(str1.isdigit())#字符串里是否为数字
print(str1.isalpha())#判断是否为字母
print(str1.isspace())#判断是否为空格
ascii_num=ord("s")#ord将一个字符通过ascii转换为对应的数字
print(chr(5))#chr将数字转换为ascii字符
print(str1.find("i",2,6))#find方法，判断是否包含某个字符，有返回索引，无返回-1
print(l1.extend(l1))
file=open("kg to bang.py","r+")
file.readline(size=8)
file.readlines()
file.read(size=9)
file.write("")


