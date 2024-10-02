/* D3 import of data from csv */
Promise.all([
    d3.csv("./tests/Test_hist.csv"),
    d3.csv("./assets/colour_pal.csv") // from https://mk.bcgsc.ca/colorblind/palettes/15.color.blindness.palette.txt
])
.then(function(files) {
    var data = files[0]; // file with financial history
    var dataColours = files[1]; // file with colours

    const cats = data.columns.slice(4); // Get expense categories
    //console.log(cats);
    const n_cats = cats.length; // number of categories
    /* Get sum for each category */
    let dataCat = new Array(n_cats); for (let i=0; i<n_cats; ++i) dataCat[i] = 0;

    for (var i = 0; i < data.length; i++) { // read through each line
        for (var j = 0; j < n_cats; j++){ // get each category sum
            dataCat[j] = dataCat[j] + parseFloat(data[i][cats[j]]); // add to total sum
        }
    }
    //console.log(dataCat);

    /* Make colour pallette */
    var palette = [];

    const str1 = 'rgb(';
    const str2 = ')';

    for (var i=0; i < dataColours.length; i++){ // loop over colours
        var strOut = str1.concat("",dataColours[i]['r']).concat(",",dataColours[i]['g'])
        strOut =  strOut.concat(",",dataColours[i]['b']).concat("",str2)
        palette.push(strOut); // add rgb code to palette
    }
    //console.log(palette);

    /* --------- Pie Chart --------- */
    /* Get canvas to draw on */
    var ctx = document.getElementById("pie").getContext("2d") 
    
    /* Define dataset */
    const catData = {
        labels: cats,
        datasets: [{
            label: 'Finance Categories',
            data: dataCat,
            hoverOffset: 1,
            backgroundColor: function(context) { // asign colours from palette
                return palette[context.dataIndex % palette.length];
            }}]
    };

    /* Make pie cart */
    const chart = new Chart(ctx, {
        type: 'pie',
        data: catData,
        options: {
            legend: {
                display: true,
                position: "right",
                title: "Categories"
            }}
    });
});