from django.shortcuts import render,HttpResponse
from .models import plug

# Create your views here.
def status(request):
	plugs=plug.objects.all()
	p=plugs[0]
	result=str(p.s1)+","+str(p.s2)

	return HttpResponse(result)


def set_status(request):
	v1=request.GET.get("s1",-1)
	v2=request.GET.get("s2",-1)

	plugs=plug.objects.all()
	p=plugs[0]
	if v1 != -1:
		p.s1=v1
	if v2 != -1:
		p.s2=v2

	p.save()
	return HttpResponse("ok")
