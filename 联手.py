from enum import IntEnum,unique
from 类 import Human
class Sb(Human):
    sex=18
    def __init__(self,name,age):
        super(Sb,self).__init__(name,age)
    def sb_name(self):
        print(self.name)
    @classmethod
    def sb_sex(cls):
        print(cls.sex)
@unique
class shitang(IntEnum):
    yst=1
    est=2
    sst=3
def zsq(f):
    def wrapper():
        print("jyf is a boy")
        f()
    return wrapper
#@zsq    
def wb(b):
    def nb():
        nonlocal b
        b=b+1
        print(b)
    return nb
@zsq
def hss():
    l=[0,1,2,3,4,4,2,3,0,0,0]
    l1=map(lambda x:x+1,l)
    from functools import reduce
    l2=reduce(lambda x,y:x-y,l,-1)
    l3=filter(lambda x:True if x!=0 else False,l)
    print(list(l1),l2,list(l3))
sb1=Sb("lch",20)
print(sb1.name+"is"+shitang.yst.name)
f=wb(5)
f()
hss()
