import hashlib

a='38e4c352809e150186920aac37190cbc'

for i in range(32,127):
 for j in range(32,127):
  for k in range(32,127):
   for l in range(32,127):
    md5=hashlib.md5()
    b='flag{www_shiyanbar_com_is_very_good_'+chr(i)+chr(j)+chr(k)+chr(l)+'}'
    #print hashlib.md5(b).hexdigest()
    if hashlib.md5(b).hexdigest()==a:
     print b
     exit()
	

