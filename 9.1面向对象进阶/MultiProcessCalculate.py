from time import time
from random import randint
from multiprocessing import Process,Queue

def task_handler(cur_list,result_queue):
    total = 0
    for number in cur_list:
        total +=number
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1,10000001)]
    result_queue = Queue()
    index = 0
    for _ in range(8):
        p = Process(target = task_handler, args = (number_list[index:index + 1250000],result_queue))
        index += 1250000
        processes.append(p)
        p.start()
    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('共耗时%d秒' % (end-start))

if __name__ == '__main__':
    main()