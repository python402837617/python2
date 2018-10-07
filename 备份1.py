#集合之间的运算
l=set([1,2,3,4,5,6,7,8,9])
l1=set([8,5,2,3,6,4,11])
l2=l&l1
l3="abcde"
#print(l3.find("r"))
def f():
    a=int(input("please input a number:"))
    try:
        sqrt_a=a**0.5
    except:
        print("input a number")
    return sqrt_a
#print(4.0/2)    
def f1():
    a=5
    b=6
    a,b=b,a
    print(a,b)
#f1() 
#dir函数了解
import 类
print(dir(类 ))
#ascii 二进制 八进制 十六进制与十进制之间的转换
def f2(a,b):
    asci=ord(a)
    er=bin(b)
    ba=oct(b)
    shil=hex(b)
    print(asci,er,ba,shil)
#f2("c",16)
#递归函数的例子
def f3(n):
    if n<=1:
        return n
    else:
        return n+f3(n-1)
#print(f3(5))
#print("i aim %E" % 8.98354)
list2=[1,2,3,4,5]
list1=["a"]
list()
#print(list2)
list3=["a","b","c","d","e"]
#list3=list2
#print(list3[0])#元组赋值
a,b,c,d,e=list2
#print(a)
def f4(a,b,c,d,e):
    return a,b,c#元组作为函数返回值
a,b=(1,2)
#print(a)
for i in range(11):
    print("%d %12.2f"%(i,10**(-i)))
jyf="shuaige"
#print(dir(jyf))
#print(help(jyf.replace))
print(dir(dict))
a="abcdef"
print(help(dict.clear))

import pickle
f=open("文件编程.py","ab ")
pickle.dump(list2,f)
 