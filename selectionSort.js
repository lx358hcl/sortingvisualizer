async function selectionSort(arr){
    async function findMin(fromIndex){
        currentMin = fromIndex;
        for(let j = fromIndex; j < arr.length; j++){
            if (arr[j] < arr[currentMin]){
                currentMin = j
            }
            await sleep(0)
            farger[j + 1] = "#000";
            farger[j] = "#ff6384"
            run()
        }
        return currentMin
    }
    for(let i = 0; i < arr.length; i++){
        min = await findMin(i)
        if (arr[min] <= arr[i]){
            tempVal = arr[i]
            arr[i] = arr[min]
            arr[min] = tempVal
            farger[i] = "#000";
        }
    }
    farger[arr.length - 1] = "#000";
    run()
    return arr;
}