class QIU(object):
    '''返回球的相关数据'''
    
    def __str__(self):
        return 1
    def __eq__(self,other):
        if type(self)!=type(other):
            return False
    @staticmethod
    def zc(r):
        zc=(4/3)*3.14*r**2
        return zc
r=int(input(""))
if r==5:
    print(QIU.zc(r))



