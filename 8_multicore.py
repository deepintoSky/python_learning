#导入模块	
import multiprocessing as mp
import time

#被调用的函数
def job1(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue存入

def job2(x):
    return x*x


def job3(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1) 
        v.value += num # 获取共享内存
        print(v.value)
    l.release() # 释放

#方法一
def multicore1():
    #创建队列存储进程结果
    q = mp.Queue()

    #创建2进程
    p1 = mp.Process(target=job1,args=(q,))#只有一个参数要有逗号表示可迭代
    p2 = mp.Process(target=job1,args=(q,))

    #启动
    p1.start()
    p2.start()

    #连接
    p1.join()
    p2.join()

    #queue读取
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)#进程结果汇总


#方法二:用进程池
def multicore2():
    pool = mp.Pool(processes=4) #自定义核数量
    res = pool.map(job2, range(10))
    print(res)
    res = pool.apply_async(job2, (2,))
    # 用get获得结果
    print(res.get())
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job2, (i,)) for i in range(10)]
    # 从迭代器中取出
    print([res.get() for res in multi_res])


#共享内存与进程锁
def multicore3():
    l = mp.Lock() # 定义一个进程锁
    v = mp.Value('i', 0) # 定义共享内存
    p1 = mp.Process(target=job3, args=(v,1,l)) # 需要将lock传入
    p2 = mp.Process(target=job3, args=(v,3,l)) 
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__=='__main__':

    multicore1()
    multicore2()
    multicore3()

