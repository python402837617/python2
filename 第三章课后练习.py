def ss(list,n):
    '''顺序搜索，当目标比给定的元素要小时，停止'''
    for i in range(len(list)):
        if i>n:
            break
import timeit
def reserve(list):
    list=[list[-i] for i in range(len(list))]
    print( list)

def expo(ds,zs):
    if ds==0:
        return "no"
    elif zs==0:
        return 1
    elif zs==1:
        
        return ds
    else:
        return ds*expo(ds,zs-1)
print(expo(3,5))
t=timeit.Timer("expo","from __main__ import expo")
sum=1
print(t.timeit(1000000))
from 排序 import swap
def kspx(lyst,left,right):
    #找到中间值并于最后的交换
    middle=(left+right)/2
    m_number=lyst(middle)
    lyst[middle]=lyst[right]
    lyst[right]=m_number
    #设置边界
    bianjie=0
    #分边
    for i in range(len(lyst)):
        if lyst[i]>m_number:
            swap(lyst,i,bianjie)
            bianjie+=1
    swap(lyst,right,bianjie)
def kspx_sort(lyst,left,right):
    if left<right:
        middle=(left+right)/2
        kspx(lyst,left,right)
        kspx_sort(lyst,left,middle)
        kspx_sort(lyst,middle+1,right)
def kspx_go(lyst,reserve=False):
    if not reserve:
        kspx_sort(lyst,0,len(lyst)-1)