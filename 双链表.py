from 单链表 import Node
#定义双向列表的类
class Twowaynode(Node):
    def __init__(self,data,previous=None,next=None):
        Node.__init__(self,data,next)
        self.previous=previous
#创建一个双向列表(通过在尾部插入创建)
head=Twowaynode(1)
tail=head
for i in range(2,7):
    tail.next=Twowaynode(i,tail)
    tail=tail.next
end=tail
while end!=None:
    print(end.data)
    end=end.previous
#创建一个带哑头的双向列表
head=Twowaynode(None)
head.next=head
head.previous=head
tail=head

for i in range(1,7):
    tail.next=Twowaynode(i,tail,head.next)
    tail=tail.next
    head.previous=tail
end=tail
while end.data!=None:
    print(end.data)
    end=end.previous
#替换第i项
start=head
while i>1 and start.next.data!=None:
    start=start.next
    i=i-1
start.next.data='value'
#删除第i项
start=head
while i>1 and start.next.next.data!=None:
    start=start.next
    i-=1
start.next=start.next.next
#在第i项插入
start=head
while i>1 and start.next.data!=None:
    start=start.next
    i-=1
start.next=Twowaynode('value',start,start.next)

