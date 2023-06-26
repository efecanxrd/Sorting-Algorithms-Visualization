import time

def partition(data, start, end, drawData, timeTick):
    i = start + 1
    pivot = data[start]

    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def quick_sort(data, start, end, drawData, timeTick):
    if start < end:
        pivot_position = partition(data, start, end, drawData, timeTick)
        quick_sort(data, start, pivot_position-1, drawData, timeTick)
        quick_sort(data, pivot_position+1, end, drawData, timeTick)

        drawData(data, ['#F22810' if x >= start and x < pivot_position else '#F22810' if x == pivot_position
                        else '#C4C5BF' if x > pivot_position and x <=end else '#C4C5BF' for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, ['#C4C5BF' for x in range(len(data))])
