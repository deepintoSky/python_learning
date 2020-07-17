#def 函数
#def function_name(parameters):
#    expressions
#如果想要函数有返回值, 在 expressions 中的逻辑代码中用 return 返回

#定义
def func(x, y):
    print('this is a function')
    a = x+y
    print(a)
    return a, x


#默认参数
def sale_car(price, color='red', brand='carmy', is_second_hand=True):
    print('price', price,
          'color', color,
          'brand', brand,
          'is_second_hand', is_second_hand)


#可变参数,放在特定参数和默认参数后面
def report1(name, *grades):
	total = 0
	for grade in grades:
		total += grade
	print('\n', name, '\'total grade is', total)


#关键字参数,放在最后
#输入任意个数自定义参数名的参数,在函数内部自动封装成一个字典(dict)
def report2(name, **para_dict):
	print('\nname is', name)
	for para_name, para_data in para_dict.items():
		print(para_name, para_data)

#局部变量与全局变量
a = None
def fun():
    global a    # 使用之前在全局里定义的 a
    a = 20      # 现在的 a 是全局变量了
    return a+100


def main():
	#调用1
	b, c = func(1, 2.5)
	print('\nfunc\'result is ')
	print(b, c)
	#调用2
	d = func(y=2.5, x=1)
	print('\nfunc\'result is ', d[0], d[1])

	sale_car(1000)
	sale_car(1000, 'black')

	report1('jack', 2)
	report1('jack', 2,5,6)
	
	report2('Mike', age=24, country='China', education='bachelor') 

	print('\n', fun())


#自调用实现,一般把这些代码放入脚本最后
#如果执行该脚本的时候，该 if 判断语句将会是 True,那么内部的代码将会执行。 
#如果外部调用该脚本，if 判断语句则为 False,内部代码将不会执行。
if __name__ == '__main__':
    main()


