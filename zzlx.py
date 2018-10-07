import re

a='["axaxaxaxaxxxxx"]'
b=re.findall('\w*',a)
c=re.match('5{3}',a)
d=re.search('x',a)

#print
print(b)
#print(c)
#print(d.span()[0])
