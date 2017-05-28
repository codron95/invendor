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
                    seriesaccx = this.series[0];
                    seriesaccy = this.series[1];
                    seriesaccz = this.series[2];
                    setInterval(function(){
                        $.ajax({
                            type:"POST",
                            url:"/fetchplots/",
                            success:function(response){
                                tripData = response;
                                console.log(tripData);
                                seriesaccx = tripData.yseriesaccx;
                                seriesaccy = tripData.yseriesaccy;
                                seriesaccz = tripData.yseriesaccz;
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