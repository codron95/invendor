var tripData;
var map;
$(function(){
		$.ajax({
		type:"POST",
		url:"/report/",
		data:{csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
		success:function(response){
			tripData = response;
			console.log(tripData.coords[0]);
			map.panTo(tripData.coords[0])
			drawPath(tripData);
			initChart(tripData);
			$(".distance-stat").text(tripData.distance);
			$(".time-stat-min").text(tripData.timemm);
			$(".time-stat-sec").text(tripData.timess);
			$(".acc-stat").text(tripData.acceleration);
			$(".brake-stat").text(tripData.braking);
			$(".sturn-stat").text(tripData.turns);
			$(".variance-stat").text(tripData.variance);
			$(".topspeed-stat").text(tripData.topspeed);
		},
		dataType:"json"
	});
});

function initMap() {
	map = new google.maps.Map(document.getElementById('map'),{
	zoom: 18,
	scrollwheel:false,
	center: {lat: 0, lng: -180},
	mapTypeId: 'terrain'
});
}

function drawPath(data){
	var directionsService = new google.maps.DirectionsService;
	var directionsDisplay = new google.maps.DirectionsRenderer;

	directionsService.route({
          origin: data.coords[0],
          destination: data.coords[data.coords.length-1],
          travelMode: google.maps.TravelMode["DRIVING"]
        }, function(response, status) {
          if (status == 'OK') {
            directionsDisplay.setDirections(response);
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });

	directionsDisplay.setMap(map);
}