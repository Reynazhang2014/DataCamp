function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel
  var metadata = d3.select("#sample-metadata").html("");
  
  var url1 = `/metadata/${sample}`;
  d3.json(url1).then(sample_metadata => {
    console.log(sample_metadata);
    metadata.append("ul");
    metadata.append("li",sample_metadata["sample"]);
    metadata.append("li",sample_metadata["ETHNICITY"]);



  })
  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`

    // Use `.html("") to clear any existing metadata

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var default_url = '/samples/940';
  d3.json(default_url).then(data => {
    // Pie chart
    let trace = {
      labels: data.otu_labels.slice(0,10),
      values: data.sample_values.slice(0,10),
      text: data.otu_ids.slice(0,10),
      type:'pie'
    };
    let data_arr = [trace];
    let layout = {
      height: 500,
      width: 600,
      showlegend: false
    };
    Plotly.plot('pie', data_arr,layout);

    // Bubble Chart
    let trace1 = {
		  x: data.otu_ids,
		  y: data.sample_values,
		  text: data.otu_labels,
		  mode: 'markers',
		  marker: {
		    size: data.sample_values,
		    color: data.otu_ids,
		    colorscale: "Earth"
		  }
		};

		let  data_arr1 = [trace1];

		var layout1 = {
		  title: 'Fancy Bubbles',
		  showlegend: false,
		  height: 600,
		};

		Plotly.newPlot('bubble', data_arr1, layout1);

  })

  d3.json(`/samples/${sample}`).then(data => {
    console.log(data);
    Plotly.restyle('pie',"labels", [data.otu_labels.slice(0,10)]);
    Plotly.restyle('pie',"values", [data.sample_values.slice(0,10)]);
    Plotly.restyle('pie','text',[data.otu_ids.slice(0,10)]);

    Plotly.restyle('bubble','x',[data.otu_ids]);
    Plotly.restyle('bubble','y',[data.sample_values]);
    Plotly.restyle('bubble','text',[data.otu_labels]);
    Plotly.restyle('bubble','marker.size',[data.sample_values]);
    Plotly.restyle('bubble','marker.color',[data.otu_id]);


    
    //Plotly.plot

  })

    // @TODO: Build a Bubble Chart using the sample data


    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
