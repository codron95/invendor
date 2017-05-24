function initChart(tripData){
    //acceleration graphss
    Highcharts.chart('acc-graph-container', {
        title: {
            text: 'Acceleration Graphs',
            x: -20 //center
        },
        yAxis: {
            title: {
                text: 'm/s-2'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'accx',
            data: tripData.yseriesaccx
        }, {
            name: 'accy',
            data: tripData.yseriesaccy
        }, {
            name: 'gyroz',
            data: tripData.yseriesaccz
        }]
    });


    //speed graphs
    Highcharts.chart('speed-graph-container', {
        title: {
            text: 'Speed',
            x: -20 //center
        },
        yAxis: {
            title: {
                text: 'Km/h'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'speed',
            data: tripData.yseriesspeed
       }]
    });
}