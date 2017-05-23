from django.db import models

# Create your models here.
class tripGps(models.Model):
	
	
	latd = models.FloatField(default=0)
	longtd = models.FloatField(default=0)
	created_dt = models.DateTimeField(auto_now=False,auto_now_add=True,blank=True)

	def __str__(self):
		return str(self.created_dt)

class tripAnalytics(models.Model):

	accx = models.FloatField(default=0)
	accy = models.FloatField(default=0)
	gyroz = models.FloatField(default=0)
	speed = models.FloatField(default=0)
	created_dt = models.DateTimeField(auto_now=False,auto_now_add=True,blank=True)

	def __str__(self):
		return str(self.created_dt)
