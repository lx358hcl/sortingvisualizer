async function quickSort(arr){
    quickSortHelper(arr, 0, arr.length - 1);
    console.log(arr)
    await sleep(0)
    run()
    return arr;
}

async function quickSortHelper(arr, start, slutt){
    if (start >= slutt) {
        return 
    }

    pivot = start
    left = start + 1
    right = slutt
    
    while (right >= left){
        if (arr[left] > arr[pivot] && arr[right] < arr[pivot]){
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            await sleep(0)
            run()
        }
        if (arr[left] <= arr[pivot]){
            left = left + 1
        }
        if (arr[right] >= arr[pivot]){
            right = right - 1
        }
    }
    
    // Swap pivot og høyrepeker
    temp = arr[pivot]
    arr[pivot] = arr[right]
    arr[right] = temp;
    await sleep(0)
    run()

    // Quicksorter venstre side
    quickSortHelper(arr, start, right - 1)

    // Quicksorter høyre side
    quickSortHelper(arr, right + 1, slutt)
}

// var arr = [6,8,2,1,7,9,7,7,4,2,2]

// console.log(quickSort(arr))