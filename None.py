class Vip():
    def __len__(self):
        return 0
    def __bool__(self):
        return True  
vip=Vip()
a=None
if not a:
    print("t")
else:
    print("f")
if not vip:
    print("t")
else:
    print("f")
print(len(vip)) 
#实例化对象对应的布尔类型的判断
   
    
