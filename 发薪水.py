class GZ(object):
    def __init__(self,name):
        self.name=name
    def gz(self):
        sx=int(input("shuru nide sx:"))
        sj=int(input("shuru nide sj:"))
        jbsj=int(input("shuru nide jbsj:"))
        gz=sx*sj+1.5*sx*jbsj
        return gz
jyf=GZ("jyf")
print(jyf.gz())