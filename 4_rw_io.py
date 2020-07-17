#写入文件
text='\tThis is my first test.\n\tThis is the second line.\n\tThis is the third line'
my_file = open('my_file.txt', 'w')
my_file.write(text)
my_file.close()

#增加内容
append_text='\n\tThis is appended file.'  # 为这行文字提前空行 "\n"
my_file = open('my_file.txt', 'a')
my_file.write(append_text)
my_file.close()

#读取文件
file= open('my_file.txt','r') 
content=file.read()  
print(content)

#按行读取
file= open('my_file.txt','r')
line1=file.readline()  # 读取第一行
print(line1)
line2=file.readline()  # 第二次调用自动读取第二行
print(line2)

#读取所有行
file= open('my_file.txt','r') 
content=file.readlines() # python_list 形式
for item in content:
    print(item)

#屏幕输入
a = input('please input a number: ')
#屏幕输出
print(a)

#input扩展
score=int(input('Please input your score: \n'))
if score>=90:
   print('Congradulation, you get an A')
elif score >=80:
    print('You get a B')
elif score >=70:
    print('You get a C')
elif score >=60:
    print('You get a D')
else:
    print('Sorry, You are failed ')


