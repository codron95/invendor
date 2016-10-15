from django.db import models

# Create your models here.
class subscribers(models.Model):
	email=models.CharField(max_length=30,default='anonymous@gmail.com')

	def __str__(self):
		return self.email

class queries(models.Model):
	email=models.CharField(max_length=30,default='anonymous@gmail.com')
	name=models.CharField(max_length=30,default='anonymous@gmail.com')
	query=models.TextField(default='No Content')

	def __str__(self):
		return self.name+' '+self.email

class expense(models.Model):
	amount=models.CharField(max_length=30,default='')
	reason=models.TextField(default='')
	created_date=models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.created_date.strftime('%m-%d-%y')+'-----------'+self.amount

class demo(models.Model):
	url = models.CharField(max_length=255,default="-1")

	def __str__(self):
		return self.url

