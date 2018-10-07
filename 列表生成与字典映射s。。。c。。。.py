#字典映射其他函数的switch case 语句
#switch(i):
#    case 0:
#       vip=red
#    case 1:
#       vip=blue
#    case 2:
#       vip=yellow
#    default:
#       vip=unkwon        
def vip1():
    return "red"
def vip2():
    return "blue"
def vip3():
    return "yellow"
def vip4():
    return "unkwon"    
vip={0:vip1(),
     1:vip2(),
     2:vip3()
    }
day=1
print(vip.get(day,vip4()))
#列表生成式
l1={"red":0,"blue":1,"yellow":3}
l2={value:key for key,value in l1.items()}
l3=[key for key,value in l1.items() if value<2]
l4=(value for key,value in l1.items())
print(l3)
print(l4)#l4是一个可遍历对象 因为元组不可改变。 
print(l2)