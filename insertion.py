import time

def insertionSort(array, draw, Time):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        draw(array, ["red" if array[x] == key else "white" for x in range(len(array))])
        time.sleep(Time)
        while j >= 0 and key < array[j]:
            draw(array, ["black" if array[j] == array[x] else "white" for x in range(len(array))])
            time.sleep(Time)
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
        draw(array, ["blue" if array[x] == key else "white" for x in range(len(array))])
        time.sleep(Time)


