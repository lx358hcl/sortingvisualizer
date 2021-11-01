// First we ask the user how big of an array they want
// var limit = parseInt(prompt("How big of an array: "));
// var min = parseInt(prompt("Min value: "));
// var max = parseInt(prompt("Max value: "));

var limit = 100
var min = 1
var max = 1000

var x = [];
var y = [];
var selectedSort = "";
var farger = Array(limit).fill("#ff6384")

var sorts = {
    "selection": selectionSort,
    "bubble": bubbleSort,
    "insertion": insertionSort,
    "heap":heapSort,
    "quick":quickSort,
}


function run() {
    myChart.update("none")
}

function generateArr(){
    x.length = 0
    y.length = 0;
    for(let i = 0; i < limit; i++){
        x.push(i);
        y.push(Math.floor(Math.random() * (max - min) ) + min);
    }
    farger.forEach((e, i) => {
        console.log(e)
        farger[i] = "#ff6384";
    })
    run()
}

var data = {
    labels: x,
    datasets: [{
        label: selectedSort,
        data: y,
        backgroundColor: farger,
        borderColor: 'rgb(255, 99, 132)',
    }]
};

const config = {
    type: 'bar',
    data: data,
    options: {
        animation: {
            duration: 0 
        },
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Sorting Visualizer'
            }
        }
    },
};

const myChart = new Chart(
    document.getElementById('myChart'),
    config
);

async function sleep(msec) {
    return new Promise(resolve => setTimeout(resolve, msec));
}


var generate = document.querySelector("#generate").addEventListener("click", generateArr, false)
var bubble = document.querySelector("#bubble").addEventListener("click", main, false)
var selection = document.querySelector("#selection").addEventListener("click", main, false)
var insertion = document.querySelector("#insertion").addEventListener("click", main, false)
var quick = document.querySelector("#quick").addEventListener("click", main, false)
var heap = document.querySelector("#heap").addEventListener("click", main, false)

function main(e){
    selectedSort = e.target.id;
    sorts[selectedSort](y)
    console.log(e.target)
}
