/* D3 import of data from csv */
Promise.all([
    d3.csv("./tests/Test_hist.csv")])
.then(function(files) {
    var data = files[0]; // file with financial history

    var dates = []; // dates for balance history
    var balances = []; // balance history

    for (var i = 0; i < data.length; i++) { // read through each line
        dates.push(data[i]["Date End"]) // add end date
        balances.push(data[i]["Balance"]) // add balance
    }

    /* --------- Line Chart --------- */
    /* Get canvas to draw on */
    var ctx = document.getElementById("line").getContext("2d") 
    
    /* Define dataset */
    const dataBal = {
        labels: dates,
        datasets: [{
            label: 'Finance History',
            data: balances,
            fill: false,
            backgroundColor: 'rgb(0,0,0)',
            tension: 0.1
        }]
    };

    /* Make line cart */
    const chart = new Chart(ctx, {
        type: 'line',
        data: dataBal,
    });
});