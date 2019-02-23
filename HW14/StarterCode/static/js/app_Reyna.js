// from data.js
var tableData = data;

// YOUR CODE HERE!
let tbody = d3.select('tbody');
;


function filterdata(){
    d3.event.preventDefault();
    // remove already existing table row in the page
    tbody.selectAll('tr').remove();
    let date_time = d3.select("#datetime").property("value");
    let city = d3.select("#cityname").property("value");
    let state = d3.select("#statename").property("value");
    let country = d3.select("#countryname").property("value");
    let shape = d3.select("#shapetype").property("value");
    let filter_data = data;
    // multiple select -- if the no input for one field, consider there is no filter on the input.
    if(date_time !== ""){
        filter_data = filter_data.filter(x => x.datetime === date_time);
    } 
    if(city != ""){
        filter_data = filter_data.filter(x =>
            x.city.toLowerCase() === city.toLowerCase());
    }
    if(state != ""){
        filter_data = filter_data.filter(x => x.state.toLowerCase() === state.toLowerCase());
    }
    if(country != ""){
        filter_data = filter_data.filter(x => x.country.toLowerCase() === country.toLowerCase());
    }
    if(shape != ""){
        filter_data = filter_data.filter(x => x.shape.toLowerCase() === shape.toLowerCase());
    }
    

    filter_data.forEach(row =>{
        var newrow = tbody.append('tr');
        Object.values(row).forEach(value => newrow.append('td').text(value));
    })
}
let button = d3.select('#filter-btn');
button.on('click',filterdata);

