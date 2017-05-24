var tripData;
var map;
$(function(){
		$.ajax({
		type:"POST",
		url:"/report/",
		data:{csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
		success:function(response){
			tripData = response;
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
    
var map,marker,i=0;
function initMap() {
    var uluru = {lat: -25.363, lng: 131.044};
    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 17,
      center: uluru
    });
    
    marker = new google.maps.Marker({
      position: uluru,
      map: map
    });

    updateLocation(marker);
}

function updateLocation(marker){
setInterval(fetch_data,1000,marker);
}

function fetch_data(marker){
	$.ajax({
		url:"/track/",
		type:"post",
		contentType:"application/x-www-form-urlencoded",
		success: function(response){
			latlng = response.split(",");
    console.log(response);
    loc = new google.maps.LatLng(parseFloat(latlng[0]),parseFloat(latlng[1]));
			marker.setPosition(loc);
    map.panTo(loc)

		}
	});
}