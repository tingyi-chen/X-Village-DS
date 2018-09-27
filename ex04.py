
from lib.queue import Queue

q = Queue()

def bubble_sort (lis) :
    for i in range (0, len(lis)-1) :
        for j in range (0, len(lis)-1) :
            if lis [j] > lis [j+1] :
                q.enqueue(lis[j])
                del lis[j]
                lis.insert(j+1, q.dequeue())
            else :
                continue
    return lis

some_list = [
    65, 81, 65, 19, 6, 28, 86, 40, 72, 27,
    76, 46, 22, 98, 49, 57, 52, 46, 47, 14,
    29, 15, 59, 74, 61, 47, 20, 33, 89, 99,
    65, 82, 84, 63, 93, 1, 42, 13, 54, 58,
    84, 17, 5, 18, 14, 14, 19, 42, 60, 77,
    17, 29, 2, 42, 42, 31, 47, 67, 15, 16,
    71, 56, 98, 46, 18, 20, 14, 36, 42, 23,
    87, 7, 5, 5, 52, 78, 76, 91, 92, 88, 38,
    66, 13, 18, 68, 96, 23, 51, 77, 93, 35,
    18, 9, 64, 51, 76, 76, 96, 5, 18
]
print (bubble_sort(some_list))
print (type(some_list.sort()))