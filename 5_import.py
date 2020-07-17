#方法一
import time
print(time.localtime())  #这样就可以print 当地时间了

#方法二
import time as t
print(t.localtime()) # 需要加t.前缀来引出功能

#方法三,只import自己想要的功能
from time import time, localtime
print(localtime())
print(time())

#方法四,import所有功能
from time import *
print(localtime())

#自建模块调用
import balance