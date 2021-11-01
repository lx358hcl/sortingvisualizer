async function bubbleSort(arr){
    var swapped = false;
    for(let i = 0; i < arr.length; i){
        swapped = false;
        for(let j = 0; j < arr.length; j++){
            swapped
            if(swapped){
                break
            }            
            if(arr[j] > arr[j + 1]){
                swapped = true;
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                await sleep(0)
                farger[j + 1] = "#000";
                farger[j] = "#ff6384"
                run()
            }
            farger[j] = "#ff6384"
            
        }
        
    }
    return arr;
}