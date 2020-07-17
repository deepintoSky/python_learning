#终端运行python代码
#Python3 ***.py

#打印字符串 要加''或者""
print('hello world')

#使用+将两个字符串链接起来
print('hello world'+' I\'m jack')

#打印运算结果
print('\n')
print(12/4)
print(int(1.9)+3) 
print(float('1.2')+3)

#数学运算**为次方
print(3**2 + 3**4)

#变量定义与使用
print('\n')
apple = 1       #赋值 数字
print('apple =', apple)
a,b,c = 11,12,13
print(a,b,c)

#while循环,循环体为缩进部分
print('\n')
count = 1
while count < 10:
    print(count)
    count+=1

#for循环
print('\n')
example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in example_list:
    print(i)
    print('inner of for')
print('outer of for')


#if判断
print('\n')
x = 1
y = 2
if x != y:
    print('x is not equal to y')
#if-else
if x > 1:
    print ('x > 1')
elif x < 1:
    print('x < 1')
else:
    print('x = 1')
print('finish')

#另一种行内表达
worked = True
result = 'done' if worked else 'not yet'
print(result)




















