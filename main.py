from tkinter import *
from tkinter import ttk
import random
from sorting_algorithms.bubbleSort import bubble_sort
from sorting_algorithms.selectionSort import selection_sort
from sorting_algorithms.insertionSort import insertion_sort
from sorting_algorithms.mergeSort import merge_sort
from sorting_algorithms.quickSort import quick_sort


# Main root 
root = Tk()
root.title("Sorting Algorithms")
root.maxsize(1000, 700)
root.config(bg = '#FFFFFF')


algorithm_name = StringVar()
speed_name = StringVar()
data = []
algorithm_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort']
speed_list = ['Fast', 'Medium', 'Slow']
arraySize = 200
print('Arr',arraySize)
# Drawing the numerical array as bars
def draw(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    root.update_idletasks()


# Randomly generate array
def generate():
    global data

    data = []
    arraySize = sizeEntry.get()
    for i in range(0, int(arraySize)):
        random_value = random.randint(1, 300)
        data.append(random_value)

    draw(data, ['#C4C5BF' for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, draw, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, draw, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, draw, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, draw, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, draw, timeTick)



### User interface ###
UI_frame = Frame(root, width= 900, height=300, bg='#FFFFFF')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

i1 = Label(UI_frame, text="Algorithm: ", bg='#FFFFFF')
i1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algorithm_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

i2 = Label(UI_frame, text="Sorting Speed: ", bg='#FFFFFF')
i2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

i3 = Label(UI_frame, text="Array Size: ", bg='#FFFFFF')
i3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=2, column=1,  padx=5, pady=5)

canvas = Canvas(root, width=800, height=400, bg='#FFFFFF')
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort", command=sort, bg='#C4C5BF')
b1.grid(row=3, column=1, padx=5, pady=5)

b2 = Button(UI_frame, text="Generate Array", command=generate, bg='#C4C5BF')
b2.grid(row=3, column=0, padx=5, pady=5)


root.mainloop()