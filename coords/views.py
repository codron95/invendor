from django.shortcuts import render
from django.http import HttpResponse
from .models import request,hospital,user
from django.views.decorators.csrf import csrf_exempt
from geopy.distance import great_circle
import json
from datetime import datetime
from django.utils import timezone
import urllib

# Create your views here.
@csrf_exempt
def reg_request(req):
	no = req.GET.get('no')
	string = urllib.parse.unquote(req.GET.get('string'))

	data = []

	slice1 = string.split("<")[1]
	slice2 = slice1.split(">")[0]
	p1 = tuple(slice2.split(","))

	hospitals = hospital.objects.all()
	for h in hospitals:
		d = {}
		p2 = tuple(h.loc.split(","))
		d['id'] = h.id
		d['name'] = h.name
		d['distance'] = great_circle(p1,p2).kilometers
		data.append(d)

	for i in range(3):
		for j in range(len(data)-1-i):
			if(data[j]['distance']<=data[j+1]['distance']):
				temp=data[j+1]
				data[j+1]=data[j]
				data[j]=temp

	cur_user = user.objects.filter(phone=no.strip())

	cur_req = request()
	cur_req.loc=",".join(p1)
	cur_req.user = cur_user[0]
	cur_req.save()
	for i in range(3):
		h = hospital.objects.filter(id=data[len(data)-i-1]['id'])
		cur_req.intent.add(h[0])
	cur_req.save()

	return HttpResponse("registered")

@csrf_exempt
def get_requests(request):
	hospital_id = request.POST.get('id',-1)
	status = request.POST.get('status',0)

	data=[]

	if hospital_id == -1:
		error={}
		error['error']="data missing"
		return HttpResponse(json.dumps(error))

	result = hospital.objects.filter(id=hospital_id)
	
	if(int(status)==0):
		requests = result[0].requests.filter(status=status)
	else:
		requests = result[0].requests.filter(status=status,acceptee__id=hospital_id)

	for request in requests:
		dur = (timezone.now() - request.created_dt).total_seconds()
		print(datetime.now())
		days = int(dur // 86400)
		hours = int((dur%86400)//3600)
		minutes = int(((dur%86400)%3600)//60)
		seconds = int((((dur%86400)%3600)%60))

		d = {}
		d['id'] = request.id
		d['loc'] = request.loc
		d['tries'] = request.tries
		d['elapsed_time'] = str(days)+":"+str(hours)+":"+str(minutes)+":"+str(seconds)
		d['username'] = request.user.name
		d['car'] = request.user.car
		d['status'] = request.status
		if(d['status']==1):
			d['acceptee_name'] = request.acceptee.name
			d['acceptee_id'] = request.acceptee.id
		data.append(d)

	return HttpResponse(json.dumps(data))

@csrf_exempt
def set_status(req):
	request_id = req.POST.get('id',-1)
	status = int(req.POST.get('status',1))
	hospital_id = req.POST.get('hospital_id',-1)

	if request_id == -1 or hospital_id == -1:
		error={}
		error['error']="data missing"
		return HttpResponse(json.dumps(error))

	cur_hospital = hospital.objects.filter(id=hospital_id)[0]

	cur_req = request.objects.filter(id=request_id)[0]
	if(status==0):
		cur_req.tries = cur_req.tries+1
	elif(status==1):
		cur_req.acceptee = cur_hospital
	cur_req.status = status
	cur_req.save()
	return HttpResponse(str(status))

@csrf_exempt
def auth(request):
	username=request.POST.get('username',-1)
	password=request.POST.get('password',-1)
	error={}

	if username == -1 or password == -1:
		error['error']="data missing"
		return HttpResponse(json.dumps(error))


	result=hospital.objects.filter(username=username,password=password).values("name","id")

	if len(result)>0:
		res=result[0]
		res['error']="no error"
		return HttpResponse(json.dumps(result[0]))
	else:
		error['error']="failed"
		return HttpResponse(json.dumps(error))



