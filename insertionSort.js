async function insertionSort(arr){
    if(arr.length == 1 || arr.length == 0){
        console.log("O")
        return arr
    }
    for (let i = 0; i < arr.length; i++){
        for (let j = i; j > 0; j--){
            if (arr[j] < arr[j - 1]){
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                await sleep(0)
                run()
            }
        }
        farger[i] = "#000"
        run()
    }
    run()
    return arr
}