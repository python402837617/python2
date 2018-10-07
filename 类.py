from enum import Enum
class Human():
    yellow=1
    green=2
    red=3
    def __init__(self,name,age):
        self.name=name
        self.age=age
class VIP(Enum):
    yellow=1
    yellow_alias=1
    green=2
    red=3
class VIP1(Enum):
    yellow=1
    green=2
    red=3    
#print(VIP.yellow)
#print(Human.yellow)  
#result=VIP.yellow.name==VIP1.yellow.name
#print(result)       
#for i in VIP:
    #print(i)