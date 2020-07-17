#序列函数用于循环
print('\n')
for i in range(0,6, 1):
    print(i)

#list、 tuple 、dict 和 set 四种基本集合
#list
print('\n')
list1 = [1, 2, 3, 4, 5]
print(list1[1:3])

#list操作
#末尾添加
list1.append(0)
print(list1[-1]) #打印末位
#指定位插入
list1.insert(1,0)
print(list1[1])

print(list1.index(0)) # 显示列表中第一次出现的值为0的项的索引
print(list1.count(0)) #统计0个数
#移除项
list1.remove(2) # 删除列表中第一个出现的值为2的项
print(list1[-5:]) # 显示列表a的倒数第5位及以后的所有项的值


#tuple
print('\n')
tup = ('python', 2.7, 64)
for i in tup:
    print(i)

#dict
print('\n')
dic = {}
dic['language'] = 'python'
dic['version'] = 3.0
dic['platform'] = 64
for key in dic:
    print(key, dic[key])

#有序字典
import collections

dic = collections.OrderedDict()
dic['language'] = 'python'
dic['version'] = 3.0
dic['platform'] = 64
for key in dic:
    print(key, dic[key])

#字典操作
d1 = {'apple':1, 'pear':2, 'orange':3}
print(d1['apple'])  # 1

del d1['pear']
print(d1)   # {'orange': 3, 'apple': 1}

d1['b'] = 20
print(d1)   # {'orange': 3, 'b': 20, 'pear': 2, 'apple': 1}



#set(乱序,去除重复)
print('\n')
s = set(['python', 'python3', 'python2.7', 'python'])
for i in s:
    print(i)


