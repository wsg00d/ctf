import hashlib

'''
爆破md5值，以某前6个固定字符开始
'''

def md5(s):
    return hashlib.md5(s).hexdigest()
 
for i in range(1, 9999999):
    if md5(str(i)).startswith('1a2459'):
     print i