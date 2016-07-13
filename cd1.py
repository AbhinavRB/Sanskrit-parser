'''from bs4 import BeautifulSoup,SoupStrainer
import urllib2
import re
req = urllib2.Request("https://sa.wikipedia.org/wiki/%E0%A4%AD%E0%A4%97%E0%A4%B5%E0%A4%A6%E0%A5%8D%E0%A4%97%E0%A5%80%E0%A4%A4%E0%A4%BE")#("http://hindi.webdunia.com/religion/religion/hindu/geeta/Chapter10_1-7.htm")
page = urllib2.urlopen(req)
links = SoupStrainer(['i'])
soup1 = BeautifulSoup(page, parse_only=links)
a=[]
b=[]
for link in soup1.find('i'):#, attrs={"class": "pdngT10 marronHead"}):
    a.append(link)



f=open("inp.txt","w")
f.write(a[0].encode('utf-8'))

f.close()'''
import re
f=open("s1.txt","r")
a=f.read()
l=[]


#Hrasvasvara
hswara = [u'\u0905' ,  u'\u0907' ,  u'\u0909' ,  u'\u090B' ,  u'\u090C']
#Deerghasvra
dswara = [u'\u0906' ,  u'\u0908' ,  u'\u090A' ,  u'\u090F' ,  u'\u0910',  u'\u0913' ,  u'\u0914', u'\u0960']
#Yogavahaka
yog=[u'\u0902', u'\u0903']
#Hrasvasvara mathra
hsm=[u'\u093f' ,  u'\u0941' ,  u'\u0943']
#Deerghasvara mathra
dsm=[u'\u0902', u'\u0903', u'\u093e' ,  u'\u0940' ,  u'\u0942' ,  u'\u0944' ,  u'\u0947',  u'\u0948' ,  u'\u094b', u'\u094c']
#Halanth
halanth=[u'\u094d']
#Vyanjana
vyanjana = [u'\u0915', u'\u0916', u'\u0917' ,  u'\u0918' ,  u'\u0919' ,  u'\u091A' ,  u'\u091B',  u'\u091C' ,  u'\u091d', u'\u091e', u'\u091f', u'\u0920', u'\u0921', u'\u0922' ,  u'\u0923' ,  u'\u0924' ,  u'\u0925' ,  u'\u0926',  u'\u0927' ,  u'\u0928', u'\u092a', u'\u092b', u'\u092c', u'\u092d', u'\u092e' ,  u'\u092f' ,  u'\u0930' ,  u'\u0932' ,  u'\u0933',  u'\u0935' ,  u'\u0936', u'\u0937', u'\u0938', u'\u0939']
#Full stop
fs=[u'\u0964',u'\u0965']


a=a.decode('utf-8')
i=0
while(i<len(a)):
    
    if(a[i] in hswara):
        if(a[i+1] in yog):
            l.append(1)
            i+=2
        else:
            l.append(0)
            i+=1
    elif(a[i] in dswara):
        l.append(1)
        if(a[i+1] in yog):
            i+=2
        else:
            i+=1
    elif(a[i] in vyanjana):
        if(a[i+1] in hsm):
            if(a[i+2] in yog):
                l.append(1)
                i+=3
            else:
                l.append(0)
                i+=2
        elif(a[i+1] in dsm):
            l.append(1)
            if(a[i+2] in yog):
                i+=3
            else:
                i+=2
        elif(a[i+1] in halanth):
            l.pop()
            l.append(1)
            if(a[i+3] in hsm):
                if(a[i+4] in yog):
                    l.append(1)
                    i+=5
                else:
                    l.append(0)
                    i+=4
            elif(a[i+3] in dsm):
                l.append(1)
                if(a[i+4] in yog):
                    i+=5
                else:
                    i+=4
            elif(a[i+3] in vyanjana):
                l.append(0)
                i+=3
            elif(a[i+3] in halanth):
                    
                if(a[i+5] in hsm):
                    if(a[i+6] in yog):
                        l.append(1)
                        i+=7
                    else:
                        l.append(0)
                        i+=6
                elif(a[i+5] in dsm):
                    l.append(1)
                    if(a[i+6] in yog):
                        i+=7
                    else:
                        i+=6
                elif(a[i+5] in vyanjana):
                    l.append(0)
                    i+=5
                    #
                else:
                    l.append(0)
                    i+=3
        elif(a[i+1] in vyanjana or a[i+1]==' '):
            l.append(0)
            i+=1
        elif(a[i+1] is ' '):
            l.append(0)
            i+=1
    
    elif(a[i] in fs):
        l.pop()
        l.append(1)
        i+=1
    elif(a[i]==' '):
        i+=1

obtained = ''.join(str(e) for e in l)
print(u'\u0932\u0918\u0941 = '+'0')
print(u'\u0917\u0941\u0930\u0941 = '+'1')
print(obtained)
names={'indravajra':u'\u0907\u0928\u094d\u0926\u094d\u0930\u0935\u091c\u094d\u0930\u093e',
       'upendravajra':u'\u0909\u092a\u0947\u0928\u094d\u0926\u094d\u0930\u0935\u091c\u094d\u0930\u093e',
       'vasanthathilaka':u'\u0935\u0938\u0928\u094d\u0924\u0924\u093f\u0932\u0915',
       'malini':u'\u092e\u093e\u0932\u093f\u0928\u0940'}
ganas={'111':u'\u092e','011':u'\u092f','101':u'\u0930','001':u'\u0938','110':u'\u0924',
       '010':u'\u091c','100':u'\u092d','000':u'\u0928'}
dic={'indravajra':'11011010111',
'upendravajra':'01011001011',
'vasanthathilaka':'11010001001011',
'malini':'000000111011011',
'mandaakranthavruttham':'11110000011011011',
'shardoolavikreeditham':'1110010100011101101',
'sragdhara':'111101100000011011011'}
for i in dic.keys():
    if(obtained==dic[i]):
        print(u'\u091b\u0928\u094d\u0926\u0903: '+names[i])
        break
        
padalength = len(obtained)
if padalength%3==1: padalength-=1
elif padalength%3==2: padalength-=2
obtainedGana=' '.join([ganas[obtained[i:i+3]] for i in range(padalength) if i%3==0])
obtainedGana+=' '.join([i for i in obtained[padalength:]])
print(u'\u0917\u0923: '+obtainedGana)
