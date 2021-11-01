import time
import random
import heapq
import numpy as np
from numpy.lib.function_base import insert

def selectionSortSondre(l):
    counter = 0
    for i in range(len(l)):
        m = i # Lagrer index til den laveste
        for j in range(i, len(l)):
            # Finner minste i resten av listen 
            counter += 1
            if l[j] < l[m]:
                m = j
        if l[m] < l[i]:
            # Swap
            temp = l[i]
            l[i] = l[m]
            l[m] = temp
    return l

def insertionSortSondre(l):
    counter = 0
    for i in range(1, len(l)):
        j = i
        while j > 0:
            counter += 1
            if l[j] < l[j-1]:
                # Swap 
                temp = l[j]
                l[j] = l[j-1]
                l[j-1] = temp 
            j -= 1 
    return l

def heapSortSondre(l):
    counter = 0

    h = []
    for e in l:
        heapq.heappush(h, e)
    l.clear()
    while h:
        l.append(heapq.heappop(h))
        
    return l

def bubbleSortSondre(inputList):
    iterations = 0
    for i in range(len(inputList)):
        swapped = False
        for j in range(len(inputList)-1):
            iterations += 1
            if inputList[j] > inputList[j+1]:
                temp = inputList[j]
                inputList[j] = inputList[j+1]
                inputList[j+1] = temp 
                swapped = True
        if not swapped: break

    return inputList

def selectionSort2(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j

        if min != i:
            tmp = arr[min]
            arr[min] = arr[i]
            arr[i] = tmp
    return arr

def insertionSort2(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            tmp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = tmp
            j -= 1
    return arr

def heapSort2(arr):
    heapq.heapify(arr)
    aux = []

    while arr:
        aux.append(arr.pop(0))
        heapq.heapify(arr)

    return aux

def bubbleSort2(arr):
    for _ in range(len(arr)):
        swaps = 0
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                tmp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = tmp
                swaps += 1

        if swaps == 0:
            break
    return arr

def createBigArray(start, end, size):
    arr = []
    for i in range(0, size):
        arr.append(random.randint(start, end))
    return arr

def selectionSort(arr):
    def findMin(fromIndex):
        currentMin = fromIndex
        for j in range(fromIndex, len(arr)):
            if arr[j] < arr[currentMin]:
                currentMin = j
        return currentMin
    
    for i in range(0, len(arr)):
        min = findMin(i)
        if arr[min] < arr[i]:
            tempVal = arr[i]
            arr[i] = arr[min]
            arr[min] = tempVal 
    return arr         

def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def heapSort(arr):
    heapq.heapify(arr)
    res = []
    for i in range(0, len(arr)):
        res.append(heapq.heappop(arr))
    return res

def insertionSort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
    return arr
            
def testSortingFunctions():
    bigArray = createBigArray(0, 100, 10000)
    sortedFasit = bigArray[:]
    sortedFasit.sort()
    
    print("______Bubble Sort______")
    comp = set()
    ## LUKA: Running Bubble Sort
    print("=> LUKA Bubble Sort")
    timeStart = time.process_time()
    res = bubbleSort(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Luka"))
    print("      LUKA Bubble Sort took: ", timeTaken, np.array_equal(sortedFasit,res))
    
    ## SERGEY: Running Bubble Sort 
    print("=> SERGEY Bubble Sort")
    timeStart = time.process_time()
    res = bubbleSort2(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Sergey"))
    print("      SERGEY Bubble Sort took: ", timeTaken, np.array_equal(sortedFasit,res))
    
    ## SONDRE: Running Bubble Sort 
    print("=> SONDRE Bubble Sort")
    timeStart = time.process_time()
    res = bubbleSortSondre(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Sondre"))
    print("      SONDRE Bubble Sort took: ", timeTaken, np.array_equal(sortedFasit,res))
    comp = list(comp)
    comp.sort()
    print("Gold: ", comp[0])
    print("Silver: ", comp[1])
    print("Bronze: ", comp[2])

    print("\n______Heap Sort______")
    comp = set()
    ## SONDRE: Running HeapSort
    print("=> SONDRE Heap Sort")
    timeStart = time.process_time()
    res = heapSortSondre(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Sondre"))
    print("      SONDRE: Heap Sort took: ", timeTaken, np.array_equal(sortedFasit, res))
    
    ## LUKA: Running HeapSort
    print("=> LUKA Heap Sort")
    timeStart = time.process_time()
    res = heapSort(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Luka"))
    print("      LUKA Heap Sort took: ", timeTaken, np.array_equal(sortedFasit, res))
    
    ## SERGEY: Running HeapSort
    print("=> SERGEY Heap Sort")
    timeStart = time.process_time()
    res = heapSort2(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Sergey"))
    print("      SERGEY: Heap Sort took: ", timeTaken, np.array_equal(sortedFasit, res))
    comp = list(comp)
    comp.sort()
    print("Gold: ", comp[0])
    print("Silver: ", comp[1])
    print("Bronze: ", comp[2])
    
    print("\n______Insertion Sort______")
    comp = set()
     ## SERGEY: Running InsertionSort
    print("=> SERGEY: Insertion Sort")
    timeStart = time.process_time()
    res = insertionSort2(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Sergey"))
    print("      SERGEY: Insertion Sort took: ", timeTaken, np.array_equal(sortedFasit, res))
    
    ## LUKA Running InsertionSort
    print("=> LUKA Insertion Sort")
    timeStart = time.process_time()
    res = insertionSort(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Luka"))
    print("      LUKA Insertion Sort took: ", timeTaken, np.array_equal(sortedFasit, res))
    
    ## SONDRE: Running InsertionSort
    print("=> SONDRE: Insertion Sort")
    timeStart = time.process_time()
    res = insertionSortSondre(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Sondre"))
    print("      SONDRE: Insertion Sort took: ", timeTaken, np.array_equal(sortedFasit, res))
    comp = list(comp)
    comp.sort()
    print("Gold: ", comp[0])
    print("Silver: ", comp[1])
    print("Bronze: ", comp[2])
    
    print("\n______Selection Sort______")
    comp = set()
    ## SONDRE Running SelectionSort
    print("=> SONDRE: Selection Sort")
    timeStart = time.process_time()
    res = selectionSortSondre(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Sondre"))
    print("      SONDRE: Selection Sort took: ", timeTaken, np.array_equal(sortedFasit, res))
    
    ## LUKA: Running SelectionSort
    print("=> LUKA: Selection Sort")
    timeStart = time.process_time()
    res = selectionSort(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Luka"))
    print("      Selection Sort took: ", timeTaken, np.array_equal(sortedFasit, res))
    
    ## SERGEY: Running SelectionSort
    print("=> SERGEY: Selection Sort")
    timeStart = time.process_time()
    res = selectionSort2(bigArray[:])
    # print(res)
    # print(sortedFasit)
    timeTaken = time.process_time() - timeStart;
    comp.add((timeTaken, "Sergey"))
    print("      SERGEY: Selection Sort took: ", timeTaken, np.array_equal(sortedFasit, res))
    comp = list(comp)
    comp.sort()
    print("Gold: ", comp[0])
    print("Silver: ", comp[1])
    print("Bronze: ", comp[2])
    
testSortingFunctions()