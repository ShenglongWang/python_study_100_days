# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:37:08 2019

@author: shenglong wang
@version:00.00.00
"""


import heapq


#取列表或字典中最大或最小的N个值
def heapq_Test():
    
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


import itertools


#排列/组合,笛卡尔积
def itertools_Test():
    
    #全排列
    for item in itertools.permutations('ABCD'):
        print(item)
    #组合
    for item in itertools.combinations('ABCDE',3):
        print(item)
    #笛卡尔积
    for item in itertools.product('ABCD','123'):
        print(item)
    
    
from collections import Counter

#统计字符串出现的次数，并返回前N个字符串
def collections_Test():
    
    words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
            ]
    counter = Counter(words)
    print(counter.most_common(2))
    
def BaiqianBainiao():
    '''
    穷举法 百元百鸡
    公鸡5元一只，母鸡3元一只，小鸡1元三只
    用100元买100只鸡 问公鸡母鸡小鸡各多少只
    '''
    
    for x in range(20):
        for y in range(33):
            z = 100 - x - y 
            if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
                print(x,y,z)
                
def Wurenfenyu():
    
    '''
    A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
    第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
    B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
    然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
    '''
    fish = 6
    while 1:
        total = fish
        enough = True
        for _ in range(5):
            if (total -1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5
        
'''
贪婪法例子：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
'''
class Thing(object):
    ''' 物品'''
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight
    @property
    def value(self):
        '''价格重量比'''
        return self.price / self.weight
def Beibaowenti():
    max_weight, num_of_things = 20,6
    all_things = []
    all_things.append(Thing('电脑',200,20))
    all_things.append(Thing('收音机',20,4))
    all_things.append(Thing('钟',175,10))
    all_things.append(Thing('花瓶',50,2))
    all_things.append(Thing('书',10,1))
    all_things.append(Thing('油画',90,9))
    all_things.sort(key=lambda x: x.value, reverse = True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print('小偷拿走了%s\n' % thing.name)
            total_weight += thing.weight
            total_price += thing.price
    print('总共价值%d元' % total_price)
    


'''
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小，右边都比枢轴大
'''
from random import randint
def quick_sort(origin_items, comp = lambda x,y : x <= y):
    items = origin_items[:]
    _quick_sort(items,0,len(items)-1, comp)
    return items
def _quick_sort(items,start,end,comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items,start,pos-1,comp)
        _quick_sort(items,pos+1,end,comp)
def _partition(items,start,end,comp):
    pivot = items[end]
    i = start - 1
    for j in range(start,end):
        if comp(items[j],pivot):
            i += 1
            items[i],items[j] = items[j],items[i]
    items[i+1], items[end] = items[end], items[i+1]
    return i + 1


def quick_Sort():
    items_list = [randint(0,100) for i in range(20)]
    print('before sorted......')
    print(items_list)
    temp_list = items_list[:]
    print('after sorted......')
    print(quick_sort(items_list))


'''
回溯法例子：骑士巡逻
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不
优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫
寻路等。

'''
import sys
import time
SIZE = 5
total = 0

def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4),end='')
        print()
def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
    col >= 0 and col < SIZE and \
    board[row][col] == 0:
        board[row][col] = step
        if step == SIZE*SIZE:
            global total
            total += 1
            print(f'第{total}种走法：')
            print_board(board)
        patrol(board, row-2, col-1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0

def Qishixunluo():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE - 1, SIZE - 1)

'''
动态规划例子1：斐波拉切数列。（不使用动态规划将会是几何级数复杂度）

动态规划 - 适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)
'''
def fib(num, temp={}):
    if num in (1,2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        return temp[num]

def Fib():
    result = [fib(i) for i in range(1,9)]
    print(result)





'''
动态规划例子2：子列表元素之和的最大值。（使用动态规划可以避免二重循环）

说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值，例如：

输入：1 -2 3 5 -3 2

输出：8

输入：0 -2 3 5 -1 2

输出：9

输入：-9 -2 -3 -5 -3

输出：-2
'''
def SumMax():
    items = list(map(int,input().split()))
    size = len(items)
    overall, partial = {}, {}
    overall[size - 1] = partial[size - 1] = items[size - 1]
    for i in range(size - 2, -1, -1):
        partial[i] = max(items[i], partial[i + 1] + items[i])
        overall[i] = max(partial[i],overall[i + 1])
    print(overall[0])



def main():
    #heapq_Test()
    #itertools_Test()
    #collections_Test()
    #BaiqianBainiao()
    #Wurenfenyu()
    #Beibaowenti()
    #quick_Sort()
    #Qishixunluo()
    #Fib()
    SumMax()
    
if __name__ == '__main__':
    main()



