from django.shortcuts import render
from .models import subscribers,queries
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def subscribe(request):
	email=request.POST['email']
	subscriber=subscribers.objects.filter(email=email)
	if subscriber:
		return HttpResponse("Already Subscribed.!")
	else:
		subscriber=subscribers(email=email)
		subscriber.save()
		return HttpResponse("You are awesome.!")

def index(request):
	return render(request,"index.html")

def four(request):
	return render(request,"404.html")



@csrf_exempt
def query(request):
	email=request.POST['email']
	query=request.POST['query']
	name=request.POST['name']
	query=queries(name=name,email=email,query=query)
	query.save()
	return HttpResponse("We will get back to you soon.!")

