import re
from urllib import request
class Spider():
    '''this is a spider'''
    url='https://www.panda.tv/cate/hearthstone'
    zz_htmls='<div class="video-info">([\w\W]*?)</div>'
    zz_html5_name='"video-nickname" title=([\w\W]*?)>'
    zz_html5_number='"video-number">([\w\W]*?)</span>'
    name_number=[]
    name_number1=[]
    def __wed_info(self):
        r=request.urlopen(Spider.url)
        htmls=r.read()
        htmls=str(htmls,encoding="utf-8")
        return htmls
    def __htmls_info(self,htmls):
        html5=re.findall(Spider.zz_htmls,htmls)
        for i in html5:
            html_name=re.findall(Spider.zz_html5_name,i)
            html_number=re.findall(Spider.zz_html5_number,i)
            dict_html=(html_name,html_number)
            Spider.name_number.append(dict_html)
        return Spider.name_number
        #print(Spider.name_number)
    def __html5_info(self,name_number):
        for i in name_number:
            name=re.findall("[0-9a-zA-Z\u4e00-\u9fa5]+",str(i[0]))
            number=re.findall("[\d\u4e00-\u9fa5]+",str(i[1]))
            dict_name_number=(name,number)
            Spider.name_number1.append(dict_name_number)
        return Spider.name_number1
    def sort_number(self,name_number1):
               
        l=sorted(name_number1,key=self.sorted)
        for i in l:    
            print(i)
    def sorted(self,touple):
        return int(touple[1][0])

            
                                    
    def go(self):
        htmls=self.__wed_info()
        name_number=self.__htmls_info(htmls)
        name_namber1=self.__html5_info(name_number)
        self.sort_number(name_namber1)



spider=Spider()
spider.go()        
    