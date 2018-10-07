from 数组 import Array
class Grid(object):
    def __init__(self,rows,columns,fillvalue=None):
        self.array=Array(rows)
        for i in range(rows):
            self.array[i]=Array(columns,fillvalue)
    def getrows(self):
        return len(self.array)
    def getcolumns(self):
        return len(self.array[0])
    def __getitem__(self,index):
        return self.array[index]
    def __str__(self):
        result=""
        for row in range(self.getrows()):
            for column in range(self.getcolumns()):
                result=result+self.array[row][column]
            result=result+"\n"
        return result
