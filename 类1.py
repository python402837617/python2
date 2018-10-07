from 类 import Human
class Student(Human):
    name="jyf"
    sum=0
    __teacher="jyf"
    def __init__(self,name,age):
        #print(name)
        #print(self.sum)
        super(Student,self).__init__(name,age)
    def jyf(self):
            print(self.sum)
    @classmethod
    def sum1(cls):
        print(Student.sum)
        print(cls.sum)
student1=Student('xjy',18)
#student1.sum1()
#student1.jyf()
#print(student1.sum)
#print(1/2)
print(student1.sum)