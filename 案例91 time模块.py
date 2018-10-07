import time
print(time.process_time())#在第一次调用的时候，返回的是程序运行的实际时间
a=time.time()#时间戳形式
b=time.localtime(a)#元组形式
c=time.ctime(a)#正常形式
print(time.time())#返回当前时间时间戳类型的时间
print(time.localtime(a))#将时间戳形式的时间转化为元组形式
print(time.ctime(a))#将时间戳形式转化为正常形式
print(time.gmtime(a))#将时间戳形式的时间转化为元组形式 0时区的
print(time.mktime(b))#将元组形式转化为时间戳形式
#time.sleep(10)#延迟指定秒数后执行
print(time.strftime('%Y-%m-%d %H:%M:%S',b))#格式化元组形式的时间
print(time.asctime(b))#将元组形式转化为正常形式

print(time.perf_counter())#以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔
import calendar
print(calendar.month(2018,9))#打印出2018年9月的日历打印出2018年9月的日历
print(calendar.month(2020,10))