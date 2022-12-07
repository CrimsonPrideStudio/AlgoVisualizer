import time


def bubble(data, drawdata, Time_tik):
    i = len(data)
    color = []
    for _ in range(0,len(data)):
        color.append('red')
    for _ in range(len(data)):
        i-=1
        for j in range(0, i ):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                for c in range(i+1):
                    if j==c or c==j+1:
                        color[c]='blue'
                    else:
                        color[c] = 'red'
                drawdata(data,color)


                time.sleep(Time_tik)
        color[i]='green'
        drawdata(data, color)
        print(i)
    drawdata(data, ['green' for x in range(len(data))])
