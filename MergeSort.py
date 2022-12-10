# # MergeSort in Python
# import time
#
#
# def mergeSort(array, draw, Time):
#     if len(array) > 1:
#
#         #  r is the point where the array is divided into two subarrays
#         r = len(array) // 2
#         L = array[:r]
#         M = array[r:]
#
#         draw(array, colorarray(len(array), L, r, M))
#         time.sleep(Time)
#
#         # Sort the two halves
#         mergeSort(L, draw, time)
#         mergeSort(M, draw, time)
#
#         i = j = k = 0
#
#         # Until we reach either end of either L or M, pick larger among
#         # elements L and M and place them in the correct position at A[p..r]
#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 array[k] = L[i]
#                 i += 1
#             else:
#                 array[k] = M[j]
#                 j += 1
#             k += 1
#
#         # When we run out of elements in either L or M,
#         # pick up the remaining elements and put in A[p..r]
#         while i < len(L):
#             array[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(M):
#             array[k] = M[j]
#             j += 1
#             k += 1
#
#         draw(array, ["green" if L[x] <= x <= M[x] else "white" for x in range(len(array))])
#         time.sleep(Time)
#
#
# def colorarray(length, left, middle, right):
#     Color = []
#

#     for i in range(length):
#         if left <= i <= right:
#             if left <= i <= middle:
#                 Color.append("yellow")
#             else:
#                 Color.append("orange")
#         else:
#             Color.append("white")
#
#     return Color
import time


def sort(nlist, draw, Time):
    merge_sort(nlist, 0, len(nlist), draw, Time)


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