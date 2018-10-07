class Node(object):
    '''定义一个链表'''
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
#用循环创造一个链表
head=None
for i in range(1,10):
    head=Node(i,head)
#会释放空间的fangwen
#while head!=None:
 #   print(head.data)
  #  head=head.next
#不会释放空间的访问，遍历
start=head
while start!=None:
    print(start.data)
    start=start.next
#搜索指定项
start=head
targetitem=5
while start.data!=targetitem and start!=None:
    start=start.next
if start==None:
    print("no")
else:
    print('yes')
#替换指定值的项
start=head
targetitem=6
replaceitem=11
while  start!=None and start.data!=targetitem:
    start=start.next
if start!=None:
    start.data=replaceitem
    print('true')
else:
    print('faulse')
#替换第i项
start=head
i=4
replaceitem=12
while i>0 and start!=None:
    start=start.next
    i-=1
if start!=None:
    start.data=replaceitem
    print(True)
else:
    print(False)
#链表头部插入
head=Node('value',head)
#链表尾部插入
newitem=Node("value")
if head==None:
    head=newitem
else:
    start=head
    while start.next!=None:
        start=start.next
    head.next=newitem
#链表头部删除
value=head.data
head=head.next
print(value)
#链表尾部删除
if head.next==None:
    head=None
else:
    start=head
    while start.next.next!=None:
        start=start.next
    start.next=None
#在任意位置插入
i=5
if head==None or i<0:
    head=Node('value',head)
start=head
while i>1 and start.next!=None:
    start=start.next
    i-=1
start.next=Node('value',start.next)
#在任意位置删除
if i<0:
    head=head.next
start=head
while i>1 and start.next.next!=None:
    start=start.next
    i-=1
start.next=start.next.next
 


