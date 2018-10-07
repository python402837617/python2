'''定义一个类实现探测器的功能'''
import time
import random
class Profiler(object):
    #探测函数
    def test(self,function,lyst=None,size=10,unique=True,comp=True,exch=True,trance=True):
        '''这是一个实现探测功能的实力方法'''
        self._comp=comp
        self._exch=exch
        self._trance=trance
        if lyst != None:
            self._lyst=lyst
        else:
            self._lyst=[]
            for i in range(size):
                self._lyst.append(random.randint(1,size))
        self._count_comp=0
        self._count_exch=0
        self._startclock()
        function(self._lyst,self)
        self._stopclock()
        print(self)
    def exchange(self):
        if self._exch:
            self._count_exch+=1
        if self._trance:
            print(self._lyst)
    def compare(self):
        if self._comp:
            self._count_comp+=1
    def _startclock(self):
        self._start=time.time()
    def _stopclock(self):
        self._stop=time.time()
    def __str__(self):
        result="problem size"
        result+=str(len(str(self._lyst)))+"\n"
        result+="Elapsed time"+str(self._stop-self._start)+"\n"
        if self._comp:
            result+="count_compare"+str(self._count_comp)
        if self._exch:
            result+="count_exchange"+str(self._count_exch)
        return result

