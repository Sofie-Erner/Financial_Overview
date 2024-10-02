/* D3 import of data from csv */
Promise.all([
    d3.csv("./tests/Test_hist.csv"),
    d3.csv("./assets/colour_pal.csv") // from https://mk.bcgsc.ca/colorblind/palettes/15.color.blindness.palette.txt
])
.then(function(files) {
    var data = files[0];
    var dataColours = files[1];

    /* Get expense categories */
    const cats = data.columns.slice(4);
    //console.log(cats);

    // Set amount of categories
    const n_cats = cats.length;

    /* Get sum for each category */
    let datas = new Array(n_cats); for (let i=0; i<n_cats; ++i) datas[i] = 0;

    for (var i = 0; i < data.length; i++) { // read through each line
        for (var j = 0; j < n_cats; j++){ // get each category sum
            datas[j] = datas[j] + parseFloat(data[i][cats[j]]); // add to total sum
        }
    }
    //console.log(datas);

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

    /* Get canvas to draw on */
    var ctx = document.getElementById("pie").getContext("2d") 
    
    /* Define dataset */
    const catData = {
        labels: cats,
        datasets: [{
            label: 'Finance Categories',
            data: datas,
            hoverOffset: 1,
            backgroundColor: function(context) { // asign colours from palette
                return palette[context.dataIndex % palette.length];
            }
        }]
    };

    /* Make pie cart */
    const chart = new Chart(ctx, {
        type: 'pie',
        data: catData,
    });
});