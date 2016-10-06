from django.db import models
from datetime import datetime

# Create your models here.
'''
Request Statuses

0 -> pending
1 -> accepted
2 -> closed
'''
class hospital(models.Model):
	name = models.CharField(max_length=50,default="")
	loc = models.CharField(max_length=20,default="0,0")
	desc = models.TextField(default="")
	phone = models.CharField(max_length=15,default="")
	created_dt = models.DateTimeField(auto_now=False,auto_now_add=True,blank=True)
	username = models.CharField(max_length=20,default="hospital")
	password = models.CharField(max_length=20,default="bla")

	def __str__(self):
		return self.name

class user(models.Model):
	name = models.CharField(max_length=30,default="")
	car = models.CharField(max_length=100,default="")
	phone = models.CharField(max_length=15,default="")
	address = models.TextField(default="")
	created_dt = models.DateTimeField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.name

class request(models.Model):
	loc = models.CharField(max_length=20,default="0,0")
	status = models.IntegerField(default=0)
	intent = models.ManyToManyField(hospital,related_name="requests")
	tries = models.IntegerField(default=0)
	acceptee = models.ForeignKey(hospital,related_name="accepts",default=1)
	user = models.ForeignKey(user,related_name="requests",default=-1)
	created_dt = models.DateTimeField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.user.name