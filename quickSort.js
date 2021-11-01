async function quickSort(arr){
    await quickSortHelper(arr, 0, arr.length - 1);
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
        }
        if (arr[left] <= arr[pivot]){
            left = left + 1
        }
        if (arr[right] >= arr[pivot]){
            right = right - 1
        }
        await sleep(0)
        farger[right] = "red";
        farger[left] = "blue";
        run()
    }
    
    // Swap pivot og høyrepeker
    temp = arr[pivot]
    arr[pivot] = arr[right]
    arr[right] = temp;

    // Quicksorter venstre side
    await quickSortHelper(arr, start, right - 1)

    // Quicksorter høyre side
    await quickSortHelper(arr, right + 1, slutt)
}
