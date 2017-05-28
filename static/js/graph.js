$(function(){
    $.ajax({
                type:"POST",
                url:"/fetchplots/",
                success:function(response){
                    tripData = response;
                    console.log("Intializing charts with:"+tripData);
                    initChart(tripData);
                },
                dataType:"json"
        });
});

function initChart(tripData){
    //acceleration graphss
    Highcharts.chart('acc-graph-container', {
        chart:{
            events:{
                load:function(){
                    seriesaccy = this.series[0];
                    seriesgyroz = this.series[1];
                    setInterval(function(){
                        $.ajax({
                            type:"POST",
                            url:"/fetchplots/",
                            success:function(response){
                                tripData = response;
                                console.log(tripData);
                                seriesaccy = tripData.yseriesaccy;
                                seriesgyroz = tripData.yseriesgyroz;
                            },
                            dataType:"json"
                        });
                    },1000);
                }
            }
        },
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
            name: 'accy',
            data: tripData.yseriesaccy
        }, {
            name: 'gyroz',
            data: tripData.yseriesgyroz
        }]
    });


    //speed graphs
    Highcharts.chart('speed-graph-container', {
        chart:{
            events:{
                load:function(){
                    seriesspeed = this.series[0];
                    setInterval(function(){
                        $.ajax({
                            type:"POST",
                            url:"/fetchplots/",
                            success:function(response){
                                tripData = response;
                                console.log(tripData);
                                seriesspeed = tripData.yseriesspeed;
                            },
                            dataType:"json"
                        });
                    },1000);
                }
            }
        },
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