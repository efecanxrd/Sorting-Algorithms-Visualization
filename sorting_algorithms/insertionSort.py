import time

def insertion_sort(data, drawData, timeTick):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k-1]:
            data[k] = data[k-1]
            k -= 1
        data[k] = temp
        drawData(data, ['#F22810' if x == k or x == i else '#C4C5BF' for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, ['#C4C5BF' for x in range(len(data))])
