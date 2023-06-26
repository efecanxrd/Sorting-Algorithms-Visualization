import time

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)-1):
        minimum = i
        for k in range(i+1, len(data)):
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        drawData(data, ['#F22810' if x == minimum or x == i else '#C4C5BF' for x in range(len(data))] )
        time.sleep(timeTick)
        
    drawData(data, ['#C4C5BF' for x in range(len(data))])
    