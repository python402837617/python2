class Array(object):
    def __init__(self,size,fillvalue=None):
        self.items=list()
        for i in range(size):
            self.items.append(fillvalue)
    def __len__(self):
        return len(self.items)
    def str(self):
        return str(self.items)
    def __iter__(self):
        return iter(self.items)
    def __getitem__(self,index):
        return self.items[index]
    def __setitem__(self,index,newItem):
        self.items[index]=newItem
array=Array(5)
#增加数组大小
test=Array(len(array)*2)
for i in range(len(array)):
    test[i]=array[i]
array=test
#插入一项
targetidex=5
item=5
for i in range(len(array),targetidex,-1):
    array[i+1]=array[i]
array[item]=targetidex



    