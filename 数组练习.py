from 数组 import Array
from 二维数组 import Grid
array2=Grid(5,5)
for i in range(5):
    for n in range(5):
        array2[i][n]=n-i
i,j=0,0
while i<5:
    if j>=5:
        i=i+1
        j=0
    elif array2[i][j]<0:
        break
    else:
        j=j+1
print(i,j)
array3=Array(3)
array3[0]=Array(3)
array3[1]=Array(6)
array3[2]=Array(8)
class Thid(object):
    def __init__(self,x,y,z,fillvalue=None):
        self.sarray=Grid(x,y,fillvalue)
        i,j=0,0
        while i<x:
            if j>=y:
                i=i+1
                j=0
            else:
                self.sarray[i][j]=Array(z,fillvalue)
                j=j+1
    def getx(self):
        return len(self.sarray)
    def gety(self):
        return len(self.sarray[0])
    def getz(self):
        return len(self.sarray[0][0])
    def __getitem__(self,index):
        return self.sarray[index]
array4=Thid(6,7,8)
x,y,z=0,0,0
while x<6:
    if y>=7:
        x=x+1
        y=0
        z=0
    elif z>=8:
        y=y+1
        z=0
    else:
        array4[x][y][z]=str(x)+str(y)+str(z)
        z=z+1
x,y,z=0,0,0
while x<6:
    if y>=7:
        x=x+1
        y=0
        z=0
    elif z>=8:
        y=y+1
        z=0
    else:
        print(array4[x][y][z])
        z+=1