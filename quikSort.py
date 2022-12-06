import time
def partition(array, head, tail,d,t):
  border = head
  pivot = array[tail]

  d(array, colering(len(array), head, tail, border, border))
  time.sleep(t)


  for j in range(head, tail):
    if array[j] < pivot:
      d(array, colering(len(array), head, tail, border, j, True))
      time.sleep(t)

      array[border], array[j] = array[j], array[border]
      border += 1

    d(array, colering(len(array), head, tail, border, j))
    time.sleep(t)

  d(array, colering(len(array), head, tail, border, tail, True))
  time.sleep(t)
  array[border], array[tail] = array[tail], array[border]

  return border

def quickSort(array, head, tail, d, t):
  if head < tail:
    pi = partition(array, head, tail, d, t)

    quickSort(array, head, pi - 1, d, t)

    quickSort(array, pi + 1, tail, d, t)


def colering(datalen, head, tail, border, curridx, swap= False):
    array = []
    for i in range(datalen):

        if head <= i <= tail:
            array.append("gray")
        else:
            array.append("white")
        if i == tail:
            array[i] = "orange"
        elif i == border:
            array[i] = "red"
        elif i == curridx:
            array[i] = "yellow"
        if swap:
            if border == i == curridx:
                array[i] = "green"
    return array
