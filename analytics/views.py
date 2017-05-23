from django.shortcuts import render
from django.http import HttpResponse
from .models import tripGps,tripAnalytics
from urllib import parse
from django.views.decorators.csrf import csrf_exempt
import json
import math
import numpy as np
import requests

# Create your views here.
@csrf_exempt
def index(request):
	data = parse.unquote(request.POST.get("data"))
	dataSplit = data.split(";")
	accxList = dataSplit[0].split(",")
	accyList = dataSplit[1].split(",")
	gyrozList = dataSplit[2].split(",")
	latdList = dataSplit[3].split(",")
	longtdList = dataSplit[4].split(",")
	speedList = dataSplit[5].split(",")
	speedList_analytics = []

	for i in range(0,len(speedList)):
		for j in range(0,4):
			speedList_analytics.append(speedList[i])
	
	for i in range(0,len(accxList)):
		entry = tripAnalytics(accx=accxList[i],accy=accyList[i],gyroz=gyroxList[i],speed=speedList_analytics[i])
		entry.save()

	for i in range(0,len(latdList)):
		entry = tripGps(latd=latdList[i],longtd=longtdList[i])
		entry.save()
		
	return HttpResponse("ok")


def report(request):
	data = tripData.objects.all().order_by("-created_dt")
	dataAsc = tripData.objects.all().order_by("created_dt")
	discData = data[0::50]

	tripDistance = 0
	tripTimehh = 0
	tripTimemm = 0
	tripTimess = 0
	tripCoords = []
	hardAcceleration = 0
	hardBraking = 0
	sharpTurns = 0
	variance = 0
	standardDeviation = 0
	topSpeed = 0
	speedList = []
	xaxislabels = []
	yseriesaccx = []
	yseriesaccy = []
	yseriesaccz = []
	yseriesspeed = []

	#trip distance
	for d in dataAsc:
		if(d.latd>0):
			startCoord = str(d.latd)+","+str(d.longtd)
			break
	endCoord = str(data[0].latd)+","+str(data[0].longtd)
	url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
	url += "origins="+startCoord+"&destinations="+endCoord+"&key=AIzaSyCmVEv6ZS278G_McB5jz1TyfOnS9EAfArU"
	res = requests.get(url)
	print(startCoord+" "+endCoord)
	responseData = res.json()
	rows = responseData["rows"]
	obj = rows[0]
	elem = obj["elements"]
	distObj = elem[0]["distance"]
	tripDistance = distObj["value"]/1000

	#graph data
	for d in dataAsc:
		if(d.latd > 0):
			xaxislabels.append(str(d.created_dt.replace(microsecond=0)).split("+")[0])
			yseriesaccx.append(d.accx)
			yseriesaccy.append(d.accy)
			yseriesaccz.append(d.accz)
			yseriesspeed.append(d.speed)

	#trip time
	startTime = dataAsc[0].created_dt
	endTime = data[0].created_dt
	distTime = endTime.replace(microsecond=0) - startTime.replace(microsecond=0)
	time = str(distTime)
	time = time.split(":")
	tripTimehh = time[0]
	tripTimemm = time[1]
	tripTimess = time[2]

	#trip coords to plot path
	for obj in discData:
		if(obj.latd>0):
			coord = {"lat":obj.latd,"lng":obj.longtd}
			tripCoords.append(coord)

	#calculate acceleration,braking and sharpturns
	for i in range(1,len(data)):
		speedList.append(data[i].speed)
		if(data[i].accy>2 and data[i-1].accy<2):
			hardAcceleration += 1

		if(math.fabs(data[i].accx)>1 and math.fabs(data[i-1].accx)<1):
			sharpTurns += 1

		if(data[i].accy<-2 and data[i-1].accy>-2):
			hardBraking += 1
	
	#top speed calculation
	topSpeed = max(speedList)

	#variance and standard deviation of speed
	variance = np.var(speedList)
	standardDeviation = np.std(speedList)

	data = {"distance":tripDistance,
	"timehh":tripTimehh,
	"timemm":tripTimemm,
	"timess":tripTimess,
	"coords":tripCoords,
	"acceleration":hardAcceleration,
	"braking":hardBraking,
	"turns":sharpTurns,
	"variance":math.floor(variance),
	"deviation":standardDeviation,
	"topspeed":math.floor(topSpeed),
	"xaxislabels":xaxislabels,
	"yseriesaccx":yseriesaccx,
	"yseriesaccy":yseriesaccy,
	"yseriesaccz":yseriesaccz,
	"yseriesspeed":yseriesspeed}

	return HttpResponse(json.dumps(data))

def acquire_data(request):
	q = tripAnalytics.objects.all().order_by('-created_dt')
	if(len(q)==0):
		return HttpResponse("empty set")
	data = ""
	for i in q:
		data = data + str(i.accx)+"\t"+str(i.accy)+"\t"+str(i.gyroz)+"\t"+str(i.speed)+"<br>"
	return HttpResponse(data)

def dashboard(request):
	return render(request, "dash.html")

