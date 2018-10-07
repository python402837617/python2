#from 探测器 import Profiler
def swap(list,i,j):
    list[i],list[j]=list[j],list[i]
    #选择排序
def xzpx1(list,p):
    for i in range(len(list)):
        for n in range(i,len(list)):
            if list[n]<list[i]:
                swap(list,i,n)
#xzpx1(l)
#p.test(xzpx1)
print()
def xzpx(list):
    for i in range(len(list)):
        minnum=i
        j=i+1
        while j<len(list):
            if list[j]<list[minnum]:
                minnum=j
            j+=1
        if list[i]!=list[minnum]:
            swap(list,i,minnum)
l=[8,5,9,4,7,3,6]


#冒泡排序
def mppx(list):
    n=len(list)
    while n>1:
        i=1
        while i<n:
            if list[i]<list[i-1]:
                swap(list,i,i-1)
            i+=1
        n=n-1
def mppx1(list):
    n=0
    while n<len(list):
        for i in range(len(list)-1):
            if list[i]>list[i+1]:
                swap(list,i,i+1)
        n+=1
mppx1(l)
#print(l)
#插入排序
def crpx(list):
    i=1
    while i<len(list):
        j=i-1
        while j>=0: 
            if list[j]>list[j+1]:
                swap(list,j,j+1)
            j-=1
        i=i+1
#crpx(l)
print(l)
def crpx1(lyst):
    for i in range(len(lyst)):
        j=i+1
        while 0<j<len(lyst):
            if lyst[j]<lyst[j-1]:
                swap(lyst,j,j-1)
                j-=1
            else:
                break
l7=[8,2,9,6,7,5,3,4,1]
crpx1(l7)
print(l7)
#快速排序
#快速排序的一个list实现
def step(list,left,right):
    #find the pivot and exchange with last
    middle=(left+right)//2
    pivot=list[middle]
    list[middle]=list[right]
    list[right]=pivot
    #set boundary(边界) to first position
    boundary=left

    for i in range(left,right):
        if list[i]<pivot:
            swap(list,i,boundary)
            boundary+=1
    swap(list,right,boundary)
    return boundary
#对各个子列也实现
def sonstep(list,left,right):
    if left<right:
        position=step(list,left,right)
        sonstep(list,left,position-1)
        sonstep(list,position+1,right)
def quiklysort(list):
    sonstep(list,0,len(list)-1)
#生成一个随机列表
import random
def main(n,sort=quiklysort):
    list=[]
    while n>0:
        number1=random.randint(1,n+1)
        list.append(number1)
        n-=1
    print(list)
    sort(list)
    print(list)
if __name__=="__main__":
    main(20)
#合并排序
def merge(lyst,array,low,middle,high):
    left1=low
    left2=middle+1
    for i in range(low,high+1):
        if lyst[left1]<lyst[left2]:
            array[i]=lyst[left1]
            left1+=1
        elif left1>middle:
            array[i]=lyst[left2]
            left2+=1
        elif left2>high:
            array[i]=lyst[left1]
            left1+=1
        else:
            array[i]=lyst[left2]
            left2+=1
    for i in range(low,high+1):
        lyst[i]=array[i]
def mergesorthelp(lyst,array,low,high):
    if low<high:
        middle=(low+high)//2
        mergesorthelp(lyst,array,low,middle)
        mergesorthelp(lyst,array,middle+1,high)
        merge(lyst,array,low,middle,high)
import array

def mergesort(lyst):
    array1=array.ArrayType(7 )
    mergesorthelp(lyst,array1,0,len(lyst)-1)
l=[8,5,9,7,2,6,4]
mergesort(l)
print(l)