async function bubbleSort(arr){
    var swapped = false;
    for(let i = 0; i < arr.length; i++){
        for(let j = 0; j < arr.length; j++){
            if(arr[j] > arr[j + 1]){
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                await sleep(0)
                farger[j + 1] = "#000";
                farger[j] = "#ff6384"
                run()
            }
            if(j < arr.length - 1 -i){
                farger[j] = "#ff6384"
            }
        }
        console.log(arr.length - i)
        farger[arr.length - 1 - i] = "#000"
        run()
    }
    return arr;
}