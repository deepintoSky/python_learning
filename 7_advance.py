#简易函数定义
fun = lambda x, y: x+y
x = 1
y = 3.2
print(fun(y, x))

#捆绑参数并可视化
print( list(map(fun,[1],[2])), list(map(fun,[1,2],[3,4])) )

#深/浅拷贝
import copy
a=[1,2,[3,4]]
b1 =  #全引用
b2 = copy.copy(a) #外围拷贝值,内部引用
b3 = copy.deepcopy(a) #全拷贝值本身

b1[1]=22
b1[2][0] = 33
print(b1, b2, b3, a)

b2[1]=222
b2[2][0] = 333
print(b1, b2, b3, a)

b3[1]=2222
b3[2][0] = 3333
print(b1, b2, b3, a)

a[0] = 11
a[2][1] = 44
print(b1, b2, b3, a)

#正则表达式


