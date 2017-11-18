#coding=utf-8
#author:wsg00d
#date:2017/11/18

'''
ctf考试题目
用request模块的cookie带cookie连续访问3次
第一次抓取网页中的header和网页中的字符串(后3位未知)，
然后循环3次匹配爆破其sha1加密值和header值对比成功后，第二次带cookie只post提交后3位
第三次带cookie最后再次提交一个数学表达式的值
'''

import requests
import re
import hashlib
url='http://106.75.90.70:1111/'

r=requests.get(url)
print r.content
xheader=r.headers['ciphertext']
xstr=''.join(re.findall('\+(\w+)',r.content))
xcookie=r.cookies

print xheader,xcookie,xstr

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            a=str(i)+str(j)+str(k)+xstr
            #print a
            if hashlib.sha1(a).hexdigest()==xheader:
                print a
                data={
                    'pass':str(i)+str(j)+str(k)
                }

                r1=requests.post(url=url,data=data,cookies=xcookie)
                print r1.text
                xstr = ''.join(re.findall('算出值提交：(.*) -->', r1.content))
                print xstr
                print eval(xstr)
                data={'pass':eval(xstr)}
                r2=requests.post(url=url,data=data,cookies=xcookie)
                print r2.content