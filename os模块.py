import os
print(os.name)#打印当前所在系统 windos(nt) linux(posix)
print(os.system("ipconfig"))#打印出系统命令执行后的结果
print(os.popen("ipconfig").read())#os.popen返回的是一个存储着命令结果的文件，read方法读取。
print(os.getcwd())#获得当前目录的工作路径
#os.chdir("目标目录")   #切换到目标目录
print(os.listdir())#列出字符串目录下的所有文件 默认为当前目录
#os.mkdir("目录")   #创建目录
# os.rmdir("目录") #删除目录
#os.remove("文件名") #删除文件 文件不存在时报错
#os.rename("老名字"，"新名字") #更改文件的名字
print(os.linesep) #打印操作系统的分隔符
print(os.environ) #打印出操作系统所有的环境变量
print(os.environ.get("PATH")) #打印出指定环境变量的值
print(os.path.abspath("p"))#可查看当前目录绝对路径
print(os.path.join(os.getcwd(),"ccc","ass"))#拼接出多级目录
print(os.path.exists("python"))#判断一个目录是否存在
print(os.path.split("/home/jyf")) #把目录拆分为两部分 后一部分为最后级别的目录或文件名
print(os.path.splitext("/home/jyf")) # 把目录拆分为两部分 后一部分为扩展名
