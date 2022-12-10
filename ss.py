import time

def sort(nlist, draw, Time):
    merge_sort(nlist,0,len(nlist)-1, draw, Time)

def merge_sort(nlist, start, end, draw, Time):
    # sorts the list from indexes start to end - 1 inclusive
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(nlist, start, mid, draw, Time)
        merge_sort(nlist, mid, end, draw, Time)
        merge_list(nlist, start, mid, end, draw, Time)


def merge_list(nlist, start, mid, end, draw, Time):
    draw(nlist, colorarray(len(nlist), start, mid, end))
    time.sleep(Time)

    left = nlist[start:mid]
    right = nlist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            nlist[k] = left[i]
            i = i + 1
        else:
            nlist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            nlist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            nlist[k] = right[j]
            j = j + 1
            k = k + 1

    draw(nlist, ["green" if start <= x <= end else "white" for x in range(len(nlist))])
    time.sleep(Time)


def colorarray(length, left, middle, right):
    Color = []

    for i in range(length):
        if left <= i <= right:
            if left <= i <= middle:
                Color.append("yellow")
            else:
                Color.append("orange")
        else:
            Color.append("white")

    return Color