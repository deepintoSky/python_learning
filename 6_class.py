class Calculator:       #首字母要大写，冒号不能缺
    name='Good Calculator'  #该行为class的属性
    price=18

    #初始化函数,name和price要指定
    def __init__(self,name,price,hight=10,width=14,weight=16): #后面三个属性设置默认值,查看运行
        self.name=name
        self.price=price
        self.h=hight
        self.wi=width
        self.we=weight

    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)


if __name__ == '__main__':
    cal = Calculator('bad calculator',18)
    print(cal.name, cal.h, cal.wi, cal.we)
    cal.times(2, 3)
    cal.divide(2.1, 2)
