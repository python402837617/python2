import sys
print(sys.argv[0])#在外部向程序内部传递参数
# sys.exit(arg)   #程序的中将退出   但arg=0时为正常退出
print(sys.getdefaultencoding())#获得当前编码  一般为ASCII码
print(sys.getfilesystemencoding())#获取文件系统编码方式  
print(sys.path)# 获取指定模块路径的字符串集合   sys.path.append("自定义模块路径")
print(sys.platform) #获取当前系统平台
sys.modules #sys.modules是一个全局字典，该字典是python启动后就加载在
             #内存中。每当程序员导入新的模块，sys.modules将自动记录该模块。
             # 当第二次再导入该模块时，python会直接到字典中查找，
             #从而加快了程序运行的速度。它拥有字典所拥有的一切方法。
#sys.stdin,sys.stdout,sys.stderr: stdin , stdout ,
#  以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,
# 而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 
# 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们
