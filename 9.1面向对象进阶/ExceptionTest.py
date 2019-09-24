


"""
import exceptions

def dirException():
    print(dir(exceptions))
"""

#异常练习
def f1():
    print(1/0)

def f2():
    try:
        f1()
    except Exception as e:
        raise

#单进程下载文件练习
from random import randint
from time import time,sleep
from os import getpid

def download_task(filename):
    print('[%d]开始下载%s...' % (getpid(),filename))
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗时%d秒' % (filename,time_to_download))
    
#单进程下载演示
def main1():
    start = time()
    download_task('python入门.pdf')
    download_task('BigData.txt')
    end = time()
    print('总共耗费了%.2f秒' % (end-start))
    
    


#多进程下载演示
from multiprocessing import Process
def main2():
    start = time()
    p1 = Process(target=download_task,args=('java从入门到放弃.pdf',))
    p1.start()
    p2 = Process(target=download_task,args=('春华秋实.txt',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('[%d]下载完成！总共耗时%d' % (getpid(),(end-start)))    


#使用多线程模拟文件下载
from threading import Thread,Lock

def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗时%d秒' % (filename,time_to_download))

def main3():
    start = time()
    t1 = Thread(target=download,args=('多愁善感.pdf',))
    t1.start()
    t2 = Thread(target=download,args=('无所畏惧.txt',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时%.3f秒' % (end-start))


#继承线程类来模拟多线程下载文件

class DownloadTask(Thread):
    def __init__(self,filename):
        super().__init__()
        self._filename = filename
    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_down = randint(5,10)
        sleep(time_to_down)
        print('%s下载完成！耗费了%d秒' % (self._filename,time_to_down))

def main4():
    start = time()
    t1 = DownloadTask('Thinking.pdf')
    t1.start()
    t2 = DownloadTask('AutoControl.txt')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时%.2f秒.' % (end-start))




"""
不加锁模拟多个线程对同意账户存钱
"""

class Account(object):
    def __init__(self):
        self._balance = 0
        #加锁处理
        self._lock = Lock()
    def deposit(self,money):
        """
        #不加锁处理
        new_balance = self._balance + money
        sleep(0.01)
        self._balance = new_balance
        """
        #加锁处理
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()
    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def main5():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account,1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为：￥%d 元' % account.balance)





def main():
    #dirException()
    #f2()
    #main1()
    #main2()
    #main3()
    #main4()
    main5()
if __name__ == "__main__":
    main()