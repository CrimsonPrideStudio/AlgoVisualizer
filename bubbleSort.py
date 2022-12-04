import time


def bubble(data, drawdata, Time_tik):
    for _ in range(len(data)):
        for j in range(0, len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawdata(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(Time_tik)
    drawdata(data, ['green' for x in range(len(data))])
