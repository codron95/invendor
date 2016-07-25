from django.db import models

# Create your models here.
class plug(models.Model):
	s1=models.IntegerField(default=0)
	s2=models.IntegerField(default=0)
	key=models.CharField(default="",max_length=16)

	def __str__(self):
		return self.key
