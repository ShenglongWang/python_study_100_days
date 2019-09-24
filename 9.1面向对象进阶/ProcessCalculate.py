from time import time

def main():
    total = 0
    data = [x for x in range(1,10000001)]
    start = time()
    for num in data:
        total += num
    print(total)
    end = time()
    print('共耗时%d秒' % (end-start))

if __name__ == '__main__':
    main()