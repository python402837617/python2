from 类1 import Student
#hasattr 判断一个对象是否存在某个属性或方法
test=Student("jyf",18)
print(hasattr(test,"sex"))
#getattr    获取某个对象的属性或方法，如果不存在，打印出默认值，默认值可选。
            #需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
            #可以在后面添加一对括号。
print(getattr(test,"age","nan"))
print(getattr(test,"sex","nan"))
print(getattr(test,"jyf","nan"))
print(getattr(test,"jyf","nan")())
print(getattr(test,"f","nan"))
#setattr    给对象的属性赋值，若属性不存在，先创建再赋值。
setattr(test,"name","xjy")
setattr(test,"sex","nan")
print(test.name)
print(hasattr(test,"sex"))